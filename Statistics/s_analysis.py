from datetime import datetime #allows convertion from Riots usage of unix to datetime

ts = int('1751576054512')
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))