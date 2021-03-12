import tweepy
import codecs
import pandas as pd
import itertools
from collections
import defaultdict
import time

#Add your credentials here
twitter_keys = {
        'consumer_key':        '---YOUR-KEY---',
        'consumer_secret':     '---YOUR-KEY---',
        'access_token_key':    '---YOUR-KEY---',
        'access_token_secret': '---YOUR-KEY---'
}

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = [str(i).zfill(2) for i in range(1, 31)]
hours = [str(i).zfill(2) for i in range(0, 24)]

def parse_tweet(tweet):
    
    return_dict = {'id': tweet['id'],
                    'user_id': tweet['user']['id'],
                    'user_name': tweet['user']['name'],
                    'user_screen_name': tweet['user']['screen_name'],
                    'user_description': tweet['user']['description'],
                    'user_follower_count': tweet['user']['followers_count'],
                    'quote_count': tweet['quote_count'],
                    'reply_count': tweet['reply_count'],
                    'retweet_count': tweet['retweet_count'],
                    'retweeted_status': 'true' if tweet.get('retweeted_status') else 'false'}
    try:
        return_dict['hashtags'] = [hashtag['text'] for hashtag in tweet['extended_tweet']['entities']['hashtags']]
        return_dict['text'] = tweet['extended_tweet']['full_text']
    except:
        try:
            return_dict['hashtags'] = [hashtag['text']\
                                       for hashtag in tweet['retweeted_status']['extended_tweet']['entities']['hashtags']]
            return_dict['text'] = tweet['retweeted_status']['extended_tweet']['full_text']
        except:
            return_dict['hashtags'] = [hashtag['text']\
                                       for hashtag in tweet['entities']['hashtags']]
            return_dict['text'] = tweet['text']

    return return_dict


def write_tweets_to_file(tweets, date):
    for tweet in tweets:
        with codecs.open(f'tweets_{date}.txt', 'a', encoding='utf-8') as file:
            file.write(f'{tweet}\n')

for day in days[6:28]:
    results = []
    for hour in hours:
        print(f'day: {day}, hour: {hour}')
        
        for trial in range(5):
            print(f'trial: {trial+1} / 5')
            try:
                results.append(api.search_30_day('thesis', '#SmartContracts', fromDate=f'202102{day}{hour}00', 
                                                                          toDate=f'202102{day}{hour}59'))
                break
                
            except:
                print('Sleeping for 60 seconds...')
                time.sleep(60)
    
    tweets = []
    for res in results:
        for r in res:
            tweets.append(parse_tweet(r._json))
            
    write_tweets_to_file(tweets, f'202102{day}')
    
    columns = defaultdict(list)
    for tweet in tweets:
        for key, val in tweet.items():
            columns[key].append(val)
            
    df = pd.DataFrame(columns)
    df.to_excel(f'tweets_202102{day}.xlsx', index=False)
    
    hashtags = list(itertools.chain(*[tweet['hashtags'] for tweet in tweets]))
    df_hashtags = pd.DataFrame(hashtags)
    df_hashtags.to_excel(f'hashtags_202102{day}.xlsx', index=False)