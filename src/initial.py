import requests
import pandas as pd
import time
import datetime
import platform
import os
from shutil import which

# Input de Dados
#
start = "01/06/2021 16:31:32.123"
end = "16/06/2021 23:59:59.123"
apiKey = os.getenv('API_KEY')
#
format_string = "%d/%m/%Y %H:%M:%S.%f"
start_timestamp = int(time.mktime(
    datetime.datetime.strptime(start, format_string).timetuple()))*1000
end_timestamp = int(time.mktime(
    datetime.datetime.strptime(end, format_string).timetuple()))*1000
