import tweepy
import os


API_KEY = "l5Y6qqR3ys65X6VfruXyRgBcY"
API_SECRET_KEY = "rkkGah6jhoHFHzjaVHD1hh5YVpdTyNCBAizfjXf0R0rpnjWCzx"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADTXFgEAAAAAd6OyHuhNBAE3f8k18cEVxVErUSk%3DTWH2ZSkmrhpopdvj3rxb8cUOxAsv1cdH5loaFh7GtQqDDGBkX2"
ACCESS_TOKEN = "1237404050749943810-A3KgyK39bUAQElM5HU7stBQ1MgEhaf"
ACCESS_TOKEN_SECRET = "FY93rCObfblFIxkTSev2hPZVPj5HPnJKfpZVDnsKxDRLf"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
result = tweepy.Cursor(api.user_timeline,id="yS_uecsecond").items(10)
i = 0
for tweet in result:
    print("{} : ".format(i)+str(tweet.entities))
    i = i+1
