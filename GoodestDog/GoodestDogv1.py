import tweepy
import openai
import schedule
import time
import tweepy.client
import random

API_KEY = 'API_KEY'
API_KEY_SECRET = 'SECRET_KEY'
ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
BEARER_TOKEN = 'BEARER_TOKEN'
openai.api_key = 'OPEN_API_KEY'

api = tweepy.Client(bearer_token=BEARER_TOKEN, 
                    consumer_key=API_KEY, 
                    consumer_secret=API_KEY_SECRET, 
                    access_token=ACCESS_TOKEN, 
                    access_token_secret=ACCESS_TOKEN_SECRET)

topic = ""

def get_first_feed():
    response = api.get_home_timeline(max_results=1)
    return response.data[0].id, response.data[0].text

def generate_chatgpt_content(topic):
    num = random.randint(1,10)
    if 1 <= num <= 6:
        print("Rolled Current event tweet")
        prompt=f"Craft a wholesome 140 char tweet from the lens of a religious, cockapoo dog regarding current events"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=50
        )
    elif 7 <= num <= 8:
        print("Rolled religious tweet")
        prompt=f"Craft a wholesome 140 char religious tweet from a cockapoo dog directly quoting an uplifting bible passage"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=50
        )
    elif num == 9:
        print("Rolled religious tweet")
        prompt=f"Craft a wholesome 140 char religious tweet from a cockapoo dog in support of the homeless"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=50
        )
    else:
        print("Rolled inspiring message")
        prompt=f"Craft a 140 char tweet with a short inspiring message from a cockapoo dog"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=50
        )
    print(response.choices[0])
    sample = response.choices[0].message.content.strip()
    sample = sample.strip('\"')
    return sample

def post_tweet():
    tweet_content = generate_chatgpt_content(topic)
    print(f"Posting tweet: {tweet_content}")
    api.create_tweet(text=tweet_content)

schedule.every(2).hours.do(post_tweet)

if __name__ == "__main__":
    '''
    print("Posting Kickoff Tweet")
    post_tweet()
    print("Bot is running and posting tweets periodically...")
    while True:
        schedule.run_pending()
        time.sleep(7200)
    '''
    print("testing retreival")
    id, text = get_first_feed()
    print(id, text)