import requests
import pandas as pd
from initial import timestamps


def getCostsDataFrame(apiKey=None, fleetId='', timestamps=timestamps):
    frames = []
    for month in timestamps:
        start_timestamp, end_timestamp = timestamps[month]
        costsURL = f"https://api.cobli.co/herbie-1.1/costs/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
        costsResponse = requests.get(costsURL, headers={'cobli-api-key': apiKey})
        frames.append(pd.read_excel(costsResponse.content, 0))
    dataframe = pd.concat(frames)
    dataframe.assign(Frota = [fleetId] * len(dataframe.index))
    dataframe.to_csv('costs.csv')
    return dataframe

costs_function_name = 'getCostsDataFrame'
