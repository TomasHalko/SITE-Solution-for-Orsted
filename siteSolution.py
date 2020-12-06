# Main Python File

# Imported libraries
import csv 
import os

# In order to append Power_Difference and sorted Wind_Speed the values are stored in corresponding lists
powerDifference = ["Power_Difference"]
windSpeed = []

# Variables used for checking if a different command was executed or not
commandOneExecuted = 0
commandTwoExecuted = 0
commandThreeExecuted = 0
commandFourExecuted = 0
commandFiveExecuted = 0
commandSixExecuted = 0
commandSevenExecuted = 0

# This function is called upon when appending the columns of Power_Difference and Wind_Speed into TurbineData.csv
# Reference: https://thispointer.com/python-add-a-column-to-an-existing-csv-file/
def add_column_in_csv(input_file, output_file, transform_row):
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, open(output_file, 'w', newline='') as write_obj:
                # Create a csv.reader object from the input file object
                csv_reader = csv.reader(read_obj, delimiter = ';')
                # Create a csv.writer object from the output file object
                csv_writer = csv.writer(write_obj, delimiter = ';')
                # Read each row of the input csv file as list
                for row in csv_reader:
                    # Pass the list / row in the transform function to add column text for this row
                    transform_row(row, csv_reader.line_num)
                    # Write the updated row / list to the output file
                    csv_writer.writerow(row)  

# After executing any command this fuction is called upon and prompts the user with 
# an option to choose and execute a different command or exit the script
def continueOrNot ():
    print("Would you like to execute a different command?")
    executeAgain = input("(Y for yes / N for no) > ")
    if executeAgain.upper() == "N":
        quit()
    elif executeAgain.upper() == "Y":
        pass
    else:
        print("Please type in only 'Y' or 'N'")
        continueOrNot()

# Defining the header and reader in order for Python to loop through the csv file
fi = open("TurbineData.csv", "r")
fieldnames = ["Date/Time","Active_Power", "Wind_Speed", "Theoretical_Power" ,"Wind Direction", "Error", "Service", "FaultMsg", "Status Text"]
reader = csv.DictReader(fi, delimiter = ";", fieldnames= fieldnames)
header = reader.fieldnames
a_line_after_header = next(reader)

# In this for loop Python is looping through every row of the csv file
# calculating the difference between Theoretical_Power and Active_Power
# and also reading the Wind_Speed values and storing all of them into corresponding lists
for line in reader:
    tP = float(line["Theoretical_Power"].replace(',' , '.'))
    aP = float(line["Active_Power"].replace(',' , '.'))
    calculatePD = aP - tP
    powerDifference.append(calculatePD)

    wS = float(line["Wind_Speed"].replace(',', '.'))
    windSpeed.append(wS)
fi.close()

# Two commands that are responsible for sorting the Wind_Speed
# and appending the header to the first index
windSpeedSorted = sorted(windSpeed, key = lambda x:float(x) , reverse = True)
windSpeedSorted.insert(0, "Wind_Speed descending")

# While loop that ensures that the script is running until the user decides to exit
while True:
    print("                *Csv file was succesfully parsed*")
    # Printing the menu
    print("                                                            "       )
    print("                         ---- MENU ----                     "       )   
    print("   Please type in the number of the command you wish to perform"   )
    print("                                                            "       )
    print("         1. Add the Power_Difference and sort the Wind_Speed"                 )
    print("         2. Plot the bar graph of Theoretical and Active Power"     )
    print("         3. Plot a graph of Wind Speed and Active Power"            )
    print("         4. Update Status Test and Service requirement"             )
    print("         5. Print the rows updated on the screen "                  )
    print("         6. Print the Turbine data with Error > 3 and FaultMsg True")
    print("         7. Delete data from Turbines with Error > 50"              )
    print("                           8. Quit                          "       )

    # Prompting the user for the input to know which command to execute
    userChoice = input("> ")

    # Executing the first command
    if(userChoice) == "1":
        if(commandOneExecuted) == 0:
            # Append the calculated power difference into the csv file
            add_column_in_csv('TurbineData.csv', 'Final.csv', lambda row, line_num: row.append(powerDifference[line_num - 1]))
            print("Power difference column added")

             # Append the sorted wind speed into the csv file
            add_column_in_csv('Final.csv', 'TurbineData.csv', lambda row, line_num: row.append(windSpeedSorted[line_num - 1]))
            os.remove("Final.csv")
            print("Wind speed sorted column added")

            commandOneExecuted += 1
            continueOrNot()
        else:
            print("This command was already executed")
            print("If you would like to append the csv file again run the script again and provide new unedited csv file")
            continueOrNot()

    # Executing the second command
    elif(userChoice) == "2":
        print("Bar graph of Theoretical and Active power")
        continueOrNot()

    # Executing the third command
    elif(userChoice) == "3":
        print("Graph of Wind speed and Active power")
        continueOrNot()

    # Executing the fourth command
    elif(userChoice) == "4":
        print("Status Test and Service requirement updated")
        continueOrNot()
    
    # Executing the fifth command
    elif(userChoice) == "5":
        print("Updated rows printed")
        continueOrNot()

    # Executing the sixth command    
    elif(userChoice) == "6":
        print("Error > 3 data")
        continueOrNot()

    # Executing the seventh command
    elif(userChoice) == "7":
        print("Data from turbines with Error > 50 deleted")
        continueOrNot()

    # Executing the eighth command
    elif(userChoice) == "8":
        print("Closing the script")
        quit()

    # Ensuring that the user only chooses a relevant option
    else:
        print("Please choose a number between 1 and 8")
        continueOrNot()
        




