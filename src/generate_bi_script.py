import inspect
import requests
from productivity import getProductivityDataFrame, productivity_function_name
from costs import getCostsDataFrame, costs_function_name
from incidents import getIncidentsDataFrame, incidents_function_name
import os
from dotenv import load_dotenv
from PySimpleGUI import PySimpleGUI as sg

load_dotenv()

productivityScript = inspect.getsource(getProductivityDataFrame)
costsScript = inspect.getsource(getCostsDataFrame)
incidentsScript = inspect.getsource(getIncidentsDataFrame)


def generate_script(apiKeyList):
    apiKeyList = apiKeyList or os.getenv('API_KEY')
    parsedApiKeyList = apiKeyList.replace(' ', '').split(',')

    fleetData = dict()

    for key in parsedApiKeyList:
        response = requests.get(
            'https://api.cobli.co/api-keys/external-auth', headers={'cobli-api-key': key})
        if(response.status_code != 200):
            modalButton = sg.popup_yes_no(f"Algo de errado aconteceu na coleta de dados da API, usando a chave {key}. Deseja revisar as chaves inseridas?",
                                          title="Erro com chave de API")
            if modalButton == 'Yes':
                return
            exit()

        fleetData[key] = response.headers.get(
            'cobli-fleet-id').replace('.', '_').replace('-', '_')

    with open("../src/initial.py", "r") as initialFile, \
            open('../output/main_file.txt', 'w') as main_file:
        main_file.write(initialFile.read() + '\n\n')
        main_file.write(costsScript + '\n')
        main_file.write(incidentsScript + '\n')
        main_file.write(productivityScript + '\n')
        for key in parsedApiKeyList:
            main_file.write(
                f"costsFunction_{fleetData[key]} = {costs_function_name}('{key}')\n\n")
            main_file.write(
                f"incidentsFunction_{fleetData[key]} = {incidents_function_name}('{key}')\n\n")
            main_file.write(
                f"productivityFunction_{fleetData[key]} = {productivity_function_name}('{key}')\n\n")
    exit()


sg.theme('Reddit')
layout = [
    [sg.Text('Por favor, digite as chaves de API das frotas desejadas, separadas por vírgula:')],
    [sg.Input(key='apiKeyList', size=(20, 1))],
    [sg.Button('Gerar Script')]
]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == 'Gerar Script':
        generate_script(values['apiKeyList'])
        window.find_element('apiKeyList').Update('')
