import os
import csv

#
csvpath = os.path.join('raw_data','budget_data_2.csv')

bank_data = []
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            bank_data.append(row)

number_months = int(len(bank_data))

total_revenue = 0
for item in bank_data:
    total_revenue+=int(item[1]) #'${:,.2f}'.format(money)

first_revenue = float(bank_data[0][1])
last_revenue = float(bank_data[number_months-1][1])
average_revenue = (last_revenue - first_revenue)/(number_months-1)

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
print("----------------------------")
print("Total Months: {}".format(number_months))
print("Total Revenue: ${}".format(total_revenue))
print("Average Revenue Change: ${}".format(average_revenue))
print("Greatest Increase in Revenue: {} $({})".format(max_date, max_increase))
print("Greatest Decrease in Revenue: {} $({})".format(min_date, min_increase))

# Set variable for output file
output_file = os.path.join("budget_data_analysis_2.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write rows
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months: {}".format(number_months)])
    writer.writerow(["Total Revenue: ${}".format(total_revenue)])
    writer.writerow(["Average Revenue Change: ${}".format(average_revenue)])
    writer.writerow(["Greatest Increase in Revenue: {} $({})".format(max_date, max_increase)])
    writer.writerow(["Greatest Decrease in Revenue: {} $({})".format(min_date, min_increase)])
