import requests
import pandas as pd
import time
import datetime

# Input de Dados
#
format_string = "%d/%m/%Y %H:%M:%S.%f"

now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")
past_date =  datetime.datetime.strptime(now, format_string) - pd.DateOffset(months=6)
past_date_str = past_date.strftime(format_string)

start_timestamp = int(time.mktime(
    datetime.datetime.strptime(past_date_str, format_string).timetuple()))*1000
end_timestamp = int(time.mktime(
    datetime.datetime.strptime(now, format_string).timetuple()))*1000
