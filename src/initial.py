import requests
import pandas as pd
import time
import datetime
import os

# Input de Dados
#
format_string = "%d/%m/%Y %H:%M:%S.%f"

now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
formattedCurrentDate = datetime.datetime.strptime(now, format_string)

timestamps = dict()

def utc_to_epoch(date):
    return int(time.mktime(datetime.datetime.strptime(date, format_string).timetuple()))*1000

for monthsAgo in range(6):
    end_date_str = (formattedCurrentDate - pd.DateOffset(months=monthsAgo)).strftime(format_string)
    end_timestamp_value = utc_to_epoch(end_date_str)

    start_date_str = (formattedCurrentDate - pd.DateOffset(months=monthsAgo+1)).strftime(format_string)
    start_timestamp_value = utc_to_epoch(start_date_str)

    timestamps[monthsAgo] = (start_timestamp_value, end_timestamp_value)

if os.path.exists(os.path.expanduser('~/cobliBI/data_file.txt')): 
    with open(os.path.expanduser('~/cobliBI/data_file.txt'), 'r') as data_file:
        last_refresh = data_file.read()

    if last_refresh:
        shortTimestamp = dict()
        shortTimestamp[0] = [utc_to_epoch(last_refresh), utc_to_epoch(now)]