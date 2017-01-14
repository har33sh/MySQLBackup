import os
from datetime import date, timedelta

yesterday = date.today() - timedelta(1)
print yesterday.strftime('%m-%d-%y')

directory=yesterday.strftime('%m-%d-%y')
## dd/mm/yyyy format
if not os.path.exists(directory):
    os.makedirs(directory)
tweets = open(directory+"/keywo.txt", "a+")
print>>tweets, "Hel"
tweets.close()
