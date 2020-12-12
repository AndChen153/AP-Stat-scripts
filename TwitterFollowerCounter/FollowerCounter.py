#https://www.geeksforgeeks.org/python-status-object-in-tweepy/
#1-9-90 rule
import tweepy

class TwitterClient(object): 

    def __init__(self):
        CONSUMER_KEY = "lorYCyfLdolyZcBd3L1YvGI4b"
        CONSUMER_SECRET_KEY = "onCURThXUu4Nh3LsVreji43z3yB2DRIk3ZX09nDdfAzk4VzdYk"
        ACCESS_TOKEN = "764173298032717825-HR6jsuRav5UnCrXxjFgj6YhsHb51x8i"
        ACCESS_TOKEN_SECRET = "fIhDmUXC0vMbkUGCrTVgzgk0gKmygXSSNqYlSIfAjuj8Q"
        try:
            self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
            self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

            self.api = tweepy.API(self.auth)
        except:
            print("Authentication Failed")

    def tweetSearch(self, hashtag):
        tweets = self.api.search(q=hashtag, 
                    lang="en")
        return tweets
    
    def tweetSearch30(self, hashtag, date):
        #date in format yyyyMMddHHmm
        tweets = self.api.search_30_day(environment_name = "development1", query=hashtag, toDate = date)
        return tweets

    def getUser(self, tweet):
        userList = []
        if tweet.user.location != None:
            if "Memphis" in tweet.user.location:
                return(tweet.user.screen_name, tweet.user.followers_count)

search = TwitterClient()


date = 202011300000
tweets30 = []
'''"Grizz", "#elvis", "#graceland", "#ilovememphis", 
         "memphistennessee", "#901", "#choose901", "#memphisgrizzlies"'''

for i in ("#memphis", "memphis", "Tennessee", "TN"):
    tweetsList = search.tweetSearch30(i, date)
    tweets30 += tweetsList

for i in tweets30:
    if search.getUser(i) != None:
        print(search.getUser(i)[0], search.getUser(i)[1])
print(len(tweets30))

