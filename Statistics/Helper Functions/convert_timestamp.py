from datetime import datetime #allows convertion from Riots usage of unix to datetime


def convertTimeStamp(timeStamp):
    #convert milliseconts to seconds
    seconds = timeStamp/1000

    results =  datetime.fromtimestamp(seconds).strftime("%m/%d/%y") #Converts from time stamp to date and time then format to only show date

    return results



