import torch
import numpy as np
import torch.nn as nn
from torch.nn import functional as F
import os

batch_size = 32
block_size = 8
max_iters = 3000            #训练周期
eval_interval = 300         #每多少个训练周期进行验证
learning_rate = 1e-2
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 20             #验证周期
torch.manual_seed(1337)
#----------------------------------------------------------



def read_data(input_file):
    if os.path.exists(input_file):
        with open(input_file , 'r' , encoding='utf-8') as f:
            text = f.read()
    else:
        print("The file not exists")
        text = None

    return text
    

input_file = os.path.join(os.getcwd() , 'zero-to-hero' , 'input.txt')
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


class BiagramLanguageModel(nn.Module):
    def __init__(self , vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size , vocab_size)

    def forward(self , idx , targets=None):
        logits = self.token_embedding_table(idx)

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
            logits , loss = self(idx)
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

for iter in range(max_iters):
    if iter % eval_interval == 0:
        losses = estimate_loss(model)
        print(f"step {iter}: train loss: {losses['train']:.4f} , val loss: {losses['val']:.4f}")
    
    xb , yb = get_batch('train')
    logits , loss = model(xb , yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

context = torch.zeros((1 , 1) , dtype=torch.long , device=device)
print(decode(model.generate(context , max_new_tokens=500)[0].tolist()))
