import csv
import time

import re

songs = open("catalog_all_unsorted_0.csv", "r")
what = open("1c.csv", "w")

for line in songs:
    if re.match("(.*)(W|w)hat(.*)", line):
        print >> what, line,



#this script uses regex, if you forget what it is go to your message at H&D slack tech-support channel -k



#this is the script i used in the end to scrape without output



songs = open("catalog_all_unsorted_8.csv", "r")


for line in songs:
    if re.match("(.*)(W|w)hat(.*)", line):
        print (" ", line)
