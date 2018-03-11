import os
import csv

# Dictionary with official USA state abbrevations
us_state_abbrev = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
        'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT',
        'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI',
        'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME',
        'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
        'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
        'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
        'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
        'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
        'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
        'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
        'Wisconsin': 'WI', 'Wyoming': 'WY',
    }

#Ask which file should be analyzed (file must be in csv format)
input_file = input("Enter the name of the file you want to analyze (without extension, must be csv file) : ") + ".csv"

# Set file path (input file should be located on the same level as the folder raw_data)
csvpath = os.path.join('raw_data', input_file)

# Append file lines to list employee_data
employee_data = []
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            employee_data.append(row)

#Create a list per element (column)
lst_firstname =[]
lst_lastname = []
lst_DOB = []
lst_SSN = []
lst_State = []

# Convert each element to the required format
for item in employee_data:
    fullname = item[1]
    # split method breaks up a string at the specified separator and returns a list of strings
    # strip method removes leading and trailing characters
    firstname =fullname.strip().split(' ')[0]
    lastname = ' '.join((fullname + ' ').split(' ')[1:]).strip()
    DOB = str(item[2][8:]) + "/" + str(item[2][5:7]) + "/" + str(item[2][0:4])
    SSN = "***-**" + str(item[3][-5:])
    # Get corresponding USA state abbreviation from dictionary us_state_abbrev:
    for key, value in us_state_abbrev.items():
        if item[4] == key:
            State = value
    # Append converted data to corresponding list
    lst_firstname.append(firstname)
    lst_lastname.append(lastname)
    lst_DOB.append(DOB)
    lst_SSN.append(SSN)
    lst_State.append(State)

# Zip lists
cleaned_employee_list = zip(lst_firstname, lst_lastname, lst_DOB, lst_SSN, lst_State)

# Print output to file
# 1) Ask what the output file should be named liked (must be csv format)
output_file = input("Enter the name for the output file (without extension): ") + ".csv"
# 2) set variable for output file
output_file = os.path.join(output_file)
#  3) Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID, First Name, Last Name, DOB, SSN, State"])

    # Write in zipped rows
    writer.writerows(cleaned_employee_list)
