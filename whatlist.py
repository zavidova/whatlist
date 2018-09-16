import csv
import time



import re

songs = open("catalog.csv", "r")
what = open("whatlist.csv", "w")

for line in songs:
    if re.match("(.*)(W|w)hat(.*)", line):
        print >> what, line,
            

