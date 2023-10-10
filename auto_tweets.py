import tweepy


### FUNCTIONS ###

# New line expressions
rep_dict = {'. ': '.\n\n',
            '? ': '?\n\n',
            '! ': '!\n\n'}

def new_lines(raw_tweet):

    for x in rep_dict.keys():
        raw_tweet = raw_tweet.replace(x, rep_dict[x])
    return raw_tweet

# Check length
def too_long_bool(tweet):

    if len(tweet) > 270:
        long_bool = True
    else:
        long_bool = False
    return long_bool

def save_too_long(tweet):
    # adding tweet to txt
    long_tweets = open('Long_Tweets.txt', 'a')
    long_tweets.writelines(tweet)
    long_tweets.close()

# Check if already sent
def sent_tweet_bool(tweet):

    archive = open('Sent_Tweets.txt', 'r')
    sent_bool = tweet in archive.readlines()
    archive.close()
    return sent_bool

def remove_tweet(tweet):
    # Deleting from all tweets
    with open("Tweets.txt", "r") as f:
        lines = f.readlines()
        f.close()
    with open("Tweets.txt", "w") as f:
        for line in lines:
            if line != tweet:
                f.write(line)

# Saving tweet in txt - these start at 0
def save_sent_tweet(tweet):

    archive = open('Sent_Tweets.txt', 'a')
    archive.writelines(tweet)
    archive.close()

## CONNECTING TO TWITTER ###

# Authenticate to Twitter
auth = tweepy.OAuthHandler() #enter 0Auth details
auth.set_access_token() #enter access token details

# Connect to Twitter API
api = tweepy.API(auth)

### TWEETING ###

bad_tweet = True

while bad_tweet:
    # reading txt file with tweets
    filename = open('Tweets.txt', 'r')
    all_tweets = filename.readlines()
    filename.close()
    tweet = all_tweets[0]

    # checking and sending
    if too_long_bool(tweet):
        save_too_long(tweet)
        remove_tweet(tweet)
        bad_tweet = True
    elif sent_tweet_bool(tweet):
        remove_tweet(tweet)
        bad_tweet = True
    else:
        api.update_status(new_lines(tweet))
        save_sent_tweet(tweet)
        remove_tweet(tweet)
        bad_tweet = False