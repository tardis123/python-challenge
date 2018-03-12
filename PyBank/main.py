# Dependencies
import os
import csv

#Ask which file should be analyzed (file must be in csv format)
input_file = input("Enter the name of the file you want to analyze (without extension, must be csv file) : ") + ".csv"

# Set file path (input file should be located on the same level as the folder raw_data)
csvpath = os.path.join('raw_data', input_file)

# Append file lines to list bank_data
bank_data = []
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            bank_data.append(row)

# Calculate number of months
number_months = int(len(bank_data))

# Calculate total revenue
total_revenue = 0
for item in bank_data:
    total_revenue+=int(item[1]) #'${:,.2f}'.format(money)

# Calculate average revenue change per month:
# (revenue in last month - revenue in first month)/(number of months -1)
# Round to a zero digit number

first_revenue = float(bank_data[0][1])
last_revenue = float(bank_data[number_months-1][1])
average_revenue = round((last_revenue - first_revenue)/(number_months-1))

# Retrieve greatest revenue increase and decrease plus corresponding month
min_increase = 0
max_increase = 0
min_date = ""
max_date = ""
j=0
for i in range(number_months):
    if i+1 < number_months:
        if int(bank_data[i+1][1]) - int(bank_data[i][1]) > max_increase:
            max_increase = int(bank_data[i+1][1]) - int(bank_data[i][1])
            max_date = bank_data[i+1][0]
        elif int(bank_data[i+1][1]) - int(bank_data[i][1]) < min_increase:
            min_increase = int(bank_data[i+1][1]) - int(bank_data[i][1])
            min_date = bank_data[i+1][0]

#Print output to terminal
print("Financial Analysis")
print("-" * 28)
print("Total Months: {}".format(number_months))
print("Total Revenue: ${}".format(total_revenue))
print("Average Revenue Change: ${}".format(average_revenue))
print("Greatest Increase in Revenue: {} $({})".format(max_date, max_increase))
print("Greatest Decrease in Revenue: {} $({})".format(min_date, min_increase))

# Print output to file
# 1) Ask what the output file should be named liked (must be csv format)
output_file = input("Enter the name for the output file (without extension): ") + ".csv"
# 2) set variable for output file
output_file = os.path.join(output_file)
#  3) Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write rows
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-" * 28])
    writer.writerow(["Total Months: {}".format(number_months)])
    writer.writerow(["Total Revenue: ${}".format(total_revenue)])
    writer.writerow(["Average Revenue Change: ${}".format(average_revenue)])
    writer.writerow(["Greatest Increase in Revenue: {} $({})".format(max_date, max_increase)])
    writer.writerow(["Greatest Decrease in Revenue: {} $({})".format(min_date, min_increase)])
