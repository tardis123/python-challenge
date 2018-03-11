# Dependencies
import os
import csv

#Ask which file should be analyzed (file must be in csv format)
input_file = input("Enter the name of the file you want to analyze (without extension, must be csv file) : ") + ".csv"

# Set file path (input file should be located on the same level as the folder raw_data)
csvpath = os.path.join('raw_data', input_file)

# Append file lines to list poll_data
poll_data = []
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            poll_data.append(row)

# Calculate total number of votes
total_votes = int(len(poll_data))
print(poll_data[0])

#print(poll_data[3]) #grab 4th row in the csv file (header not included)
#print(poll_data[3][2]) #grab value in the 3th column for the 4th row (header not included)

# Append candidate name plus total votes per candidate to dictionary candidates
candidates = {}
for i in range(total_votes):
    key = poll_data[i][2]
    if key not in candidates:
        candidates[key] = 1
    else:
        candidates[key] += 1

#Print output to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: {}".format(total_votes))
print("-------------------------")
relative_votes = 0
top_vote = 0
winner = ""
for key, value in candidates.items():
    relative_votes = "{:.2%}".format(float(value/total_votes))
    print("{}: {} ({})".format(key, relative_votes, value))
    if value > top_vote:
        top_vote = value
        winner = key
print("-------------------------")
print("Winner: {}".format(winner) )
print("-------------------------")

# Set variable for output file
output_file = os.path.join("election_results.csv")

#  Print output to file
# 1) Ask what the output file should be named liked (must be csv format)
output_file = input("Enter the name for the output file (without extension): ") + ".csv"
# 2) set variable for output file
output_file = os.path.join(output_file)
#  3) Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow(["Total Votes: {}".format(total_votes)])
    writer.writerow(["-------------------------"])
    relative_votes = 0
    top_vote = 0
    for key, value in candidates.items():
        relative_votes = "{:.2%}".format(float(value/total_votes))
        writer.writerow(["{}: {} ({})".format(key, relative_votes, value)])
    writer.writerow([""])
    writer.writerow(["-------------------------"])
    writer.writerow(["Winner: {}".format(winner)])
    writer.writerow(["-------------------------"])
