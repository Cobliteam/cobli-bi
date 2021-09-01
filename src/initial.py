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
shortTimestamp = None

def utc_to_epoch(date):
    return int(time.mktime(datetime.datetime.strptime(date, format_string).timetuple()))*1000

for monthsAgo in range(6):
    end_date_str = (formattedCurrentDate - pd.DateOffset(months=monthsAgo)).strftime(format_string)
    end_timestamp_value = utc_to_epoch(end_date_str)

    start_date_str = (formattedCurrentDate - pd.DateOffset(months=monthsAgo+1)).strftime(format_string)
    start_timestamp_value = utc_to_epoch(start_date_str)

    timestamps[monthsAgo] = (start_timestamp_value, end_timestamp_value)

if os.path.exists(os.path.expanduser('~/cobliBI/data_file.csv')): 
    last_refresh = pd.read_csv(os.path.expanduser('~/cobliBI/data_file.csv'))
    if last_refresh.columns[0]:
        shortTimestamp = dict()
        shortTimestamp[0] = [utc_to_epoch(last_refresh.iat[0,0]), utc_to_epoch(now)]