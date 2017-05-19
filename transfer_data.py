from bs4 import BeautifulSoup
import urllib
import csv 

l = []
r = urllib.urlopen('http://www.soccernews.com/soccer-transfers/')
j = 0
soup = BeautifulSoup(r,"html.parser")
link = soup.findAll('a')
link =  link[69:119]
for i in link:
	l.append(i.get('href'))

l.append('http://www.soccernews.com/soccer-transfers/english-premier-league-transfers/')
l.append('http://www.soccernews.com/soccer-transfers/spanish-la-liga-transfers/')
l.append('http://www.soccernews.com/soccer-transfers/italian-serie-a-transfers/')
l.append('http://www.soccernews.com/soccer-transfers/german-bundesliga-transfers/')
l.append('http://www.soccernews.com/soccer-transfers/rest-of-europe-transfers/')
uls =[]
li_final_to = []
li_final_from = []
li_final_p = []
l = [x for x in l if len(x) >5]

for trans in l:
	read = urllib.urlopen(trans)
	soup = BeautifulSoup(read,"html.parser")

	div = soup.find("div", {"class": "panes"})
	uls = div.findAll('ul')

	li_p = []
	li_to = []
	li_from = []

	for i in uls:
		t =i.find('li',{'class':'player'})
		[t.extract() for t in soup('span')]
		li_p.append(t.text.strip())
		li_to.append(i.find('li',{'class':'to'}).text.strip())
		li_from.append(i.find('li',{'class':'from'}).text.strip())
	
	li_final_to += li_to
	li_final_from += li_from
	li_final_p += li_p

index = []
j = len(li_final_p)
for x in range(j):
	if(li_final_p[x] == 'RSS'):
		index.append(x)

index.sort(reverse=True)

for ind in index:
	del li_final_p[ind]
	del li_final_to[ind]
	del li_final_from[ind]

final_data = zip(li_final_p,li_final_to,li_final_from)
index = 0
with open('transfer.csv', 'wb') as f:
	writer = csv.writer(f)
	for row in final_data:
		writer.writerow([s.encode('utf8') if type(s) is unicode else s for s in row]) 
