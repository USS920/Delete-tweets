import tweepy
import datetime

consumer_key="IFFIRl234sFoIlvjs2dym7A2q"
consumer_secret="op3l0KEolTycpTO63bHphewrlZLuuReDzZ0p94jMq4QCh6Jz9C"
access_token="1403363039466819586-6wSIxYVZa4ngQFvTZZXOPLwS5dnWgl"
access_token_secret="p7KK1f6ka2pYuwQBlOeTHLrjqGITcyxrWGNolOcx326rq"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def writetweet(tweet_del):
    with open('deleted_tweet.txt', 'a') as f:
        f.write('\n\n'+tweet_del)

def delbykeyword(key):
    keyword = key
    print("Fetching First 200 tweets")
    tweets = api.user_timeline(count=200, tweet_mode='extended')

    while len(tweets) > 0:
        for tweet in tweets:
            full_text = tweet.full_text
            if keyword.upper() in full_text.upper():
                api.destroy_status(tweet.id)
                writetweet(full_text)
                print("Deleted tweet with ID:", tweet.id)
        max_id = tweets[-1].id - 1
        print("Fetching Next 200 tweets")
        tweets = api.user_timeline(count=200, max_id=max_id, tweet_mode='extended')
def delbydate(date,month,year):
    threshold_date = datetime.datetime(year, month, date, 0, 0, 0)
    print("Fetching First 200 tweets")
    tweets = api.user_timeline(count=200)
    while len(tweets) > 0:
        for tweet in tweets:
            tweet_date = datetime.datetime.strptime(tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            if tweet_date < threshold_date:
                api.destroy_status(tweet.id)
                writetweet(tweet.text)
                print("Deleted tweet with ID:", tweet.id)
        max_id = tweets[-1].id - 1
        tweets = api.user_timeline(count=200, max_id=max_id)

#All tweets contaning GoodMorning will be deleted.
delbykeyword("GoodMorning")
#delbydate has a format (d,m,yyyy) in the below, it will delete all tweet before 01st March 2021.
#If you want to delete only by date, comment the delbykeyword("GoodMorning") line.
delbydate(1,3,2021)
