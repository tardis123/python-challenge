import os
import csv
import re

txtpath = os.path.join('raw_data','paragraph_2.txt')

paragraph = []
with open(txtpath, 'r', newline ='', encoding="utf-8") as txtFile:
        for line in txtFile:
            filtered = line.replace('\n', '')
        #readTXT = csv.reader(txtFile)
        for row in filtered:
            #paragraph+=str(row) #if you define paragraph as a string

            paragraph.append(filtered)

print(paragraph)
