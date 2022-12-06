import os
from dotenv import load_dotenv
import tweepy
import bard

load_dotenv()
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

twitter_handle = "@shakeybard"


if __name__ == '__main__':

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
                           access_token_secret=access_token_secret, wait_on_rate_limit=True)
    another_client = tweepy.Client(bearer_token=bearer_token)
    response = another_client.get_user(username=twitter_handle[1:])
    own_id = response.data.id


    class ClapBack(tweepy.StreamingClient):

        def on_tweet(self, tweet):
            original_text = tweet.text
            original_tweet_id = tweet.id
            author_id = tweet.author_id

            print(f"Author Id: {author_id}\nOriginal Tweet Id: {tweet.id}")

            # this guard clause prevents an infinite loop if the bot's twitter handle
            # is not stripped out of the original tweet and also keeps it from replying to
            # its own tweets
            if author_id != own_id:

                # strip out tag from string if it is the first part
                if original_text[0:len(twitter_handle)] == twitter_handle:
                    original_text = original_text[len(twitter_handle):].lstrip()

                reply_text = bard.shake_it(original_text).choices[0].text.lstrip()
                print(f"Reply_text: {reply_text}")

                client.follow_user(author_id)
                client.create_tweet(text=reply_text, in_reply_to_tweet_id=original_tweet_id)

            else:
                print("Potential infinite loop detected. Response aborted.")

    clap_back = ClapBack(bearer_token=bearer_token)
    clap_back.add_rules(tweepy.StreamRule("@shakeybard"))
    clap_back.filter(expansions=["author_id"])




