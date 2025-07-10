import pandas as pd
import convert_timestamp as convert_timeStamp
import count_daily_game as count_daily_game

df = pd.read_csv('.\match_history.csv') #Read in match history as data frame

convertedColumn = [] #Placeholder for updated Date

#Converts startTime timestap to date
for timeStamp in df['startTime']:
        convertedColumn.append(convert_timeStamp.convertTimeStamp(timeStamp))

df['gameDates'] = convertedColumn #add new column

gamesPlayedPerDay = count_daily_game.gamesPerDayCounter(df['gameDates']) #Counts the games played per day

def findAverageDailyGames(gameDict): #Calculates average of the daily games played to be moved in helper file
        countofRecords = 0
        totalGames = 0
        for day in gameDict:
                countofRecords += 1
                totalGames = gameDict[day] + totalGames
        return totalGames / countofRecords

print(findAverageDailyGames(gamesPlayedPerDay))




'''
Next Steps:
1. Update dataframe with updated column - Complete
2. Write function to summarize by day and count of games
3. Estimate the average games per day
4. Check out what is causing cap on number of records written
'''