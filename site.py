# Main Python file

# Imported libraries
import csv

# Each individual turbine.csv data column stored in a coresponding list
dateAndTime = []
windDirection = []
windSpeed = []
theoreticalPower = []
activePower = []
error = []
service = []
faultMsg = []
statusText = []

# Parsing the csv file and switching the delimeter of the dataset provided
# from comma to semicolon in order to separate the data correctly
f = open("Turbine.csv")
csv_f = csv.reader(f,delimiter =';',quotechar =',',quoting=csv.QUOTE_MINIMAL)

# In this for loop Python is looping through Turbine.csv file's columns
# and storing them into relevant lists
for row in csv_f:
    dateAndTime.append(row[0])
    windDirection.append(row[1])
    windSpeed.append(row[2])
    theoreticalPower.append(row[3])
    activePower.append(row[4])
    error.append(row[5])
    service.append(row[6])
    faultMsg.append(row[7])
    statusText.append(row[8])

# The only way to test this so far is to print whatever data you want by 
# printing a coresponding list with index of a row the data you wish to print is stored
print (windDirection [1])
f.close()

# Issues: Figure out a way to ignore index 0 of every list to not store headings in the csv file

# Further development: The data is stored now so we have the base to work with

#                      More development is needed with already parsed csv file 
#                      according to the requirements of the assignment

