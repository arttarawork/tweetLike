import markovify	#https://github.com/jsvine/markovify
import sys, os
import operator
import tweepy		#https://github.com/tweepy/tweepy
import csv

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

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



with open(os.path.join(os.path.dirname(__file__), "markovify/test/texts/sherlock.txt")) as f:
    sherlock = f.read()
    sherlock_model = markovify.Text(sherlock)
    print(sherlock_model.make_sentence())