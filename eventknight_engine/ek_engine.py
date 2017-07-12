from channels import Group
# from .models import Event, User
import tweepy
import threading
import json

# Globals
# User Token
tw_access_token = "880132005291147265-g8pIqlL4mK7ibjFIBYiSZMZNRIhFl4d"
tw_access_token_secret = "3ibVdFJjkoi6IyGS8RZLbOr2Pkvs3zJGqtGnueEjyX1FO"

# APP Key
tw_consumer_key = "7AQXhWHC8OD7K1pN11OZ0W3in"
tw_consumer_secret = "UBHYFRWM8B728I2D7d6xKNiSvzDQjP87SJOFcNcOK7dJsVgZAb"

tw_str = None
auth = None
l = None


class RealTimeListener(tweepy.streaming.StreamListener):
    # def on_status(self, status):
    #     Group("live-1").send({
    #         "text": "[stream] --> " + status,
    #     })
    #     print('\nSTREAM --> ' + status.text)

    def on_data(self, data):
        # decoded = json.loads(data)
        # Group("live-1").send({
        #     data,
        # })
        print('>>>')
        print('>>>')
        print(data)
        print('<<<')
        print('<<<')

    def on_error(self, status_code):
        print('\nAPI ERROR CODE:' + status_code + '\nSTREAM DISCONNECTED.')
        tw_str.disconnect()
        return False


def get_timeline_tweets():
    global auth
    threading.Timer(120.0, get_timeline_tweets).start()
    print('\n<timeline_block> | 2min sliding window')
    rest_api = tweepy.API(auth)
    timeline_tweets = rest_api.home_timeline()

    api_stat = rest_api.rate_limit_status()
    print(api_stat['resources']['statuses']['/statuses/home_timeline'])
    print(api_stat['resources']['users']['/users/lookup'])

    for tweet in timeline_tweets:
        if "polytest1" not in tweet.text:
            continue
        print('>>>')
        print('>>>')
        print(tweet)
        print('<<<')
        print('<<<')
    print('<end_of_timeline>')


def get_search():
    global auth
    api = tweepy.API(auth)

    query = '@shanith32dll'
    max_tweets = 50

    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            searched_tweets.extend(new_tweets)
            last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # depending on TweepError.code, one may want to retry or wait
            # to keep things simple, we will give up on an error
            break
    print(searched_tweets)
    for tweet in searched_tweets:
        print(tweet.text)
        Group("live-1").send({
            "text": "[stream] --> " + tweet.text,
        })


def fire_up():
    global auth, tw_str, l
    auth = tweepy.OAuthHandler(tw_consumer_key, tw_consumer_secret)
    auth.set_access_token(tw_access_token, tw_access_token_secret)
    l = RealTimeListener()
    tw_str = tweepy.Stream(auth, l)
    tw_str.filter(track=['polygon_tech', 'polytest1', 'polytest2', 'polytest3'], async=True)
    # get_search()
    get_timeline_tweets()
