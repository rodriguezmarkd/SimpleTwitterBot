import tweepy
import openai
import schedule
import time
import tweepy.client
import random
import warnings

warnings.filterwarnings("ignore", module="urllib3")
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

def get_first_feed():
    response = api.get_home_timeline(max_results=1)
    print("Tweet Piper is Responding to:")
    print(response.data[0].text)
    return response.data[0].id, response.data[0].text

def generate_chatgpt_content():
    reply = False
    id = 0
    num = random.randint(1,10)
    print(num)
    #num = 10
    if 1 <= num <= 5:
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
    elif 6 <= num <= 7:
        print("Rolled Bible Passage tweet")
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
    elif num == 8:
        print("Rolled Homeless Support Tweet")
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
    elif num == 9:
        print("Somebody is getting a response from PIEPUR")
        reply = True
        id, text = get_first_feed()
        prompt=f"Craft a wholesome 140 char response a religious cockapoo dog would give to the following tweet: {text}"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=100
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
    sample = response.choices[0].message.content.strip()
    sample = sample.strip('\"')
    return sample, reply, id

def post_tweet():
    tweet_content, reply, id = generate_chatgpt_content()
    print(f"Posting tweet: {tweet_content}")
    if reply == False:
        api.create_tweet(text=tweet_content)
    elif reply == True:
        api.create_tweet(in_reply_to_tweet_id=id,text=tweet_content)

schedule.every(2).hours.do(post_tweet)

if __name__ == "__main__":
    print("Posting Kickoff Tweet")
    post_tweet()
    print("Bot is running and posting tweets periodically...")
    while True:
        schedule.run_pending()
        time.sleep(7200)
