import torch
import pandas as pd
import numpy as np
import pytorch_transformers

model_class = pytorch_transformers.BertModel
tokenizer_class = pytorch_transformers.BertTokenizer
pretrained_weights = 'bert-base-uncased'

model = model_class.from_pretrained(pretrained_weights)

folder = 'd:\git\project1\generated'
df_union = pd.read_csv(f'{folder}\date_time_tokens_array_short.csv')
padded = np.array(df_union.iloc[:, 4:])
attention_mask = np.where(padded != 0, 1, 0)
input_ids = torch.tensor(padded)  
attention_mask = torch.tensor(attention_mask)

with torch.no_grad():
    last_hidden_states = model(input_ids, attention_mask=attention_mask)

classification = pd.DataFrame(last_hidden_states[0][:,0,:])
classification.to_csv(f'{folder}\classification_array.csv')