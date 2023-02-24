import pandas as pd
import spacy
import numpy as np
from sklearn.model_selection import train_test_split


df = pd.read_csv('output.csv', encoding='iso-8859-1')
processed_text = df['content']
processed_summary = df['summary']

nlp = spacy.load("en_core_web_sm", disable=['ner', 'parser'])

text = [str(doc) for doc in nlp.pipe(processed_text, batch_size=5000)]
summary = ['_START_ '+ str(doc) + ' _END_' for doc in nlp.pipe(processed_summary, batch_size=5000)]

df['cleaned_text'] = pd.Series(text)
df['cleaned_summary'] = pd.Series(summary)

max_text_len = 25000
max_summary_len = 1000

cleaned_text = np.array(df['cleaned_text'])
cleaned_summary= np.array(df['cleaned_summary'])

short_text = []
short_summary = []

for i in range(len(cleaned_text)):
    if len(cleaned_summary[i].split()) <= max_summary_len and len(cleaned_text[i].split()) <= max_text_len:
        short_text.append(cleaned_text[i])
        short_summary.append(cleaned_summary[i])
        
post_pre = pd.DataFrame({'content': short_text,'summary': short_summary})

post_pre['summary'] = post_pre['summary'].apply(lambda x: 'sostok ' + x \
        + ' eostok')

x_tr, x_val, y_tr, y_val = train_test_split(
    np.array(post_pre["content"]),
    np.array(post_pre["summary"]),
    test_size=0.1,
    random_state=0,
    shuffle=True,
)
