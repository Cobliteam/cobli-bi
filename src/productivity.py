import requests
import pandas as pd
from initial import timestamps


def getProductivityDataFrame(apiKey=None, fleetId='', timestamps=timestamps):
    frames = []
    for month in timestamps:
        start_timestamp, end_timestamp = timestamps[month]
        productivityURL = f"https://api.cobli.co/herbie-1.1/stats/performance/vehicle/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
        productivityResponse = requests.get(
            productivityURL, headers={'cobli-api-key': apiKey})
        frames.append(pd.read_excel(productivityResponse.content, 2))
    dataframe = pd.concat(frames)
    
    return dataframe.assign(Frota = [fleetId] * len(dataframe.index))

productivity_function_name = 'getProductivityDataFrame'
