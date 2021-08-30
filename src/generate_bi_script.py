import inspect
import requests
from productivity import getProductivityDataFrame, productivity_function_name
from costs import getCostsDataFrame, costs_function_name
from incidents import getIncidentsDataFrame, incidents_function_name
from gui import gui
import os
from dotenv import load_dotenv
from PySimpleGUI import PySimpleGUI as sg
import initial

load_dotenv()

productivityScript = inspect.getsource(getProductivityDataFrame)
costsScript = inspect.getsource(getCostsDataFrame)
incidentsScript = inspect.getsource(getIncidentsDataFrame)
initialSource = inspect.getsource(initial)

def check_api_keys(apiKeyList: dict):
    for idx, key in enumerate(apiKeyList):
        response = requests.get(
            'https://api.cobli.co/api-keys/external-auth', headers={'cobli-api-key': apiKeyList[key]})
        if(response.status_code != 200):
            modalButton = sg.popup_yes_no(f"Algo de errado aconteceu na coleta de dados da API, usando a chave {apiKeyList[key]}. Deseja revisar as chaves inseridas?",
                                          title="Erro com chave de API")
            if modalButton == 'Yes':
                return idx
            exit()

    generate_script(apiKeyList)


def generate_script(apiKeyList: dict):
    with open('./main_file.txt', 'w') as main_file:
        main_file.write(initialSource + '\n\n')
        main_file.write(costsScript + '\n')
        main_file.write(incidentsScript + '\n')
        main_file.write(productivityScript + '\n')
        for key in apiKeyList:
            main_file.write(
                f"{costs_function_name}('{apiKeyList[key]}', '{key}')\n\n")
            main_file.write(
                f"{incidents_function_name}('{apiKeyList[key]}', '{key}')\n\n")
            main_file.write(
                f"{productivity_function_name}('{apiKeyList[key]}', '{key}')\n\n")
    with open('./data_file.txt', 'w') as data_file:
        data_file.write(initial.now)

gui(check_api_keys)