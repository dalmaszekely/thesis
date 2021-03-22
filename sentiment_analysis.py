import codecs
import collections
import stanza
nlp = stanza.Pipeline('en')

results = []

#tweets comes from words_from_tweets.py

for i, tweet in enumerate(tweets):
    d = nlp(tweet)
    res = []
    for sentence in d.sentences:
        res.append(sentence.sentiment)
    results.append((tweet, res, sum(res)/len(res)))
    
    if i % 10 == 0:
        print(f'{i} / {len(tweets)}')


with codecs.open('sentiment.txt', 'a', 'utf-8') as file:
    file.write(str(results))

counter = []

for r in results:
    counter.append(dict(collections.Counter(r[1])))

with codecs.open('sentiment_counter.txt', 'a', 'utf-8') as file:
    file.write(str(counter))
    
with codecs.open('sentiment.txt', 'r', 'utf-8') as file:
    tweets_mood = file.read()

tweets_mood = eval(tweets_mood)
df_tweets_mood = pd.DataFrame(tweets_mood)
df_tweets_mood['counter'] = counter
df_tweets_mood.to_excel('tweets_mood.xlsx')

numbers = [tweet[1] for tweet in tweets_mood]
numbers = list(itertools.chain(*numbers))
collections.Counter(numbers)