import os
import csv

csvpath = os.path.join('raw_data','election_data_1.csv')

voter_id = []
county = []
candidate = []
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

total_votes = int(len(candidate))
print(total_votes)
