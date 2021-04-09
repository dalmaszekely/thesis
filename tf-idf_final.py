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
        raw_count[word] = math.log(N / float(val))

## tf-idf

def me_computeTFIDF(tfBagOfWords, idfs):
    words =[]
    tfs = []
    idfs = []
    tfidfs = []
    for word, val in tfBagOfWords.items():
        tfidf[word] = {word, val, idfs[word], val * idfs[word]}
        #print(word, val, idfs[word], tfidf[word])
        
        me_word.append(word)
        me_tf.append(val)
        me_idf.append(idfs[word])
        me_tfidf.append(val*idfs[word])
    pd.DataFrame(words).to_excel('tf-idf_words.xlsx')
    pd.DataFrame(tfs).to_excel('tf-idf_tfs.xlsx')
    pd.DataFrame(idfs).to_excel('tf-idf_idfs.xlsx')
    pd.DataFrame(tfidfs).to_excel('tf-idf_tfidfs.xlsx')

all_tf = computeTF(raw_count, all_words)
me_tfidf = me_computeTFIDF(all_tf, raw_count)