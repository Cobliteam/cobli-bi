import requests
import pandas as pd
from initial import timestamps


def getIncidentsDataFrame(apiKey=None, fleetId='', timestamps=timestamps):
    frames = []
    for month in timestamps:
        start_timestamp, end_timestamp = timestamps[month]
        incidentsURL = f"https://api.cobli.co/herbie-1.1/stats/incidents/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
        incidentsResponse = requests.get(
            incidentsURL, headers={'cobli-api-key': apiKey})
        frames.append(pd.read_excel(incidentsResponse.content, 0))
    dataframe = pd.concat(frames)
    
    dataframe.assign(Frota = [fleetId] * len(dataframe.index))
    dataframe.to_csv('incidents.csv')
    return dataframe

incidents_function_name = 'getIncidentsDataFrame'
