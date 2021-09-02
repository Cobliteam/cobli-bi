import requests
import pandas as pd
from initial import timestamps
import os


def getCostsDataFrame(apiKey=None, fleetName='', currentTimestamp=timestamps):
    frames = []
    for month in currentTimestamp:
        start_timestamp, end_timestamp = currentTimestamp[month]
        costsURL = f"https://api.cobli.co/herbie-1.1/costs/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
        costsResponse = requests.get(costsURL, headers={'cobli-api-key': apiKey})
        frames.append(pd.read_excel(costsResponse.content, 0))
    dataframe = pd.concat(frames)
    dataframe['Frota'] = [fleetName] * len(dataframe.index)
    dataframe.to_csv(os.path.expanduser('~/cobliBI/costs.csv'), index = False)
    return dataframe

costs_function_name = 'getCostsDataFrame'
