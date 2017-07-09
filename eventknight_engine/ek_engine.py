from ws4py.client.threadedclient import WebSocketClient
import tweepy
import threading
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


class Socket(WebSocketClient):
    def opened(self):
        print('connected')

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print(m)
        if len(m) == 175:
            self.close(reason='Bye bye')


# Globals
tw_access_token = "880132005291147265-g8pIqlL4mK7ibjFIBYiSZMZNRIhFl4d"
tw_access_token_secret = "3ibVdFJjkoi6IyGS8RZLbOr2Pkvs3zJGqtGnueEjyX1FO"
tw_consumer_key = "7AQXhWHC8OD7K1pN11OZ0W3in"
tw_consumer_secret = "UBHYFRWM8B728I2D7d6xKNiSvzDQjP87SJOFcNcOK7dJsVgZAb"

tw_str = None
auth = None
l = None


class RealTimeListener(StreamListener):
    def on_status(self, status):
        global ws
        print('\nSTREAM --> ' + status.text)
        ws.send(status.text)

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
        print(tweet.text)
    print('<end_of_timeline>')


def open_socket():
    global ws


def fire_up_ek_engine():
    global auth, tw_str, l
    auth = OAuthHandler(tw_consumer_key, tw_consumer_secret)
    auth.set_access_token(tw_access_token, tw_access_token_secret)
    l = RealTimeListener()
    tw_str = Stream(auth, l)
    tw_str.filter(track=['polygon_tech', 'polytest1', 'polytest2', 'polytest3'], async=True)
    # get_timeline_tweets()

# fire_up_ek_engine()
# ws = Socket('ws://localhost:8000/live/1')
# ws.connect()
# ws.run_forever()
