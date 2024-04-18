import os
import csv

# Setting the path for the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as budget:
    rdr = csv.reader(budget, delimiter=",")
    hdr = next(rdr)
    
    # Initializing variables
    month_count = 0
    profit = 0
    loss = 0
    pl_list = [] # List to store profit/loss values (row 1 in data)

    maxincrease_amount = ["", 9999999] # setting it to 9999999 because that's a big number I don't think the data has
    maxdecrease_amount = ["", 0] 
        
    # Loop through the budget data
    for row in rdr:
        # Calculate month count, which is the row count for the data, not counting header
        month_count += 1 #is the same as month_count = month_count + 1

        # Extract amount from the row and convert it to float
        amount = float(row[1])

        # Check if amount is positive (profit) or negative (loss)
        if amount > 0:
            profit += amount 
        elif amount < 0:
            loss += abs(amount) #calculating with absolute value allows us to ignore the 
                                #negative sign to sum it up
        total = int(profit - loss)
        
        # Append amount to the empty profit/loss list
        pl_list.append(amount)

    # Calculate average change ----------------------------------------------------------
    revenue_change_list = [pl_list[i] - pl_list[i-1] for i in range(1, len(pl_list))]
    average_change = sum(revenue_change_list) / len(revenue_change_list)
        #so from 1 to the length of pl_list, were finding the change in profit/loss (aka revenue) 
        #between the first value of that row to the next one in pl_list, then finding the average
        #of it in line 40

    # Calucating the greatest inc and greatest dec
    greatest_inc = int(max(revenue_change_list))
    greatest_dec = int(min(revenue_change_list))

    # Printing the results ----------------------------------------------------------
    print(f"Total Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_inc}")
    print(f"Greatest Decrease in Profits: {greatest_dec}")
    print("\nThe results has been written to the analysis.txt file.")

# Writing results on text file ----------------------------------------------------------

# Open a file in write mode ('w')
with open('analysis.txt', 'w') as file:
    # Write some text into the file
    file.write("Financial Analysis\n----------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec}")