import requests
import pandas as pd
from initial import start_timestamp, end_timestamp


def getCostsDataFrame(apiKey=None, end_timestamp=end_timestamp, start_timestamp=start_timestamp):
    costsURL = f"https://api.cobli.co/herbie-1.1/costs/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
    costsResponse = requests.get(costsURL, headers={'cobli-api-key': apiKey})
    return pd.read_excel(costsResponse.content, 0)


costs_function_name = 'getCostsDataFrame'
