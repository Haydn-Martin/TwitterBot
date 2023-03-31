import re

tweet = 'Let’s go! What happens if I tweet two lines... Actually what happens if I run over my tweet limit. How many lines is too many? Extra bit.\n'


# regex dict
rep_dict = {'. ': '.\n\n',
            '? ': '?\n\n',
            '! ': '!\n\n'}

tweet =


test_tweet = tweet
for x in rep_dict.keys():
    test_tweet = test_tweet.replace(x, rep_dict[x])

print(test_2)
print(test_tweet)

def format_tweet(raw_tweet):

    tweet_list = raw_tweet.split('. ')
    formatted_tweet = ''

    for line in tweet_list:

        if line.find('? ') != -1:
            ques_lines = line.split('? ')
            for i in range(len(ques_lines)):
                if i != (len(ques_lines)-1):
                    formatted_tweet = formatted_tweet + ques_lines[i] + '?\n\n'
                else:
                    formatted_tweet = formatted_tweet + ques_lines[i] + '.\n\n'
        else:
            formatted_tweet = formatted_tweet + line + '.\n\n'

    return formatted_tweet[:-4]

print(format_tweet(tweet))