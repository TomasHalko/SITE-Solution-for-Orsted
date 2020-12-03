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
csv_r = csv.reader(f, delimiter =';',quotechar =',',quoting=csv.QUOTE_MINIMAL)
csv_w = csv.writer(f, delimiter =';',quotechar =',',quoting=csv.QUOTE_MINIMAL)

# In this for loop Python is looping through Turbine.csv file's columns
# and storing them into relevant lists
for row in csv_r:
    dateAndTime.append(row[0])
    windDirection.append(row[1])
    windSpeed.append(row[2])
    theoreticalPower.append(row[3])
    activePower.append(row[4])
    error.append(row[5])
    service.append(row[6])
    faultMsg.append(row[7])
    statusText.append(row[8])

def powerDifference (row):
    tP = float(theoreticalPower[row].replace(',' , '.'))
    aP = float(activePower[row].replace(',' , '.'))
    return round(tP - aP, 2)


print("                                                            "       )
print("                         ---- MENU ----                     "       )   
print("   Please type in the number of the function you wish to perform"   )
print("                                                            "       )
print("         1. Calculate and add the Power Difference"                 )
print("         2. Plot the bar graph of Theoretical and Active Power"     )
print("         3. Sort the Wind Speed in descending order"                )
print("         4. Plot a graph of Wind Speed and Active Power"            )
print("         5. Update Status Test and Service requirement"             )
print("         6. Print the rows updated on the screen "                  )
print("         7. Print the Turbine data with Error > 3 and FaultMsg True")
print("         8. Delete data from Turbines with Error > 50"              )
print("                           9. Quit                          "       )

userChoice = input("> ")

if(userChoice) == "1":
    print("The power difference is: " + str(powerDifference(2)))

elif(userChoice) == "2":
    print("Option 2")

elif(userChoice) == "3":
    print("Option 3")

elif(userChoice) == "4":
    print("Option 4")

elif(userChoice) == "5":
    print("Option 5")
    
elif(userChoice) == "6":
    print("Option 6")

elif(userChoice) == "7":
    print("Option 7")

elif(userChoice) == "8":
    print("Option 8")

elif(userChoice) == "9":
    print("Option 9")

else: print("Please choose a number between 1 and 9")

f.close()

# Issues: Figure out a way to ignore index 0 of every list to not store headings in the csv file

# Further development: The data is stored now so we have the base to work with

#                      More development is needed with already parsed csv file 
#                      according to the requirements of the assignment

