import requests
import pandas as pd
from initial import start_timestamp, end_timestamp


def getIncidentsDataFrame(apiKey=None, end_timestamp=end_timestamp, start_timestamp=start_timestamp):
    incidentsURL = f"https://api.cobli.co/herbie-1.1/stats/incidents/report?begin={start_timestamp}&end={end_timestamp}&tz=America%2FFortaleza"
    incidentsResponse = requests.get(
        incidentsURL, headers={'cobli-api-key': apiKey})
    return pd.read_excel(incidentsResponse.content, 0)


incidents_function_name = 'getIncidentsDataFrame'
