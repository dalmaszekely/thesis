tweets_mood_df = pd.read_excel('tweets_mood.xlsx')
bad_mood_df = tweets_mood_df[tweets_mood_df[2] <= 0.5]
bad_mood_tweets = list(bad_mood_df[0])
negative_hashtags = [eval(hashtag) for i, hashtag in enumerate(df['hashtags']) if df.loc[i]['text'] in bad_mood_tweets]
negative_hashtags = list(itertools.chain(*negative_hashtags))
pd.DataFrame(negative_hashtags).to_excel('negative_hashtags.xlsx')