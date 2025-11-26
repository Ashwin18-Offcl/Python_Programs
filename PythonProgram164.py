"""Covert string into a datetime object"""
"""For example, You received the following date in string format.Please convert it into Python's date Time object
date_string = 'Feb 25 2020 4:20PM"""
from datetime import datetime
date_string="Feb 25 2020 4:20PM"
date_time_object = datetime.strptime(date_string,"%b %d %Y %I:%M%p")
print(date_time_object)