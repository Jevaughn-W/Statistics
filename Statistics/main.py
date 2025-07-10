import pandas as pd
import convert_timestamp as convert_timeStamp

df = pd.read_csv('.\match_history.csv') #Read in match history as data frame

convertedColumn = [] #Placeholder for updated Date

#Converts startTime timestap to date
for timeStamp in df['startTime']:
        convertedColumn.append(convert_timeStamp.convertTimeStamp(timeStamp))

df['gameDates'] = convertedColumn #add new column

print(df)


'''
Next Steps:
1. Update dataframe with updated column - Complete
2. Write function to summarize by day and count of games
3. Estimate the average games per day
4. Check out what is causing cap on number of records written
'''