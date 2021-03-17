import stanza
import pandas as pd
import itertools
nlp = stanza.Pipeline('en')

def filter_words(tweet):
    doc = nlp(tweet)
    
    return_list = []
    
    for sentence in doc.sentences:
        word_list = []
        for word in sentence.to_dict():
            if word['upos'] in {'ADJ', 'ADV', 'INTJ', 'NOUN', 'NUM', 'PROPN', 'VERB', 'X'}:
                word_list.append(word)
                
        return_list.append(word_list)
        
    return list(itertools.chain(*return_list))

df_tweets = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')

tweets = list(df_tweets['text'])

words = []

for i, tweet in enumerate(tweets):
    words.append(filter_words(tweet))
    
    if i % 10 == 0:
        print(i)
                          
import codecs

with codecs.open('words.txt', 'a', 'utf-8') as file:
    file.write(str(words))