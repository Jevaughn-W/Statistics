import pandas as pd
import convert_timestamp as convert_timeStamp

df = pd.read_csv('.\match_history.csv') #Read in match history as data frame

#print(df)

for time in df["startTime"]:
        print(convert_timeStamp.convertTimeStamp(time))


'''
Next Steps:
1. Update dataframe with updated column
2. Write function to summarize by day and count of games
3. Estimate the average games per day
4. Check out what is causing cap on number of records written
'''