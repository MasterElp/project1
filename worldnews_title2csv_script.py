from sklearn.metrics import mean_squared_error
import re
from nltk.corpus import stopwords
import pymorphy2

def review_to_wordlist(review):
    #1)
    review_text = re.sub("[^а-яА-Яa-zA-Z]"," ", review)
    #2)
    words = review_text.lower().split()
    #3)
    words = [w for w in words if not w in stops]
    #4)
    words = [morph.parse(w)[0].normal_form for w in words ]
    return(words)

morph = pymorphy2.MorphAnalyzer()
stops = set(stopwords.words("english"))

df = pd.read_csv("d:\git\project1\datetime_news.csv")
%% time
df['title'] = df['title'].apply(review_to_wordlist)
print(df)