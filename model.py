import pandas as pd
import spacy
from time import time
import matplotlib.pyplot as plt

def loadData():
    df = pd.read_csv('output.csv', encoding='iso-8859-1')
    processed_text = df['content']
    processed_summary = df['summary']

    nlp = spacy.load("en_core_web_sm", disable=['ner', 'parser'])

    text = [str(doc) for doc in nlp.pipe(processed_text, batch_size=5000)]
    summary = ['_START_ '+ str(doc) + ' _END_' for doc in nlp.pipe(processed_summary, batch_size=5000)]

    df['cleaned_text'] = pd.Series(text)
    df['cleaned_summary'] = pd.Series(summary)

    return df

def plotMaxPermissibleSequence():
    text_count = []
    summary_count = []

    for sent in df['cleaned_text']:
        text_count.append(len(sent.split()))
        
    for sent in df['cleaned_summary']:
        summary_count.append(len(sent.split()))

    graph_df = pd.DataFrame() 

    graph_df['text'] = text_count
    graph_df['summary'] = summary_count

    graph_df.hist(bins = 5)
    plt.show()

def countMaxPermissibleSequence(df, data, start, end):
    cnt = start
    for i in df[data]:
        if len(i.split()) <= end:
            cnt = cnt + 1
    return cnt / len(df[data])

df =loadData()
print(countMaxPermissibleSequence(df, "cleaned_text", 0, 25000))
print(countMaxPermissibleSequence(df, "cleaned_summary", 0, 1000))

max_text_len = 25000
max_summary_len = 1000