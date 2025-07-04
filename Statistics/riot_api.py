import requests #Package for making API calls
import sys #Package allowing for the use of variables in CLI
import json #allows python to convert json response to an object

#Get riot account PUUID using Account -v1 API point: get account by riot ID
gameName = "xLazor"
tagLine = "NA1"
apiKey = sys.argv[1] #Enter Riot key when running script
api = 'https://americas.api.riotgames.com'
getAccountEndPoint = f"/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={apiKey}" #API with variables note thatf is added to interpolate


accountResponse = requests.get(f"{api}{getAccountEndPoint}") #API call

puuid = (accountResponse.json()['puuid']) #string of puuid which is needed to call match IDs


#Get riot matchIDs using Match-v5 API point: get account by PUUID

getMatchesEndPoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids?/start=0&count=20&api_key={apiKey}" #To update and pass in variables in better manner

matchResponse = requests.get(f"{api}{getMatchesEndPoint}") #API call

matchArr = matchResponse.json() #saves match IDs as an array

#Get match information using Match-v5 API endpoint: get a matchline by match id
matchData = []

for match in matchArr:
    GetMatchTimelineEndPoint= f"/lol/match/v5/matches/{match}/timeline?api_key={apiKey}"
    matchTimeline = requests.get(f"{api}{GetMatchTimelineEndPoint}") #API call for Match data
    matchData.append(matchTimeline) #add 200 response for each match

print(matchData)