import requests #Package for making API calls
import sys #Package allowing for the use of variables in CLI
import json #allows pythong to convert json response to an object

#Get riot account PUUID using Account -v1 API point: get account by riot ID
gameName = "xLazor"
tagLine = "NA1"
apiKey = sys.argv[1] #Enter Riot key when running script
api = 'https://americas.api.riotgames.com'
getAccountEndPoint = f"/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={apiKey}" #API with variables note thatf is added to interpolate


accountResponse = requests.get(f"{api}{getAccountEndPoint}") #API call

puuid = (accountResponse.json()['puuid']) #string of puuid which is needed to call match IDs

#print(puuid)

#Get riot matchIDs using Match-v5 API point: get account by PUUID

getMatchesEndPoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids?/start=0&count=100&api_key={apiKey}" #To update and pass in variables in better manner

matchResponse = requests.get(f"{api}{getMatchesEndPoint}") #API call

print(matchResponse.json())