import requests
import pandas as pd
from initial import timestamps
import os


def getIncidentsDataFrame(apiKey=None, fleetName='',  currentTimestamp=timestamps):
    frames = []
    for month in currentTimestamp:
        start_timestamp, end_timestamp = currentTimestamp[month]
        incidentsURL = f"https://api.cobli.co/herbie-1.1/stats/incidents/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
        incidentsResponse = requests.get(
            incidentsURL, headers={'cobli-api-key': apiKey})
        frames.append(pd.read_excel(incidentsResponse.content, 0))
    dataframe = pd.concat(frames)
    dataframe['Frota'] = [fleetName] * len(dataframe.index)
    dataframe.to_csv(os.path.expanduser('~/cobliBI/incidents.csv'), index = False)
    return dataframe

incidents_function_name = 'getIncidentsDataFrame'
