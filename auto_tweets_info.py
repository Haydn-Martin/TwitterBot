import tweepy
import time
from datetime import date
import schedule
from random import randint

# Authenticate to Twitter
auth = tweepy.OAuthHandler("OVKyfFEKOkF41d9S4aHiR8Of6",
    "VWFiNisJXp0wqMzrFTzGYlRdP69ALO77pAxls0XHnmarMuXbww")
auth.set_access_token("1255949337269612546-uq4oaI8gzqYRo1JLdt6WWPqq8NqJf0",
    "bCBILV6NfUs84RAIYPDiLW8VM6t8mtFD2Wr99Rcsonsjn")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



# Reading lines from txt file
filename = open('Tweets.txt', 'r')
tweettext = filename.readlines()
filename.close()

tweet = tweettext[0]

tweet_list = tweet.split('. ')

formatted_tweet = ''

for line in tweet_list:

    if line.find('?') != -1:
        ques_lines = line.split('? ')
        for split_ques_lines in ques_lines:
            if split_ques_lines != (len(ques_lines)-1):
                formatted_tweet = formatted_tweet + split_ques_lines + '?\n\n'
            else:
                formatted_tweet = formatted_tweet + split_ques_lines + '.\n\n'
    else:
        formatted_tweet = formatted_tweet+line+'.\n\n'


formatted_tweet = formatted_tweet[:-4]

api.update_status(formatted_tweet)

# Tweeting lines with some time delay
for line in tweettext: # Will only write first 5 lines
 api.update_status(line)
 print line
 time.sleep(15) # Sleep for 15 seconds

# print line corresponding to today's date - start date
start_date = date(2021, 8, 10)
line = (date.today() - start_date).days

hour = randint(16, 21)
minute = randint(0, 60)
time_string = string(hour)+':'+string(minute)

def tweet():
    api.update_status(tweettext[line])

schedule.every(1).day.at(time_string).do(tweet)

while True:
    schedule.run_pending()
