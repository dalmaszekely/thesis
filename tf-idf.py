## Term Frequency - tf

clean_tweets = [tweet.split() for tweet in tweets]
clean_tweets = [[word.lower().strip('#&@+-*.-:?!') for word in clean_tweet] for clean_tweet in clean_tweets]
clean_tweets = [[word for word in tweet if word in unique_words] for tweet in clean_tweets]
num_of_words = dict.fromkeys(unique_words, 0)

num_of_words_list = []

for tweet in clean_tweets:
    temp_dict = num_of_words.copy()
    for word in tweet:
        temp_dict[word] += 1
    num_of_words_list.append(temp_dict)

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfs = [computeTF(now, ct) for now, ct in zip(num_of_words_list, clean_tweets)]

## Inverse Document Frequency - idf

def computeIDF(documents):
    import math
    N = len(documents)   
    for word, val in raw_count.items():
        print(word, val)
        raw_count[word] = math.log(N / float(val))

## tf-idf

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfs = [computeTFIDF(tf, raw_count) for tf in tfs]
tfidfs = [dict(sorted(df_tfidfs.sum().items(), key=lambda t: t[1], reverse=True)) for tfidf in tfidfs]
df_tfidfs = pd.DataFrame(tfidfs)
important_words = dict(sorted(df_tfidfs.sum().items(), key=lambda t: t[1], reverse=True))
pd.DataFrame(important_words.items()).to_excel('tf-idf.xlsx')