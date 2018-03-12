# paragraph 2 -> 10 sentences, word count 294,

import os
import csv
import re

#Ask which file should be analyzed (file must be in txt format)
input_file = input("Enter the name of the file you want to analyze (without extension, must be txt file) : ") + ".txt"

# Set file path (input file should be located on the same level as the folder raw_data)
txtpath = os.path.join('raw_data', input_file)

# Read file content into a text string
paragraph = ''
with open(txtpath, 'r', newline ='', encoding="utf-8") as txtFile:
    csvreader = csv.reader(txtFile)
    for line in txtFile:
        #line =line.replace('\n', '\s')
        paragraph += line
        #print(line)

#paragraph = re.sub("[\n,\r,\'\']",'',paragraph)
#Number of sentences
paragraph_sen = re.split("[.!?]", paragraph)
sentence_count = -1
for item in paragraph_sen:
    sentence_count +=1

#Number of words
word_count = len(paragraph.split())

#Number of characters
char_count=0
for word in paragraph.split():
    word = re.sub(r"[!?.,\"]",'',word)
    char_count +=len(word)

#Average letter counts
avg_letter_count = char_count/word_count

#Average sentence length
avg_sent_length = word_count/sentence_count

#Print output to terminal
print("Paragraph Analysis")
print("-" * 17)
print("Approximate Word Count: {}".format(word_count))
print("Approximate Sentence Count: {}".format(sentence_count))
print("Average Letter Count: {}".format(avg_letter_count))
print("Average Sentence Length: {}".format(avg_sent_length))

#  Print output to file
# 1) Ask what the output file should be named liked (must be csv format)
output_file = input("Enter the name for the output file (without extension): ") + ".txt"
# 2) set variable for output file
output_file = os.path.join(output_file)
#  3) Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Paragraph Analysis"])
    writer.writerow(["-" * 17])
    writer.writerow(["Approximate Word Count: {}".format(word_count)])
    writer.writerow(["Average Letter Count: {}".format(avg_letter_count)])
    writer.writerow(["Average Sentence Length: {}".format(avg_sent_length)])
