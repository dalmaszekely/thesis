import pandas as pd
import nltk
import collections

tweets_df = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')
tweets = tweets_df['text']

def create_quintgrams(tweets):

    quintgrams = []
    for tweet in tweets:
        no_symbols = [word.lower().strip('.,?!+-*') for word in tweet.split() if '#' not in word\
                     and '@' not in word and '$' not in word]
        filtered_tweet = [elem['text'] for elem in filter_words(' '.join(no_symbols))]

        quintgrams.append(list(nltk.ngrams(filtered_tweet, 5)))
        
    return quintgrams

quintgrams = create_quintgrams(tweets)
quintgrams = list(itertools.chain(*quintgrams))
quintgram_frequency = collections.Counter(quintgrams).most_common()
frequency_df = pd.DataFrame(quintgram_frequency)
frequency_df.to_excel('quintgram.xlsx')