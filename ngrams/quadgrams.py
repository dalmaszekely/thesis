import pandas as pd
import nltk
import collections

tweets_df = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')
tweets = tweets_df['text']

def create_quadgrams(tweets):

    quadgrams = []
    for tweet in tweets:
        no_symbols = [word.lower().strip('.,?!+-*') for word in tweet.split() if '#' not in word\
                     and '@' not in word and '$' not in word]
        filtered_tweet = [elem['text'] for elem in filter_words(' '.join(no_symbols))]

        quadgrams.append(list(nltk.ngrams(filtered_tweet, 4)))
        
    return quadgrams

quadgrams = create_quadgrams(tweets)
quadgrams = list(itertools.chain(*quadgrams))
quadgram_frequency = collections.Counter(quadgrams).most_common()
frequency_df = pd.DataFrame(quadgram_frequency)
frequency_df.to_excel('quadgram.xlsx')