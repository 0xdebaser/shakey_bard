import os
from dotenv import load_dotenv
import tweepy

load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


def setup_client():
	client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
						   access_token_secret=access_token_secret, wait_on_rate_limit=True)
	return client


def setup_streaming_client():
	# streaming_client = tweepy.StreamingClient(bearer_token)
	# return streaming_client
	class ClapBack(tweepy.StreamingClient):

		def on_tweet(self, tweet):
			print(tweet)

	clap_back = ClapBack(bearer_token=bearer_token)
	clap_back.add_rules(tweepy.StreamRule("@shakeybard"))
	clap_back.filter()
	return clap_back
