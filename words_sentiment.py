words_for_sentiment = list(df_words_text[0])
words_sentiment = []

for word in words_for_sentiment:
    d = nlp(word)
    words_sentiment.append((word, d.sentences[0].sentiment))
    
sentiment_df = pd.DataFrame(words_sentiment)
sentiment_df.to_excel('words_sentiment.xlsx')