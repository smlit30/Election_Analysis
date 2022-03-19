# The data we need to retrieve
# The total number of votes cast
## The complete list of candidates who recieved votes
## The percentage of votes each candidate won
## The total number of votes cast for each candidate
## The winner of the election based on teh popular vote


##file_to_load = 'election_results.csv'

##with open(file_to_load) as election_data:
   ## print(election_data)


#add dpendencies
import csv
import os
#assign a variable to load a file from path
file_to_load = os.path.join("election_results.csv")
#Assign a variable to save teh file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0



#open teh election results and read the file
with open(file_to_load) as election_data:
    
    #to do : read and analyze the data here
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes)*100
    #deteremine winning count & candidate
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
 
winning_candidate_summary = (
     f"----------------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"----------------------------------\n")
print(winning_candidate_summary)
  
    #print(f"{candidate_name}: received {'%.1f'%vote_percentage}% of the vote.") 

#print(candidate_votes)
   

    
#Practice creating txt file
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
    