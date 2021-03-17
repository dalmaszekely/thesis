import pandas as pd
import itertools

df = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')

hashtags = list(df['hashtags'])

hashtags = [eval(hashtag) for hashtag in hashtags]

hashtags = list(itertools.chain(*hashtags))

hashtags_df = pd.DataFrame(hashtags)

hashtags_df.to_excel('hashtags.xlsx')