import csv
import time



import re

songs = open("catalog.csv", "r")
what = open("whatlist.csv", "w")

for line in songs:
    if re.match("(.*)(W|w)hat(.*)", line):
        print >> what, line,

-----second script

import csv

with open('final_what.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['artist'] == 'Britney Spears':
            print(row['title'] ,row ['artist'])
