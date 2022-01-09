import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate Options and candidate votes
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""        
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
    
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Vote Percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        #Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        #winning candidate
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true set winning count = votes and winning percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        #Winning Candidate Summary
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

#Print the total votes
#print(candidate_votes)