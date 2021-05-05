import pandas as pd

def line_lenght(cell, min, max):
  return bool(cell.count(" ")+1 >= min) and (cell.count(" ")+1 <= max)

df_clear = pd.read_csv("d:\git\project1\generated\clear_news.csv")

df_clear['norm_len'] = df_clear['title'].apply(line_lenght, min=3, max=20)
#df_clear[df_clear['norm_len'] == True]

df_small = df_clear[~(df_clear['norm_len'] == False)]
del df_small['latin']
del df_small['norm_len']

df_small.to_csv("d:\git\project1\generated\small_news.csv")