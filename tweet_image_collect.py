import tweepy
import sys
sys.path.append("..")
import info
from urllib import request

# 別ファイルからキー取得
API_KEY = info.KEY_INFO.API_KEY
API_SECRET_KEY = info.KEY_INFO.API_SECRET_KEY
BEARER_TOKEN = info.KEY_INFO.BEARER_TOKEN
ACCESS_TOKEN = info.KEY_INFO.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = info.KEY_INFO.ACCESS_TOKEN_SECRET

# tweepyのインスタンス化
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# tweet取得
get_tweet_num = 100
ID_name = ["ecoyuri"]
result = tweepy.Cursor(api.user_timeline,id=ID_name[0]).items(get_tweet_num)

i = 0
for tweet in result:
    # 確認
    # print("{} : ".format(i)+str(tweet.entities))
    # print(len(tweet.entities))
    # i = i+1
    # entitiesの要素が4以上→画像がある？→要検討
    if (len(tweet.entities) > 4):
        filename = "{:0=4}".format(i) 
        # 保存→複数ユーザにするなら命名規則は要変更
        request.urlretrieve(tweet.entities["media"][0]["media_url_https"], "./image/"+filename+".jpg")
        i = i+1

    # 追加したい機能：ツイート内容も同じファイル名.txtで保存したい
    # tweet.entities["media"][0]が確認できない