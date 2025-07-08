import requests #Package for making API calls
import sys #Package allowing for the use of variables in CLI
import json #allows python to convert json response to an object
import pandas as pd #allows transformation of data and writing to CSV file

#Get riot account PUUID using Account -v1 API point: get account by riot ID
gameName = "xLazor"
tagLine = "NA1"
apiKey = sys.argv[1] #Enter Riot key when running script
countOfMatchesRequested = sys.argv[2] #Error when using 100 matches -- Check if there is a limit of requests per seconds
api = 'https://americas.api.riotgames.com'
getAccountEndPoint = f"/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={apiKey}" #API with variables note thatf is added to interpolate


accountResponse = requests.get(f"{api}{getAccountEndPoint}") #API call

puuid = (accountResponse.json()['puuid']) #string of puuid which is needed to call match IDs


#Get riot matchIDs using Match-v5 API point: get account by PUUID

getMatchesEndPoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids?/start=0&count={countOfMatchesRequested}&api_key={apiKey}" #To update and pass in variables in better manner

matchResponse = requests.get(f"{api}{getMatchesEndPoint}") #API call

matchArr = matchResponse.json() #saves match IDs as an array

#Get match information using Match-v5 API endpoint: get a matchline by match id
matchData = []

for match in matchArr:
    GetMatchTimelineEndPoint= f"/lol/match/v5/matches/{match}?api_key={apiKey}"
    matchTimeline = requests.get(f"{api}{GetMatchTimelineEndPoint}") #API call for Match data
    
    matchData.append({
        "matchId": matchTimeline.json()['metadata']["matchId"],
        "startTime": matchTimeline.json()["info"]["gameCreation"],
        }) #add response (start, end and match ID) for each match

# Creating structuring data and write to CSV file

df = pd.DataFrame(
    matchData
)

df.to_csv('match_history.csv', index=True)