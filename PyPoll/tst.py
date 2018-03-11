import os
import csv

csvpath = os.path.join('raw_data','election_data_1.csv')

poll_data = []
i=0
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            poll_data.append(row)
            i += 1

total_votes = int(len(poll_data))
print(i)
#print(poll_data[0])

#List of candidates who received total_votes
#Pythonic would be to use set:
#s = set()
#for item in poll_data:
#    s.add(item[2])
#print(s)

#print(poll_data[3]) #grab 4th row in the csv file (header not included)
#print(poll_data[3][2]) #grab value in the 3th column for the 4th row (header not included)

candidates = {}
for i in range(total_votes):
    key = poll_data[i][2]
    if key not in candidates:
        candidates[key] = 1
    else:
        candidates[key] += 1

print(candidates)
