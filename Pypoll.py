# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our Dependencies.
import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     #Read the header row.
     headers = next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
         # Add to the total vote count.
         total_votes += 1
         # Print the candidate name from each row
         candidate_name = row[2]
         # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
             # Add it to the list of candidates
             candidate_options.append(candidate_name)

             # Begin tracking that candidate's vote count
             candidate_votes[candidate_name] = 0
         # Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of a candidate 
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)