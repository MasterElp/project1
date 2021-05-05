import re
import pandas as pd

def is_latin(cell):
  return bool(not re.search(r'[^0-9a-zA-Z~`!@#$%^&*()_+{}\[\];:\'",<.>/?\\| -_=+]', cell))
  
df = pd.read_csv("d:\git\project1\generated\datetime_news.csv")

df['latin'] = df['title'].apply(is_latin)
#df[df['latin'] == False]
df_clear = df[~(df['latin'] == False)]

df_clear.to_csv("d:\git\project1\generated\clear_news.csv")