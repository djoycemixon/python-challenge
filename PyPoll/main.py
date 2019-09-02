import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
csvpath_output = open("csvpath_summary.txt","w")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # header row
    csvheader = next(csvreader)
    #print(f"csvheader: {csvheader}")

    # variables
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    winner = []

# loop needed
    for row in csvreader:

        candidate = row[2]
        if candidate == "Khan":
            khan_votes += 1
        elif candidate == "Correy":
            correy_votes += 1
        elif candidate == "Li":
            li_votes += 1
        elif candidate == "O'Tooley":
            otooley_votes += 1

    
    total_votes = khan_votes + correy_votes + li_votes + otooley_votes
    #print(total_votes)

    # percent of votes won
    khan_percent = "{:.2%}".format(khan_votes/total_votes)
    correy_percent = "{:.2%}".format(correy_votes/total_votes)
    li_percent = "{:.2%}".format(li_votes/total_votes)
    otooley_percent = "{:.2%}".format(otooley_votes/total_votes)
    total_percentages = {khan_percent + correy_percent + li_percent + otooley_percent}
    #print(total_percentages)
    
    # vote dictionary
    candidate_totals = {"Khan": khan_votes, "Correy": correy_votes, "Li": li_votes, "O'Tooley": otooley_votes}
    #print(candidate_totals)


    # winner
    winner_votes = max(candidate_totals.values())
    # print(winner_votes)

    # winner = [c for c, v in candidate_totals.items() if v == winner_votes]
    #print(winner, winner_votes)

    # print and export

    print(f"            Election Results            \n")
    print(f"----------------------------------------\n")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------------\n")
    print(f"Khan: {khan_percent} ({khan_votes})\n")
    print(f"Correy: {correy_percent} ({correy_votes})\n")
    print(f"Li: {li_percent} ({li_votes})\n")
    print(f"O'Tooley: {otooley_percent} ({otooley_votes})\n")
    print("----------------------------------------\n")
    print(f"Winner: {winner_votes}")

    