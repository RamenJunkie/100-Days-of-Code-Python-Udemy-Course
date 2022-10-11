#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
## use mailer_class not Notification Manager, I already solved that problem.

## This doesn't work and I'm not signing up for this API because it wants payment info so I'm going to fake the
## motions a bit for the sake of learning.   I did fake some IATA Codes using the first three letters of each city
## in order to do the PUT function and update the sheets.  I considered making randomly generated fake prices but
## decided that really just wastes time in the end since the point is handling APIs, which I have had no problem
## with and just using random data is just wasting time to create garbage.

import mailer_class
import data_manager

mailer = mailer_class.Mailer()
dmanager = data_manager.DataManager()

#dmanager.add_city("data")
#dmanager.get_data()

row = 1
for each in dmanager.data["prices"]:
    # Add Missing IATA Codes
    row +=1
    if each["iataCode"] == "":
        dmanager.add_code(each["city"], row)
