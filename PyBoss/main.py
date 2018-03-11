import os
import csv

us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

csvpath = os.path.join('raw_data','employee_data1.csv')

employee_data = []
with open(csvpath, 'r', newline ='', encoding="utf-8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None) # skip file header

        for row in csvReader:
            employee_data.append(row)

#Create a list per element
lst_firstname =[]
lst_lastname = []
lst_DOB = []
lst_SSN = []
lst_State = []
#for i in range(1):
for item in employee_data:
    fullname = item[1]
    # split method breaks up a string at the specified separator and returns a list of strings
    # strip method removes leading and trailing characters
    firstname =fullname.strip().split(' ')[0]
    lastname = ' '.join((fullname + ' ').split(' ')[1:]).strip()
    DOB = str(item[2][8:]) + "/" + str(item[2][5:7]) + "/" + str(item[2][0:4])
    SSN = "***-**" + str(item[3][-5:])
    for key, value in us_state_abbrev.items():
        if item[4] == key:
            State = value
    lst_firstname.append(firstname)
    lst_lastname.append(lastname)
    lst_DOB.append(DOB)
    lst_SSN.append(SSN)
    lst_State.append(State)

# Zip lists
cleaned_employee_list = zip(lst_firstname, lst_lastname, lst_DOB, lst_SSN, lst_State)

# Set variable for output file
output_file = os.path.join("employee_data1_cleaned.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID, First Name, Last Name, DOB, SSN, State"])

    # Write in zipped rows
    writer.writerows(cleaned_employee_list)
