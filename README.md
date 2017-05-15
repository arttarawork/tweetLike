# tweetLike

A commandline tool to generate tweets like whatever twitter handle you want to imitate.

Scrapes the tweets of said twitter profile, uses Markov chains to generate familiar sounding tweet.

Built in python, powered by Markovify and Tweepy.

Project for COMP 3211 (Spring 2017 HKUST) by Artur Tarasenko and Drew Brost.

## System Details

This was run on Ubuntu 16.04 LTS and Python 2.7

Due to UTF-8 issues in Python on Windows, this would be better to run on UNIX-like systems.

## Installation

* Make sure you have Python 2.7 installed

* Create a set of [Twitter api keys](https://apps.twitter.com)

* Follow the [tweepy](https://github.com/tweepy/tweepy) installation requirements

* Follow the [markovify](https://github.com/jsvine/markovify) installation requirements

Then just run 

```
python runMe.py
```

## Resources used

[Python 2.7](https://www.python.org/downloads/)

[tweepy](https://github.com/tweepy/tweepy)

[markovify](https://github.com/jsvine/markovify)
