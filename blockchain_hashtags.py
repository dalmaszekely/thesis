hashtags = list(bc_df['hashtags'])

hashtags = [eval(hashtag) for hashtag in hashtags]

hashtags = list(itertools.chain(*hashtags))

hashtags_df = pd.DataFrame(hashtags)

hashtags_df.to_excel('blockchain_hashtags.xlsx') 