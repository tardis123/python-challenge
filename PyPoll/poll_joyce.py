import os
import csv# Set path for file

csvpath = os.path.join('raw_data','election_data_1.csv')

voter_id = []
counties = []
candidates = []# Open the current elections csv

with open(csvpath, 'r', newline = '', encoding="utf-8") as csvfile:# CSV reader specifies delimiter and variable that holds contents

   csvreader = csv.reader(csvfile, delimiter=',') # Skipp headers
   next(csvreader) # Each row is read is in

   for row in csvreader:
       voter_id.append(row[0])
       counties.append(row[1])
       candidates.append(row[2])

print(len(candidates))
