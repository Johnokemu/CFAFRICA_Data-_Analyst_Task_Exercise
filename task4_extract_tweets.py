#FOR US TO DO TWITTER SENTIMENTAL ANALYSIS ON THE XENOPHOBIC ATTACKS IN SOUTH AFRICA.
# I AM USING THE HASHTAG #SAYNOTOXENOPHOBIA THAT WAS POPULAR IN TWITTER TO EXTRACT THE TWEETS AND SAVE THEM
# IN THE CSV FILE FOR ANALYSIS
# I WILL BE USING THE tweepy api and NLTK textblob later in the analysis

import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'PGcqQvuRuyCWqkUclwrvD0DE3'
consumer_secret = 'TpiVPqi5vgfjEfOMOIKdxJqkugwlVGLgnNN5H025jqDCDdvfLJ'
access_token = '1346194784-v1PiyvRnEiA1vstbysc23X2fzp23ezZLqm0ykJL'
access_token_secret = 'bzaJwGapJiC3hUdDij21qXuzMpv9Zu6BnZxQ5k0SZqmao'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('task4SayNoToXenophobia.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="##SayNoToXenophobia",count=100,
                           lang="en",
                           since="2019-08-03").items():
    print (tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
