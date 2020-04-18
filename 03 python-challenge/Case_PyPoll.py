import os
import csv

poll_info = os.path.join('PyPoll','Resources','election_data.csv')

candidates = []
vote_count = []
total_votes = 0

with open (poll_info) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)
    
    for row in csvreader:
        total_votes += 1
        candidates_col = (row[2])
    
        if candidates_col in candidates:
            candidates_index = candidates.index(candidates_col)
            vote_count[candidates_index] = vote_count[candidates_index] + 1
            
        else:
            candidates.append(candidates_col)
            vote_count.append(1)
            
percentage = []
max_vote = vote_count[0]
max_index = 0

for x in range(len(candidates)):
    vote_percentage = vote_count[x]/total_votes * 100
    percentage.append(vote_percentage)
    
    if vote_count[x] > max_vote:
        max_votes = vote_count[x]
        max_index = x
        
winner = candidates[max_index]

print('\nElection Results')
print('________________________________')
print(f'\nTotal Votes: {total_votes:,}')
print('________________________________')
for x in range(len(candidates)):
    print(f'\n{candidates[x]}: {percentage[x]:.2f}% ({vote_count[x]:,})')
print('________________________________')
print(f'\nWinner: {winner}')
print('________________________________')

file= open('Poll_Analysis.txt','w')
file.write('\nElection Results')
file.write('\n________________________________')
for x in range(len(candidates)):
    file.write(f'\n\n{candidates[x]}: {percentage[x]:.2f}% ({vote_count[x]:,})')
file.write('\n________________________________')
file.write(f'\n\nWinner: {winner}')
file.write('\n________________________________')
    
file.close()
