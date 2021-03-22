words_merged = list(itertools.chain(*words))
words_text = [(word['text'], word['upos']) for word in words_merged if '#' not in word['text']\
             and '@' not in word['text'] and '$' not in word['text']]
df_words_text = pd.DataFrame(words_text)
df_words_text.to_excel('tweet_words.xlsx')