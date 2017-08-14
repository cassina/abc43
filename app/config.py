import os

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

HOME_TIMELINE_URL = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
POST_TWEET_URL = 'https://api.twitter.com/1.1/statuses/update.json'
