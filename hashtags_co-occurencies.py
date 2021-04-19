tweets_df = pd.read_excel('tweetek_retweetekNélkül_0207-0304.xlsx')

tweets_hashtags = tweets_df['hashtags']

tweets_hashtags = [eval(hashtags) for hashtags in tweets_hashtags]

tweets_hashtags = [[hashtag.lower() for hashtag in hashtags] for hashtags in tweets_hashtags]

tweets_hashtags[1]

unique_hashtags = set(itertools.chain(*tweets_hashtags))
all_hashtags = list(itertools.chain(*tweets_hashtags))

counter_all_hashtags = collections.Counter(all_hashtags)

counter_hashtags = {hashtag: dict.fromkeys(unique_hashtags, 0) for hashtag in unique_hashtags}

for hashtag in counter_hashtags:
    for hashtags in tweets_hashtags:
        if hashtag in hashtags:
            for hashtag2 in set(hashtags):
                counter_hashtags[hashtag][hashtag2] += 1

top30_hashtags = dict(counter_all_hashtags.most_common()[:30])
top30_counter = {hashtag: counter_hashtags[hashtag] for hashtag in top30_hashtags}

pd.DataFrame(top30_counter).to_excel('hashtags_co-occurence.xlsx')

counter_hashtags = {hashtag: dict(collections.Counter(counter_hashtags[hashtag]).most_common()) for hashtag in counter_hashtags}

def sort_func(hashtag1, hashtag2):
    return counter_all_hashtags[hashtag1] < counter_all_hashtags[hashtag2]

sorted(list(counter_hashtags.items())[:5], key=sort_func)

list(counter_hashtags.items())[:5]

