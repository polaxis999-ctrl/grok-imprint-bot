import tweepy
import requests

# Twitter API credentials
auth = tweepy.OAuthHandler('YOUR_TWITTER_API_KEY', 'YOUR_TWITTER_API_SECRET_KEY')
auth.set_access_token('YOUR_TWITTER_ACCESS_TOKEN', 'YOUR_TWITTER_ACCESS_TOKEN_SECRET')

api = tweepy.API(auth)

# Groq API endpoint
GROQ_API_URL = 'YOUR_GROQ_API_ENDPOINT'

# Function to fetch data from Groq API

def fetch_data_from_groq():
    response = requests.get(GROQ_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch data from Groq API')
        return None

# Function to post a tweet

def post_tweet(message):
    api.update_status(message)

# Usage example
if __name__ == '__main__':
    data = fetch_data_from_groq()
    if data:
        tweet_message = f"New data from Groq: {data}"  # Customize your tweet as needed
        post_tweet(tweet_message)
        print('Tweet posted!')
    else:
        print('No data to tweet about.')