from datetime import datetime, timedelta
from pytz import timezone
import pytz
utc = pytz.utc
print("UTC Zone : ", utc.zone)
eastern = timezone('US/Eastern')  # 'US/Eastern'
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
loc_dt = eastern.localize(datetime(2021, 2, 10, 8, 54, 0))
print(loc_dt.strftime(fmt))

'''
2-August-2022
02-August-2022
2-Aug-22
02-Aug-22
02-08-22
02-08-2022
08-02-2022
Aug-02-2022
Aug-02-22
02/02/22

'''




from calendar import month
import calendar
from datetime import *
from datetime import datetime
import time

import pytz

cur_dt_time = datetime.now()
print("Now---------", cur_dt_time)
val = datetime.strptime('Wed May 12 2021', '%a %b %d %Y').strftime('%d-%m-%Y')
print("Formatted date time : ", val)
'''
2021-02-10 WED
10-02-2021 WED
02-10-2021 WED
10-02-21 WED
2021-02-10 Wednesday
10-02-2021 Wednesday
02-10-2021 Wednesday
10-02-21 Wednesday

10-Feb-21
10th Feb 2021
Feb-10-21
Feb-10-2021


2020-03-30 10:20:51
2020-03-30 10:20
2020-03-30 10
2020-03-30
30-03-2020
03-30-2020
30-Mar-2020
30-Mar-20
'''
#now = datetime.strptime(now,"YYYY-MM-DD")
#print("Now---------",now)
#now = now.astimezone(pytz)
#print("Now---------",now)
# EPOCH Time
epoch = time.time()
print("Epoch        Time :", epoch)

# Current Time
current_time = time.ctime()
print("Current time      :", current_time)

print("--------------------------")
# Current Date Time
now = datetime.now()
print("Current Date time :", now)
print("Date now          : {}-{}-{}".format(now.day, now.month, now.year))
print("--------------------------")
# Today's date and Time

tdm = datetime.today()
print("Today's Date & Time :", tdm)
td = date.today()
print("Today's Date        :", td)
print("Today's Date        :", td.strftime("%d, %B, %Y"))

# CALENDAR
yy = int(input("Enter year : "))
mm = int(input("Enter month: "))

str1 = month(yy, mm)
print("Calendar for Current Month", str1)

year = int(input("Enter year :"))
print(calendar.calendar(year, 2, 1, 8, 3))


'''
# facebook USA India - 2-Feb-2021 8.40AM GMT+5.30 Hours -> P  
# UI    ---> Python          ---> Database
  India      EST time zone   ---> 1-Feb-2021 11.40 PM
'''

