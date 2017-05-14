import markovify
import sys, os
import operator

with open(os.path.join(os.path.dirname(__file__), "markovify/test/texts/sherlock.txt")) as f:
    sherlock = f.read()
    sherlock_model = markovify.Text(sherlock)
    print(sherlock_model.make_sentence())