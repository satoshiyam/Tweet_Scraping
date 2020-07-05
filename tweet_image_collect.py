import tweepy
import sys
sys.path.append("..")
import info


API_KEY = info.KEY_INFO.API_KEY
API_SECRET_KEY = info.KEY_INFO.API_SECRET_KEY
BEARER_TOKEN = info.KEY_INFO.BEARER_TOKEN
ACCESS_TOKEN = info.KEY_INFO.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = info.KEY_INFO.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
result = tweepy.Cursor(api.user_timeline,id="yS_uecsecond").items(10)
i = 0
for tweet in result:
    print("{} : ".format(i)+str(tweet.entities))
    i = i+1
