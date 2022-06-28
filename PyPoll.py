# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each canditate won
# 4. the total number of cotes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os
# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initialize a total vote counter
total_votes = 0
# initialize candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

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
            #if the candidate does not match any existing candidate, add to the candidate list
            if candidate_name not in candidate_options:
                # add it to the list of candidiates
                candidate_options.append(candidate_name)
                # and begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0
            # add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

# save the results to our text file
with open(file_to_save, "w") as txt_file:
    # after opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save the final vote count to the text file
    txt_file.write(election_results)
    #determinet the percentage of cotes for each candidate by looping through the counts
    # iterate through the candidate list
    for candidate_name in candidate_votes:
        # retrieve vote count and percentage of votes of a candidate
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # print each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print each candidate's vote count and percentage to the terminal  
        print(candidate_results)
        # save the candidate results to our text file
        txt_file.write(candidate_results)
        #determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # print the winning candidate, vote count, and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)