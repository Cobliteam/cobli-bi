import requests
import pandas as pd
import time
import datetime
import os

# Input de Dados
#
format_string = "%d/%m/%Y %H:%M:%S.%f"

now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")

timestamps = dict()

for monthsAgo in range(6):
    end_date_str = (datetime.datetime.strptime(now, format_string) - pd.DateOffset(months=monthsAgo)).strftime(format_string)
    end_timestamp_value = int(time.mktime(
    datetime.datetime.strptime(end_date_str, format_string).timetuple()))*1000

    start_date_str = (datetime.datetime.strptime(now, format_string) - pd.DateOffset(months=monthsAgo+1)).strftime(format_string)
    start_timestamp_value = int(time.mktime(
    datetime.datetime.strptime(start_date_str, format_string).timetuple()))*1000

    timestamps[monthsAgo] = (start_timestamp_value, end_timestamp_value)

if os.path.exists('./data_file.txt'): 
    with open('./data_file.txt', 'r') as data_file:
        last_refresh = data_file.read()

    if last_refresh:
        timestamps = [last_refresh, now]