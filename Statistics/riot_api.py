import requests #Package for making API calls
import sys #Package allowing for the use of variables in CLI

#Get riot account PUUID using Account -v1 API point: get account by riot IF
gameName = "xLazor"
tagLine = "NA1"
apiKey = sys.argv[1] #Enter Riot key when running script

getAccountUrl = f"/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={apiKey}" #API with variables note thatf is added to interpolate


response = requests.get(f"https://americas.api.riotgames.com{getAccountUrl}") #API call


print(response)