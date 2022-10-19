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

api = tweepy.API(auth)


def get_user_data(name=''):
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
    public_tweets = api.user_timeline(user_id=user_id)
    lists = []
    for tweet in public_tweets:
        lists.append(tweet.text)
    return lists
