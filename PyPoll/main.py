import os
import csv

# Setting the path for the CSV file
csvpath = os.path.join("Resources", "election_data.csv")


with open(csvpath) as budget:
    rdr = csv.reader(budget, delimiter=",")
    hdr = next(rdr)

# Initializing variables
    total_votes = 0
    candidate_names = []
    candidate_count = {} #adding a dictionary to store the count values for each candidate
    
    for row in rdr:
    #Calculating total votes----------------------------------------------------------
        total_votes += 1

    #Calulating unique canidate names-------------------------------------------------
        candidate = row[2]
        if candidate not in candidate_names:
            candidate_names.append(candidate)

    #Calculating candidate count----------------------------------------------------------
        if candidate in candidate_count:
            candidate_count[candidate] += 1
        else:
            candidate_count[candidate] = 1

    #Calculating vote percentage ------------------------------------------------- 
        candidate_percentages = {} #to store percentages for each candidate
        for candidate, count in candidate_count.items():
            percentage = (count / total_votes) * 100
            candidate_percentages[candidate] = percentage
    
    
    # For prinitng, combine candidate names, counts, and percentages into a single output string
candidate_output = []
for candidate, count in candidate_count.items():
    percentage = candidate_percentages[candidate]
    candidate_output.append(f"{candidate}: {percentage:.3f}% ({count}) ")



# Join the list of candidate outputs into a single string with newline separators
candidate_output_str = "\n".join(candidate_output)

# Finding the winner ----------------------------------------------
   
# Initialize variables to store the largest count and the winner's name
largest_votes = 0
winner = ""

# Iterate over each candidate output
for candidate_info in candidate_output:
    # Split the candidate info to extract the count part
    count_part = candidate_info.split("(")[1].split(")")[0]
    count = int(count_part.replace(",", "")) 
    
    # Check if the current vote count is larger than the largest vote found so far
    if count > largest_votes:
        largest_votes = count
        winner = candidate_info
winner_name = winner.split(":")[0] # This will only allow us to print the name of winner

#Printing the Results  
print("Election Results \n------------------------------ \n")  
print(f"Total Votes: {total_votes} \n------------------------------ \n")
print(f"{candidate_output_str}\n------------------------------ \n")
print(f"Winner: {winner_name}\n------------------------------ \n ")

# Writing results on text file ----------------------------------------------------------

# Open a file in write mode ('w')
with open('analysis.txt', 'w') as file:
    # Write some text into the file
    file.write("Election Results \n------------------------------ \n")  
    file.write(f"Total Votes: {total_votes} \n------------------------------ \n")
    file.write(f"{candidate_output_str}\n------------------------------ \n")
    file.write(f"Winner: {winner_name}\n------------------------------ \n ")
