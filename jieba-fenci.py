"""
   Chinese text segmentation and counting
   using jieba library
"""
import jieba
import jieba.analyse
from collections import Counter
import csv
import pandas as pd

#jieba-probability
counter = Counter()
content = ''

#enter your output filename here
with open('infile.csv') as f:
    spamreader = csv.reader(f, delimiter=',')
    for row in spamreader:
        content += row[0]
        
        # seg_list = jieba.cut(row[2], cut_all=False)
        # counter.update(seg_list)

a=jieba.analyse.extract_tags(content, topK=2000, allowPOS=(),withWeight=True)
print(a[0:3])

# store into output file
import csv

#enter your output filename here
f = open('outfile.csv', 'w')

writer = csv.writer(f)

for row in a:
    writer.writerow(row)

f.close()




