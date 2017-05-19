from operator import itemgetter
import numpy as np

f = open('LeagueTransfers.csv')
data=[]
teamNames=[]
for row in f:
    datarow=row.split(',')
    if(len(datarow)>4):
        del datarow[2]
    data.append(datarow)
for i in range(1,len(data)):
    teamNames.append(data[i][1])
teamNames=list(set(teamNames))
teamNames.sort()
teamTransferMatrix=np.zeros((len(teamNames),len(teamNames)),dtype=np.int)
index=1
for i in range(3,len(data)):
    playerId=data[i-1][2]
    newPlayerID=data[i][2]
    if(newPlayerID!=playerId):
        for j in range(index+1,i):
            teamName=data[j-1][1]
            newTeamName=data[j][1]
            if(newTeamName!=teamName):
                teamTransferMatrix[teamNames.index(teamName)][teamNames.index(newTeamName)] +=1
        index=i
del data[0]
teamList=[]
LeagueTeamList=[]
teamIndex=[]
LeagueToTeamMap={}
index=0
data=sorted(data, key=itemgetter(0))
for i in range(1,len(data)):
    leagueName=data[i-1][0]
    newLeagueName=data[i][0]
    if(newLeagueName!=leagueName):
        for j in range(index,i):
            teamList.append(data[j][1])
        teamList=list(set(teamList))
        teamList.sort()
        for item in teamList:
            teamIndex.append(teamNames.index(item))
        LeagueToTeamMap[leagueName]=teamIndex
        LeagueTeamList.append(teamList)
        teamList=[]
        teamIndex=[]
        index=i
BelgiumTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Belgium Jupiler League'],LeagueToTeamMap['Belgium Jupiler League'])]
EnglandTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['England Premier League'],LeagueToTeamMap['England Premier League'])]
FranceTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['France Ligue 1'],LeagueToTeamMap['France Ligue 1'])]
GermanyTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Germany 1. Bundesliga'],LeagueToTeamMap['Germany 1. Bundesliga'])]
ItalyTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Italy Serie A'],LeagueToTeamMap['Italy Serie A'])]
NetherlandsTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Netherlands Eredivisie'],LeagueToTeamMap['Netherlands Eredivisie'])]
PolandTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Poland Ekstraklasa'],LeagueToTeamMap['Poland Ekstraklasa'])]
PortugalTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Portugal Liga ZON Sagres'],LeagueToTeamMap['Portugal Liga ZON Sagres'])]
ScotlandTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Scotland Premier League'],LeagueToTeamMap['Scotland Premier League'])]
SpainTransferMatrix=teamTransferMatrix[np.ix_(LeagueToTeamMap['Spain LIGA BBVA'],LeagueToTeamMap['Spain LIGA BBVA'])]