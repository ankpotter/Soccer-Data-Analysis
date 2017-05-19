import csv
data = [] 
with open('transfer.csv','rb') as cfile:
	rows = csv.reader(cfile, delimiter=',',quotechar='|')
	for row in rows:
		data.append(row)

teams = []

for row in data:
	if(row[1] not in teams):
		teams.append(row[1])
	if(row[2] not in teams):
		teams.append(row[2])

with open('teams.csv', 'wb') as f:
    writer = csv.writer(f)
    for team in teams:
        writer.writerow([team])

data_new = []

with open('teams.csv','rb') as cfile:
	rows = csv.reader(cfile, delimiter=',',quotechar='|')
	for row in rows:
		data_new.append(row)

for i in range(len(data)):
	for j in range(len(data_new)):
		if(data[i][1] == data_new[j][0]):
			data[i].append(data_new[j][1])

for i in range(len(data)):
	for j in range(len(data_new)):
		if(data[i][2] == data_new[j][0]):
			data[i].append(data_new[j][1])			
