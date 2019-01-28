import tweepy
import time

print("This is my twitter bot")

CONSUMER_KEY = "kOUDwjIGwYD5oq5JMTx0KxM04"
CONSUMER_SECRET = "hRrV3Sa2Cqo6dM3bzdzG5FFo1PUBUg2qT3YkwGycDwIN88euKm"
ACCESS_KEY = "1089652882381537280-1ZLrp7ah3VTYB6UtzkqL2ZnSmK4wwz"
ACCESS_SECRET = "hSUZQX8uG9KGEZvYOGoM8wbngWwVNukMnXiqYGhbSZ9kI"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()


idFile = 'lastseenid.txt'


def retrieveLastSeenId(idFile):
    f_read = open(idFile, mode='r')
    lastSeenId = int(f_read.read().strip())
    f_read.close()
    return lastSeenId

def storeLastSeenId(lastSeenId,idFile):
    f_write = open(idFile, mode='w')
    f_write.write(str(lastSeenId))
    f_write.close()
    return

def reply():
    print('retrieving and replying to tweets...', flush=True)
    lastSeenId = retrieveLastSeenId(idFile)
    mentions = api.mentions_timeline(lastSeenId, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        lastSeenId = mention.id
        storeLastSeenId(lastSeenId, idFile)
        if "#helloworld" in mention.full_text.lower():
            print("Found hello world", flush=True)
            print("Responding back...", flush=True)
            api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!!')


while True:
    reply()
    time.sleep(5)