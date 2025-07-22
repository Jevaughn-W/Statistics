from datetime import datetime #allows convertion from Riots usage of unix to datetime


def convertTimeStamp(timeStamp):
    #convert milliseconts to seconds
    seconds = timeStamp/1000

    results =  datetime.fromtimestamp(seconds).strftime("%m/%d/%y") #Converts from time stamp to date and time then format to only show date

    return results


def convertTimeStamptoTime(timeStamp):
    #convert milliseconts to seconds
    seconds = timeStamp/1000

    results =  datetime.fromtimestamp(seconds).strftime("%H:%M:%S") #Converts from time stamp to date and time then format to only show time

    return results

def calculateDuration(start, end):
    startObject = datetime.strptime(start, "%H:%M:%S")
    endObject = datetime.strptime(end, "%H:%M:%S")
    result = endObject - startObject

    return result.seconds