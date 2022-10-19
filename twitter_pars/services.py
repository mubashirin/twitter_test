from random import randint
import tweepy
from dotenv import load_dotenv
import os


load_dotenv()

auth = tweepy.OAuth1UserHandler(
   os.getenv('API_KEY'),
   os.getenv('API_SECRET_KEY'),
   os.getenv('API_ACCESS_TOKEN'),
   os.getenv('API_ACCESS_TOKEN_SECRET')
)
auth_bearer = tweepy.OAuth2BearerHandler(f"Bearer {os.getenv('API_KEY')}")


def get_random_proxy():
    proxy = [
        'http://uJEM1BHn:HBPjf7Tc@212.193.143.51:48707',
        'http://Q8xxGmcG:56CSHWxE@91.188.221.249:45460',
        'http://Q8xxGmcG:56CSHWxE@195.208.123.248:48634'
    ]
    count = len(proxy)
    return proxy[count - 1]


def get_user_data(name=''):
    api = tweepy.API(auth, proxy=get_random_proxy())
    user = api.get_user(screen_name=name.replace('\r\n', ''))

    data = {
        'id': user.id,
        'name': user.name,
        'username': user.screen_name,
        'following': user.friends_count,
        'followers': user.followers_count,
        'description': user.description
    }
    return data


def get_user_timeline(user_id=''):
    api = tweepy.API(auth, proxy=get_random_proxy())
    public_tweets = api.user_timeline(user_id=user_id)
    lists = []
    try:
        for tweet in public_tweets:
            lists.append(tweet.text)
    except:
        pass
    return lists
