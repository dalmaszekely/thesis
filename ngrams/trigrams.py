import pandas as pd
import nltk
import collections

tweets_df = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')
tweets = tweets_df['text']

def create_trigrams(tweets):

    trigrams = []
    for tweet in tweets:
        no_symbols = [word.lower().strip('.,?!+-*') for word in tweet.split() if '#' not in word\
                     and '@' not in word and '$' not in word]
        filtered_tweet = [elem['text'] for elem in filter_words(' '.join(no_symbols))]

        trigrams.append(list(nltk.ngrams(filtered_tweet, 3)))
        
    return trigrams

trigrams = create_trigrams(tweets)
trigrams = list(itertools.chain(*trigrams))
trigram_frequency = collections.Counter(trigrams).most_common()
frequency_df = pd.DataFrame(trigram_frequency)
frequency_df.to_excel('trigram.xlsx')