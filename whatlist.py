import csv
import time

search_string = "what"

with open('catalog.csv', 'rb') as f, open('whatlist.csv', 'wb') as g:
    reader = csv.DictReader(f)
    c1, c2, c3, *_ = reader.fieldnames

    writer = csv.DictWriter(g, fieldnames=(c1, c2))
    for row in reader:
        if row[c3] == search_string:
            writer.writerow({c1:row[c1], c2:row[c2]})