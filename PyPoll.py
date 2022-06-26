# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each canditate won
# 4. the total number of cotes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
import datetime as dt
import os
# Use the now() attribbute on the datetime class to get the present time
now = dt.datetime.now()
# Print the present time
print("The time right now is ", now)


# Add our dependencies
import csv
import os
# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election analysis and write in the file
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file
    txt_file.write("Counties in the Election \n------------------------- \nArapahoe \nDenver \nJefferson")

#Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)
    print(headers)

    # print each row in the CSV file
    #for row in file_reader:
            #print(row)


#Using the open() function with the "w" mode we will write data to the file

# Open the election results and read the file
#with open(file_to_load) as election_data:
    #reader = csv.reader(election_data)
    #for row in reader:
        #print(row)

#  To do: perform analysis

# Close the file