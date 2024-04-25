"""
    This is a python program to pick content
    containing given keyword(s)
"""

import csv

keywords = [
#enter your key words here
]
results = []
file_zhan=[]
n = 2; #set row here

# enter your input filename here
with open('infile.csv') as f:
    spamreader = csv.reader(f, delimiter=',')
    for row in spamreader:
        file_zhan.append(row[n]) 

for line in file_zhan:
    for keyword in keywords:
        if keyword in line:
            results.append([line])
            break

a=results

# enter your output filename here
f = open('outfile', 'w')

writer = csv.writer(f)

for row in a:
    writer.writerow(row)

f.close()
