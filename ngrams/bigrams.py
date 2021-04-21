import pandas as pd
import nltk
import collections

tweets_df = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')
tweets = tweets_df['text']

def create_bigrams(tweets):

    bigrams = []
    for tweet in tweets:
        no_symbols = [word.lower().strip('.,?!+-*') for word in tweet.split() if '#' not in word\
                     and '@' not in word and '$' not in word]
        filtered_tweet = [elem['text'] for elem in filter_words(' '.join(no_symbols))]

        bigrams.append(list(nltk.bigrams(filtered_tweet)))
        
    return bigrams

bigrams = create_bigrams(tweets)
bigrams = list(itertools.chain(*bigrams))
bigram_frequency = collections.Counter(bigrams).most_common()
frequency_df = pd.DataFrame(bigram_frequency)
frequency_df.to_excel('bigram_frequency_with_ner.xlsx')