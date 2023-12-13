"""
Database:
Name - Date of birth.

Available commands:
init - create a new database
add 'Name Date of Birth' - add 'Name Date of Birth'
read 'Name' - show data for 'Name'
readall - show the entire database
drop 'Name' - delete data by 'Name'
"""

################################################
# imports
################################################
import sys
import csv
import os

################################################
# constants
################################################
# Database file
file_name = '/tmp/databaseLuda.csv'
# Create a temporary file for recording
# new data for the "drop" command
temp_file_name = 'temp.csv'

################################################
# logic
################################################
# Get a list of command line arguments
arguments = sys.argv

if 'init' in arguments:
    data = [['Name', 'Birth date']]
    with open(file_name, 'w') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)
        # Write the data to the CSV file
        csv_writer.writerows(data)
    print(f'A new database was created in {file_name}')

elif 'readall' in arguments:
    with open(file_name, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        # Read and print each row from the CSV file
        for row in csv_reader:
            print(row)

elif 'add' in arguments:
    # New data row
    data = arguments[2: 4]
    # Open the file in append mode ('a')
    with open(file_name, 'a') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)
        # Write a new line to the end of the file
        csv_writer.writerow(data)
    print(f'A new line has been added to {file_name}')

elif 'drop' in arguments:
    # Row value to delete
    value_to_remove = arguments[2]
    with open(file_name, 'r') as file, open(temp_file_name, 'w') as temp_file:
        csv_reader = csv.reader(file)
        csv_writer = csv.writer(temp_file)
        # Rewriting a string, excluding those whose value is value_to_remove
        for row in csv_reader:
            # The element to be removed is assumed to be in the first column
            if row[0] != value_to_remove:
                csv_writer.writerow(row)
    # Replace the original file with a temporary one
    os.replace(temp_file_name, file_name)
    print(f'Rows with {value_to_remove} have been removed from {file_name}')

elif 'read' in arguments:
    # Value to search
    value_to_find = arguments[2]
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        # Going through the lines of the file
        for row in csv_reader:
            # The element to be read is assumed to be in the first column
            if row[0] == value_to_find:
                print(f'Row found: {row}')
                # Interrupt the loop because the required row was found
                break
        else:
            print(f'The row with {value_to_find} was not found in {file_name}')

else:
    print('Incorrect command')