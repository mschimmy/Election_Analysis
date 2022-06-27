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
#now = dt.datetime.now()
# Print the present time
#print("The time right now is ", now)


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

# initialize a total vote counter
total_votes = 0

# initialize candidate options and candidate votes
candidate_options = []
# decalre an empty dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the CSV file
    for row in file_reader:
            # add to the total vote count
            total_votes += 1

            # print the candidate name from each row
            candidate_name = row[2]

            #if the candidate does not match any existing candidate
            if candidate_name not in candidate_options:
                # add it to the list of candidiates
                candidate_options.append(candidate_name)
                # begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0
            # add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

#print the candidate vote dictionary
#print(candidate_votes)

# print the total votes
#print(total_votes)

#determinet he percentage of cotes for each candidate by looping through the counts
# iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # to do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

# to do: print out the winning candidate, vote count, and percentage to terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)