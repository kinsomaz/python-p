#This program access specified twitter account and search for tweet about COVID19
import os
import tweepy as tw
import pandas as pd
consumer_key = 'yourkeyhere'
consumer_secrect = 'yourkeyhere'
access_token = 'yourkeyhere'
access_token_secret = 'yourkeyhere'

#defining the users account
akinlade = tw.AkinladeAbdulsamad(consumer_key , consumer_secret)
akinlade.set_access_token(access_token , access_token_secret)
api = tw.API(akinlade , wait_on_rate_limit = True)

#define the search terms and the date_since as variables
search_words = '#COVID19'
date_since = '2019-05-19'
new_search = search_words + ' -filter:retweets' 

#collecting tweet
tweets = tw.Cursor(api.search,
                                       q = new_words,
                                       lang = 'en',
                                       since = date_since).item(50)
print(tweets)
covidFile = open('Accessing COVID19 from Twitter.txt' , 'w')
covidFile.write([tweets])
covidFile.close()

#create list of tweets
[tweet.text for tweet in tweets ]

#Those tweeting and their location
users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
print(users_locs)

#creating a pandas Data frame a list of Tweet data
tweet_text = pd.Dataframe(data = users_locs,
                                                        columns = ['user' , 'location'])
print(tweet_text)
usersLocs = open('Users twitting about COVID19 location.txt' , 'w')
usersLocs.write(tweet_text)
usersLocs.close()

    













    
    
    

