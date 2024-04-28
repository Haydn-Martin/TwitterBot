# Reading lines from txt file
filename = open('Tweets/Tweets.txt', 'r')
all_tweets = filename.readlines()
filename.close()

# Reading lines from sent tweets file
filename = open('Tweets/Sent_Tweets.txt', 'r')
sent_tweets = filename.readlines()
filename.close()

# Removing tweet number for list comparison
def og_tweet(line):
    length = len(line)
    for i in range(length):
        if line[i] == ':':
            new_line = line[i + 2:length]
            break
    return new_line

sent_tweets_og = list(map(lambda x: og_tweet(x), sent_tweets))

# Saving unsent tweets in list
unsent_tweets = []
for tweet in all_tweets:

    if tweet not in sent_tweets_og:

        # Saving unsent tweets in txt
        archive = open('Tweets/Unsent_Tweets.txt', 'a')
        archive.writelines(tweet)
        archive.close()

        unsent_tweets.append(tweet)