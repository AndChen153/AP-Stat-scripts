# https://www.geeksforgeeks.org/python-status-object-in-tweepy/
# 1-9-90 rule
import tweepy
import time

class TwitterClient(object): 
    '''
    twitter class for finding tweets from memphis area and counting the follwer counts for unique accounts
    '''
    def __init__(self):
        # finding authentication keys from file to stay secure
        keyfile = open(r"C:\Users\Andrew Chen\Dropbox\code\TwitterKeys.txt", "r")
        keys = []
        for i in keyfile:
            keys.append(i)
        CONSUMER_KEY = keys[0][:-1]
        CONSUMER_SECRET_KEY = keys[1][:-1]
        ACCESS_TOKEN = keys[2][:-1]
        ACCESS_TOKEN_SECRET = keys[3]

        # create lists to hold found tweets
        self.tweetsList = []

        # attempt authentication
        try:
            self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
            self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            # twitter rate limit prevents over requests https://developer.twitter.com/en/docs/rate-limits
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        except:
            print("Authentication Failed")

    def tweetSearch(self, hashtag):
        '''
        search from most recent tweets
        q – The query to run against people search
        '''
        return self.api.search(q=hashtag, lang="en")
    
    def tweetSearch30(self, hashtag, date):
        '''
        search from the past 30 days, 100 maximum results
        chose not to use because date format is a pain to increment and twitter puts a limit on the number of searches per month
        '''
        # date in format yyyyMMddHHmm
        tweets = self.api.search_30_day(environment_name = "development1", query=hashtag, toDate = date)
        return tweets

    def getUser(self, tweet):
        '''
        checks if a tweet is from a person who has set their location to memphis
        '''
        # if there is no location, calling location returns a None value
        if tweet.user.location != None:
            if "Memphis" in tweet.user.location:
                return(tweet.user.screen_name, tweet.user.followers_count)

    def tweetWrite(self, hashtags):
        '''
        writes user id's and follower counts to separate text files
        '''
        noEntries = True

        # search for tweets
        for i in hashtags:
            tweetsList = self.tweetSearch(i)
            self.tweetsList += tweetsList
        
        for i in self.tweetsList:
            # checks user against previously collected usernames
            if self.getUser(i) != None:
                write = True
                readUsers = open("Usernames.txt", "r")
                for x in readUsers:
                    if str(self.getUser(i)[0]) in x:
                        write = False
                readUsers.close()
                
                # writes to separate files if value is unique
                if write:
                    noEntries = False
                    print(i.user.screen_name, i.user.followers_count)
                    writeUsers = open("Usernames.txt", "a")
                    writeUsers.write(str(self.getUser(i)[0]) + "\n")
                    writeUsers.close()
                    writeFollowers = open("FollowerCts.txt", "a")
                    writeFollowers.write(str(self.getUser(i)[1]) + "\n")
                    writeFollowers.close()
        if noEntries:
            print("no new entries")
                    

search = TwitterClient()
keywords = ["#memphis", "memphis", "Tennessee", "TN",
        "Grizz", "#elvis", "#graceland", "#ilovememphis", 
        "memphistennessee", "#901", "#choose901", "#memphisgrizzlies"]

while True:
    # check every 60 seconds
    print("SEARCHING...")
    search.tweetWrite(keywords)
    time.sleep(60)







