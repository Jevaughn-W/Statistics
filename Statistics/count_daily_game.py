# sampleDates = [ 'a','a','b','c','d','d','d','e'] # Date for testing

def gamesPerDayCounter(dateArray):
    results ={} 

    for date in dateArray:                      #Loop through the array passed in from the dataframe
        if date in results:                     #Check if the loop has encountered the date already
            results[date] = 1 + results[date]   #If yes, add 1 to the count
        else:
            results[date] = 1                   #If no, add a key key with the count 1

    return results



# print(gamesPerDayCounter(sampleDates))










