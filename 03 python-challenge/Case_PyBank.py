import os
import csv

budget_info = os.path.join('Pybank','Resources','budget_data.csv')

with open (budget_info) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader, None)
    
    profit = []
    period = []
    
    for rows in csvreader:
        profit.append(int(rows[1]))
        period.append(rows[0])
    
    revenue = []
    
    for x in range(1, len(profit)):
        revenue.append((int(profit[x])-int(profit[x-1])))

    revenue_avg = sum(revenue)  / len(revenue)
    
    total_months = len(period)
    
    greatest_increase = max(revenue)
    greatest_decrease = min(revenue)
    
print('\nFinancial Analysis')
print('______________________________________________________________')
print(f'\nTotal Months: {total_months}')
print(f'Total: ${sum(profit):,d}')
print(f'Average change: ${revenue_avg:,.2f}')
print(f'Greatest increase in profits: {period[revenue.index(max(revenue))+1]} ${greatest_increase:,}')
print(f'Greatest increase in profits: {period[revenue.index(min(revenue))+1]} ${greatest_decrease:,}')
    
file= open('Financial_Analysis.txt','w')
file.write('\nFinancial Analysis')
file.write('\n______________________________________________________________')
file.write(f'\n\nTotal Months: {total_months}')
file.write(f'\nTotal: ${sum(profit):,d}')
file.write(f'\nAverage change: ${revenue_avg:,.2f}')
file.write(f'\nGreatest increase in profits: {period[revenue.index(max(revenue))+1]} ${greatest_increase:,}')
file.write(f'\nGreatest increase in profits: {period[revenue.index(min(revenue))+1]} ${greatest_decrease:,}')
    
file.close()

    