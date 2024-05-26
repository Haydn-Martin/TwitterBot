# Twitter_Bot

Twitter bot for automated tweeting using python.

Note: functinality affected by Twitter API v1.1 deprecation

## Usage - Tweeting

- `auto_tweets.py` posts tweets stored in `Tweets.txt`
- Tweets that are too long are stored in `Long_Tweets.txt`
- Use `Unsent_Gen.py` to find all tweets in `Tweets.txt` that haven't been sent (because they don't appear in `Sent_Tweets.txt`)
- Use `delete_tweets.ipynb` to delete tweets

## Deleting Tweets

- Follow the tutorial outlined here: [https://www.youtube.com/watch?v=jB1-z6LbX5w&t=248s&ab_channel=LucaHammer]
- Note: you may have to launch chrome with the `--disable-web-security` argument to negate CORS issues
