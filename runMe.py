# -*- coding: utf-8 -*-

import markovify	#https://github.com/jsvine/markovify
import sys, os
import operator
import tweepy		#https://github.com/tweepy/tweepy
import csv

# Twitter API authentication

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# if authenication isn't provided, it's prompted here

if ((not consumer_key) | (not consumer_secret) | (not access_key) | (not access_secret)):
	print "You will be prompted for your Twitter API details, but you can change the string value for them inside the runMe.py file.\nYou can find these settings at https://dev.twitter.com/apps\n"

if (not consumer_key):
	consumer_key = raw_input("Consumer Key: ")

if (not consumer_secret):
	consumer_secret = raw_input("Consumer Secret: ")

if (not access_key):
	access_key = raw_input("Access Key: ")

if (not access_secret):
	access_secret = raw_input("Access Secret: ")

#Authenticates

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

handle = raw_input("Twitter Username: ")

#Compiles tweets

total_tweets = []

next_tweets = api.user_timeline(screen_name = handle, count = 200)

total_tweets.extend(next_tweets)

while len(next_tweets) > 0:

	next_tweets = api.user_timeline(screen_name = handle, count = 200, max_id = total_tweets[-1].id - 1)

	total_tweets.extend(next_tweets)

#Generates string of corpus

corpus = ""

for tweet in total_tweets:
	corpus += (tweet.text + " ")

#Generates markov model of corpus

markov_model = markovify.Text(corpus)

#Prints sentence

print(markov_model.make_sentence())