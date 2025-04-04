import torch
import json
import os


def top_k_p_sample(probs, top_k, top_p):
    sorted_indices = torch.argsort(probs, descending=True)[0]  #argsort返回排序后的索引，从大到小
    sorted_probs = probs[0][sorted_indices]         #排序后的概率
    print(f"sorted_indices : {sorted_indices}")
    print(f"sorted_probs : {sorted_probs}")

    #计算累积概率，找到满足累积概率>= top_p 的最小集合
    cumulative_probs = torch.cumsum(sorted_probs, dim=-1)  #沿dim方向累积求和
    print(f"cumulative_probs : {cumulative_probs}")
    last_index = torch.where(cumulative_probs >= top_p)[0]
    print(f"last_index : {last_index}")
    last_index = last_index[0] if len(last_index)!=0 else len(cumulative_probs)

    #先进行top_k截断，再进行top_p截断
    sorted_indices = sorted_indices[:last_index+1]
    sorted_indices = sorted_indices[:top_k]
    print(f"sorted_indices : {sorted_indices}")

    #将选出的概率进行重新归一化
    final_probs = probs[0][sorted_indices]
    print(f"final_probs : {final_probs}")
    final_probs /= final_probs.sum()
    print(f"final_probs : {final_probs}")
    return final_probs, sorted_indices

# probs = torch.tensor([[0.1 , 0.23 , 0.12 , 0.02 , 0.05 , 0.03 , 0.24 , 0.21]])

# # probs, indices = top_k_p_sample(probs, 3, 0.9)

# final_probs, sorted_indices = top_k_p_sample(probs, 3, 0.9)
# generated_token_prob_index = sorted_indices[torch.multinomial(final_probs, num_samples=1).item()].item()
# generated_token_prob = probs[0][generated_token_prob_index].item()

# print(f"generated_token_prob_index : {generated_token_prob_index}")
# print(f"generated_token_prob : {generated_token_prob}")

def process_indented_block(code):
    if code.rstrip().endswith(":"):
        last_line = code.rstrip("\n").split("\n")[-1]
        if last_line.lstrip().startswith("while"):
            code = code.rstrip("\n")+" break \n"
        else:
            code = code.rstrip("\n")+" pass \n"
    return code

input_code = "while True:\n    n = 10\nif n >= 10:"
output = process_indented_block(input_code)
print(output)