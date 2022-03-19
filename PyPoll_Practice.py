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
    print(f"{candidate_name}: received {'%.1f'%vote_percentage}% of the vote.") 

#print(candidate_votes)
   

    
#Practice creating txt file
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
    