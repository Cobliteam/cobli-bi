import requests
import pandas as pd
from initial import timestamps, shortTimestamp
import os


def getProductivityDataFrame(apiKey=None, fleetName='', currentTimestamp=shortTimestamp or timestamps):
    frames = []
    if os.path.exists(os.path.expanduser('~/cobliBI/productivity.csv')): 
        frames.append(pd.read_csv(os.path.expanduser('~/cobliBI/productivity.csv')))
    for month in currentTimestamp:
        start_timestamp, end_timestamp = currentTimestamp[month]
        productivityURL = f"https://api.cobli.co/herbie-1.1/stats/performance/vehicle/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
        productivityResponse = requests.get(
            productivityURL, headers={'cobli-api-key': apiKey})
        frames.append(pd.read_excel(productivityResponse.content, 2))
    dataframe = pd.concat(frames)
    dataframe['Frota'] = [fleetName] * len(dataframe.index)
    dataframe.to_csv(os.path.expanduser('~/cobliBI/productivity.csv'), index = False)
    return dataframe

productivity_function_name = 'getProductivityDataFrame'
