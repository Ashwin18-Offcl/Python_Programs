"""Calculate the date 4 months from the current date"""
"""Given
#2020-02-25 
date_1 =datetime(2020, 2, 25)
#2020-09-17
date_2 = datetime(2020, 9, 17)
Expected output:
205 days
"""
#2020-02-25
from datetime import datetime
date_1 = datetime(2020, 2, 25).date()

#2020-09-17
date_2 = datetime(2020, 9, 17).date()
delta = None
if date_1>date_2:
    delta=date_1-date_2
else:
    delta=date_2-date_1
print("Difference of the days will be :\n",delta.days)
