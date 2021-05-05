import pandas as pd
import numpy as np
import torch

def lines_max_lenght(old_array):
    max_len = 0
    for i in old_array.values:
        if len(i) > max_len:
            max_len = len(i)
    return max_len
    
def padding(old_array):
    max_lenght = lines_max_lenght(old_array)
    new_array = []
    i = 0 
    for line in old_array.values:
        i+=1
        new_line = line
        #print(line)
        #print(np.zeros(max_lenght-len(line)))
        if (i > 10): break
        #new_line.append(line)
        for i in range(max_lenght-len(line)):
            new_line.append(0)
        new_array.append(new_line)
    return new_array


df_union = pd.read_csv('D:\git\project1\generated\date_time_tokens_array.csv')

padded = df_union.iloc[:, 2:]
attention_mask = np.where(padded != 0, 1, 0)

input_ids = torch.tensor(padded)  
attention_mask = torch.tensor(attention_mask)
with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)[0]

print(padded)