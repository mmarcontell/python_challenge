import os
import csv

file_path = os.path.join("Resources", "budget_data.csv")
output_analysis = os.path.join("Analysis", "Final_Analysis.txt")

with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

#create empty lists to append as we read through the file
    date = []
    profit_loss = []

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

#create variables for total number of months and net profit
    total_month = len(date)

    net_profit = sum(profit_loss)

    change_list = []

#find the monthly change by subtracting the previous months profit loss from the current month's
    for i in range(1, len(profit_loss)):
        change_list.append(profit_loss[i]-profit_loss[i-1])

#use python functions to find mean, max, and min
    average_change = sum(change_list)/len(change_list)

    max_change = max(change_list)

#use index to figure out which month had the max/min values
    max_index = change_list.index(max_change)
    max_date = date[max_index+1]

    min_change = min(change_list)
    min_index = change_list.index(min_change)
    min_date = date[min_index+1]

    print((f'Financial Analysis\n --------------------------------\n Total Months: {total_month}\n Total: ${net_profit}\n Average Change: ${average_change}\n Greatest Increase in Profits: {max_date} ${max_change}\n Greatest Decrease in Profits: {min_date} ${min_change}')
)

with open(output_analysis, 'w', newline = '') as txt:
    txt.write(f'Financial Analysis\n --------------------------------\n Total Months: {total_month}\n Total: ${net_profit}\n Average Change: ${average_change}\n Greatest Increase in Profits: {max_date} ${max_change}\n Greatest Decrease in Profits: {min_date} ${min_change}')
