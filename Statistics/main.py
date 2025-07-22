import pandas as pd
import convert_timestamp as convert_timeStamp
import count_daily_game as count_daily_game
import matplotlib.pyplot as plt 
from scipy.stats import poisson
import numpy as np

df = pd.read_csv('.\match_history.csv') #Read in match history as data frame

convertedDates = [] #Placeholder for updated Date
convertedStartTime = [] #Placeholder for updated Date
convertedEndTime =[] #Placeholder for updated Date

#Converts startTime timestamp to date
for timeStamp in df['startTime']:
        convertedDates.append(convert_timeStamp.convertTimeStamp(timeStamp)) #Gets the date of the game
        convertedStartTime.append(convert_timeStamp.convertTimeStamptoTime(timeStamp)) #Gets the time of the game

#Converts endTime time stamp to time
for endTimeStamp in df['endTime']:
        convertedEndTime.append(convert_timeStamp.convertTimeStamptoTime(endTimeStamp)) #Gets the end time of the game)

df['gameDates'] = convertedDates #add new column for date
df['gameStart'] = convertedStartTime #add new column for start time
df['gameEnd'] = convertedEndTime #add new column for end time
gamesPlayedPerDay = count_daily_game.gamesPerDayCounter(df['gameDates']) #Counts the games played per day

def findAverageDailyGames(gameDict): #Calculates average of the daily games played to be moved in helper file
        countofRecords = 0
        totalGames = 0
        for day in gameDict:
                countofRecords += 1
                totalGames = gameDict[day] + totalGames
        return totalGames / countofRecords

avgGamesPerDay = findAverageDailyGames(gamesPlayedPerDay)

#Caluculating the duration of the games
duration = []
for i in range(len(convertedStartTime)-1):
        gameLength = convert_timeStamp.calculateDuration(convertedStartTime[i], convertedEndTime[i])
        duration.append(gameLength)

# Manual calculation of PMF
# def poissonPlots(avgGames): #Function to calculate the plot points for a poisson distribution
#         result = {}
#         for i in range(5):
#                 result[i] = (math.exp(-avgGames) * ((avgGames) ** i)/ math.factorial(i))
#         return result

xAxis = np.arange(10) #Creating the x axis
pmf = poisson.pmf(xAxis, avgGamesPerDay) #Calculating PMF for each k

#Details for plotting distribution

plt.figure(figsize=(8, 5))
plt.bar(xAxis, pmf, color='skyblue', edgecolor='black')
plt.title(f'Poisson Distribution (λ = {avgGamesPerDay})')
plt.xlabel('Number of Events (k)')
plt.ylabel('Probability')
plt.xticks(xAxis) # Ensure integer ticks on the x-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



'''
Next Steps:
1. Update dataframe with updated column - Complete
2. Write function to summarize by day and count of games - Complete
3. Estimate the average games per day - Complete
4. Check out what is causing cap on number of records written - complete
'''