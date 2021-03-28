tweets_mood_df = pd.read_excel('tweets_mood.xlsx')
good_mood_df = tweets_mood_df[tweets_mood_df[2] >= 1.5]
good_mood_tweets = list(good_mood_df[0])
positive_hashtags = [eval(hashtag) for i, hashtag in enumerate(df['hashtags']) if df.loc[i]['text'] in good_mood_tweets]
positive_hashtags = list(itertools.chain(*positive_hashtags))
pd.DataFrame(positive_hashtags).to_excel('positive_hashtags.xlsx')