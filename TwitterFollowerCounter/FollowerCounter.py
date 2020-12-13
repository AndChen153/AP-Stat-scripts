#https://www.geeksforgeeks.org/python-status-object-in-tweepy/
#1-9-90 rule
import tweepy
import time

class TwitterClient(object): 
    
    def __init__(self):
        keyfile = open(r"C:\Users\Andrew Chen\Dropbox\code\TwitterKeys.txt", "r")
        keys = []
        for i in keyfile:
            keys.append(i)
        CONSUMER_KEY = keys[0][:-1]
        CONSUMER_SECRET_KEY = keys[1][:-1]
        ACCESS_TOKEN = keys[2][:-1]
        ACCESS_TOKEN_SECRET = keys[3]
        self.tweetsList = []
        try:
            self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
            self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

            self.api = tweepy.API(self.auth)
        except:
            print("Authentication Failed")

    def tweetSearch(self, hashtag):
        return self.api.search(q=hashtag, 
                    lang="en")
    
    def tweetSearch30(self, hashtag, date):
        #date in format yyyyMMddHHmm
        tweets = self.api.search_30_day(environment_name = "development1", query=hashtag, toDate = date)
        return tweets

    def getUser(self, tweet):
        if tweet.user.location != None:
            if "Memphis" in tweet.user.location:
                return(tweet.user.screen_name, tweet.user.followers_count)

    def tweetWrite(self, hashtags):
        noEntries = True
        for i in hashtags:
            tweetsList = self.tweetSearch(i)
            self.tweetsList += tweetsList
        
        for i in self.tweetsList:
            if self.getUser(i) != None:
                write = True
                readUsers = open("Usernames.txt", "r")
                for x in readUsers:
                    if str(self.getUser(i)[0]) in x:
                        write = False
                readUsers.close()

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
keywords = ["#memphis", "memphis", "Tennessee", "TN"]

while True:
    print("SEARCHING... \n")
    search.tweetWrite(keywords)
    time.sleep(60)








for i in range(11): 
    date -= 10000

for i in range(17):
    date2 -= 10000

#print (date)



'''"Grizz", "#elvis", "#graceland", "#ilovememphis", 
         "memphistennessee", "#901", "#choose901", "#memphisgrizzlies"'''
