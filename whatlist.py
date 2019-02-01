import csv
import time

import re

songs = open("1.csv", "r")
what = open("part_01.csv", "w")

for line in songs:
    if re.match("(.*)(W|w)hat(.*)", line):
        print >> what, line,

#this script uses regex, if you forget what it is go to your message at H&D slack tech-support channel -k
