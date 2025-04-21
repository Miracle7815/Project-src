import torch
import numpy as np
import torch.nn as nn
from torch.nn import functional as F
import os


#hyperparameters
batch_size = 64            #批量大小
block_size = 256           #最大上下文长度
max_iters = 5000            #训练周期
eval_interval = 500         #每多少个训练周期进行验证
learning_rate = 3e-4
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200             #验证周期
torch.manual_seed(1337)
n_embd = 384
n_head = 6
n_layer = 6
dropout = 0.2
#----------------------------------------------------------



def read_data(input_file):
    if os.path.exists(input_file):
        with open(input_file , 'r' , encoding='utf-8') as f:
            text = f.read()
    else:
        print("The file not exists")
        text = None

    return text
    

input_file = os.path.join(os.getcwd() , 'zero-to-hero' , 'nanogpt', 'input.txt')
print(input_file)
text = read_data(input_file)

chars = sorted(list(set(text)))
vocab_size = len(chars)

stoi = {s : i for i , s in enumerate(chars)}
itos = {i : s for i , s in enumerate(chars)}

encode = lambda s : [stoi[c] for c in s]
decode = lambda l : ''.join([itos[i] for i in l])


def build_dataset(text):
    data = torch.tensor(encode(text) , dtype=torch.long)
    n = int(len(text) * 0.9)

    train_data = data[:n]
    val_data = data[n:]

    return train_data , val_data


def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = torch.randint(0 , len(data) - block_size , (batch_size,))
    x = torch.stack([data[i : i + block_size] for i in ix])
    y = torch.stack([data[i + 1 : i + 1 + block_size] for i in ix])
    x , y = x.to(device) , y.to(device)

    return x , y


@torch.no_grad()
def estimate_loss(model):
    out = {}
    model.eval()   #有些网络在不同模式下的工作状态不同，所以需要注意所处模式
    for split in ['train' , 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X , Y = get_batch(split)
            logits , loss = model(X , Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

    
class Head(nn.Module):

    def __init__(self , head_size):
        super().__init__()
        self.key = nn.Linear(n_embd , head_size , bias=False)
        self.query = nn.Linear(n_embd , head_size , bias=False)
        self.value = nn.Linear(n_embd , head_size , bias=False)
        #持久化缓冲区域
        self.register_buffer('tril' , torch.tril(torch.ones(block_size , block_size)))

        self.dropout = nn.Dropout(dropout)

    def forward(self , x):
        B , T , C = x.shape
        k = self.key(x)
        q = self.query(x)
        v = self.value(x)
        #attention score
        wei = q @ k.transpose(-2 , -1) * C ** -0.5      #B * T * T
        wei = wei.masked_fill(self.tril[:T , :T] == 0 , float('-inf'))
        wei = F.softmax(wei , dim=-1)
        wei = self.dropout(wei)
        
        v = self.value(x)
        out = wei @ v        #B * T * C
        return out
    
    
class MultiHeadAttention(nn.Module):
    def __init__(self , num_heads , head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
        #投影回残差路径
        self.proj = nn.Linear(n_embd , n_embd)
        self.dropout = nn.Dropout(dropout)

    def forward(self , x):
        out = torch.cat([h(x) for h in self.heads] , dim=-1)
        out = self.proj(out)
        out = self.dropout(out)
        return out
    

class FeedForward(nn.Module):
    def __init__(self , n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd , 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd , n_embd),
            nn.Dropout(dropout)
        )

    def forward(self , x):
        return self.net(x)


class Block(nn.Module):
    """Transformer block: communication followed by computation """
    
    def __init__(self , n_embd , n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa_head = MultiHeadAttention(n_head , head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self , x):
        #残差链接
        x = x + self.sa_head(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x


class BiagramLanguageModel(nn.Module):
    def __init__(self , vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size , n_embd)
        self.position_embedding_table = nn.Embedding(block_size , n_embd)   #position embedding
        # self.sa_head = Head(n_embd)
        # self.sa_head = MultiHeadAttention(4 , n_embd // 4)
        # self.ffwd = FeedForward(n_embd)
        # self.blocks = nn.Sequential(
        #     Block(n_embd , n_head=4),
        #     Block(n_embd , n_head=4),
        #     Block(n_embd , n_head=4),  
        # )
        self.blocks = nn.Sequential(*[Block(n_embd , n_head=n_head) for _ in range(n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.lm_head = nn.Linear(n_embd , vocab_size)

    def forward(self , idx , targets=None):
        B , T = idx.shape
        token_embd = self.token_embedding_table(idx)    # B * T * C
        pos_embd = self.position_embedding_table(torch.arange(T , device=device))
        x = token_embd + pos_embd
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)     # B * T * vocab_size
        

        if targets == None:
            loss = None
        else:
            B , T , C = logits.shape
            logits = logits.view(B * T , C)
            targets = targets.view(B * T)
            loss = F.cross_entropy(logits , targets)
        
        return logits , loss
    
    def generate(self , idx , max_new_tokens):

        for _ in range(max_new_tokens):
            #idx = B * T 
            idx_cond = idx[: , -block_size:]       #embedding只能支持blocksize长度的上下文
            logits , loss = self(idx_cond)
            logits = logits[: , -1 , :]
            probs = F.softmax(logits , dim=-1)
            idx_next = torch.multinomial(probs , num_samples=1)
            idx = torch.cat((idx , idx_next) , dim=1)

        return idx


train_data , val_data = build_dataset(text)
print(len(train_data) , len(val_data))
# xb , yb = get_batch('train')
# print(xb.shape , yb.shape)

model = BiagramLanguageModel(vocab_size)
model.to(device)

optimizer = torch.optim.AdamW(model.parameters() , lr=learning_rate)

# for iter in range(max_iters):
#     if iter % eval_interval == 0:
#         losses = estimate_loss(model)
#         print(f"step {iter}: train loss: {losses['train']:.4f} , val loss: {losses['val']:.4f}")
    
#     xb , yb = get_batch('train')
#     logits , loss = model(xb , yb)
#     optimizer.zero_grad(set_to_none=True)
#     loss.backward() 
#     optimizer.step()

# context = torch.zeros((1 , 1) , dtype=torch.long , device=device)
# print(decode(model.generate(context , max_new_tokens=500)[0].tolist()))

print(sum(p.numel() for p in model.parameters() if p.requires_grad))