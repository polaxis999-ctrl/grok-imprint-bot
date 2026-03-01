import tweepy
import requests
import json

# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Function to post tweets
def post_tweet(content):
    twitter_api.update_status(content)

# groq API URL
GROQ_API_URL = 'https://api.groq.example.com/data'

# Fetch data from groq API
def fetch_data():
    response = requests.get(GROQ_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# System prompt emphasizing Detroit culture and Motown vibes
SYSTEM_PROMPT = "Bring the vibes of Detroit to life! Highlight the city's rich culture infused with the essence of Motown. Include examples of meme coins like DetroitRise and MotownMojo."

# Main bot logic
if __name__ == '__main__':
    data = fetch_data()
    if data:
        # Process the data and create content for tweeting
        content = SYSTEM_PROMPT + '\nHere are the latest updates on meme coins: ' + json.dumps(data)
        post_tweet(content)
        print('Tweet posted!')
    else:
        print('Failed to fetch data from groq API.')
