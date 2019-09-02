# Import Modules
import os
import csv

#Open CSV

budgetfile = "Resources/budget_data.csv"
budgetfile_output = open("budgetfile_summary.txt","w")


# variables  
total_months = 0
total_revenue = 0
prev_monthrev = 0
current_revchange = 0
revchange_list = []
month_change = []
gincrease = ["", 0]
gdecrease = ["", 9999999999]

# Read and skip header

with open(budgetfile, newline='') as csv_file:
    read_file = csv.reader(csv_file)
    header = next(read_file)
    reader = csv.DictReader(csv_file)

# Loop and calculate

    for row in read_file:

                # total number of months reviewed and revenue
                total_months = total_months + 1
                total_revenue = total_revenue + int(row[1])
                
                # revenue changes
                currentrev_change = int(row[1]) - prev_monthrev
                prev_monthrev = int(row[-1])
                month_change = [row[1]]
                revchange_list = revchange_list + [current_revchange]

                # largest increase, decrease and avg change
if (current_revchange > gincrease[1]):
                gincrease[0] = row[0]
                gincrease[1] = current_revchange

                
if (current_revchange < gdecrease[1]):
                gdecrease[0] = row[0]
                gdecrease[1] = current_revchange

                revaverage = sum(revchange_list)/len(revchange_list)

      
 



print(f"    Financial Analysis      \n")
print(f"----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total:    ${total_revenue}\n"  )
print(f"Average Change: ${current_revchange}\n")
print(f"Greatest Increase in Profits: {gincrease[0]} ${gincrease[1]}\n") 
print(f"Greatest Decrease in Losses: {gdecrease[0]} ${gdecrease[1]}\n")
        

