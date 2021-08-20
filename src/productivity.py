import requests
import pandas as pd
from initial import start_timestamp, end_timestamp, apiKey


def getProductivityDataFrame(apiKey=apiKey, end_timestamp=end_timestamp, start_timestamp=start_timestamp):
    productivityURL = f"https://api.cobli.co/herbie-1.1/stats/performance/vehicle/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
    productivityResponse = requests.get(
        productivityURL, headers={'cobli-api-key': apiKey})
    return pd.read_excel(productivityResponse.content, 2)


productivity_function_name = 'getProductivityDataFrame'
