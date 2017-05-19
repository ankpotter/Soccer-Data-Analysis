import numpy as np
import matplotlib.pyplot as plt
import pygal
import lxml

data = [] 
f = open('LeagueTransfers.csv')
for i in f:
    row = i.split(',')
    if(len(row) > 4):
        del row[2]
    data.append(row)
data_size = len(data) - 1
for i in range(0,data_size):
    if(len(data[i]) != 4):
        print(i)
indices = []
for i in range(1,data_size):
	if(data[i][2] == ""):
		indices.append(i)

indices.sort(reverse=True)

for i in indices:
	del data[i]
 
row_names = data[0]
del data[0]

season = set()
for i in data:
    season.add(i[3])

league = set()
for i in data:
	league.add(i[0])

seasons = list(season)
leagues = list(league)
leagues.sort()
seasons.sort()

print(seasons)

player_league = []
player_league_wise = []

for i in leagues:
	player_league = [x for x in data if x[0] == i]
	player_league_wise.append(player_league)
	player_league = []

player_season = []
player_season_wise = []

for i in seasons:
	player_season = [x for x in data if x[3] == i]
	player_season_wise.append(player_season)
	player_season = []

#transfer_matrix = np.zeros((11,11),np.int)
transfer_matrix = [[0]*11 for _ in range(11)]

i=0
while(i<data_size):
	curr_league = data[i][0]
	curr_team = data[i][1]
	curr_player = data[i][2]
	curr_league_index = leagues.index(curr_league)
	while((i<data_size) & (data[i][0] == curr_league) & (data[i][1]==curr_team) & (data[i][2] == curr_player)):
		i = i + 1
		if(i == data_size):
			break
	if(i >= data_size):
		break
	elif(data[i][2] != curr_player):
		continue				
	elif(data[i][0] != curr_league):
		transfer_matrix[curr_league_index][leagues.index(data[i][0])] += 1
	elif(data[i][1] != curr_team):
		transfer_matrix[curr_league_index][curr_league_index] += 1
	else:
		print("You are screwed !")	

total_transfer = []
percent_transfer = []
for i in range(0,len(transfer_matrix)):
    total_transfer.append(sum(transfer_matrix[i]))
    percent_transfer.append([transfer_matrix[i][i]/total_transfer[i],leagues[i]])

percent_transfer.sort(key = lambda x:x[0],reverse = True)
line_chart0 = pygal.HorizontalBar()
line_chart0.title = 'Transfer Within League (% of Total)'
for i in percent_transfer:
    line_chart0.add(i[1],i[0])
line_chart0.render_to_file('line_chart0.svg')    


league_within = []
j = 0

for i in range(0,len(transfer_matrix)):
    league_within.append([transfer_matrix[i][i],leagues[i]])
    transfer_matrix[i][i]= 0

league_within.sort(key = lambda x:x[0],reverse = True)

line_chart = pygal.HorizontalBar()
line_chart.title = 'Transfer Within League (total)'
for i in league_within:
    line_chart.add(i[1],i[0])
line_chart.render_to_file('line_chart.svg')    
    
dot = pygal.Dot(x_label_rotation= 30,show_legend = False)
dot.title = 'Transfer Trends'
dot.x_labels = leagues

j = 0

for i in transfer_matrix:
    dot.add(leagues[j],i)
    j = j + 1
dot.render_to_file('dot.svg')
