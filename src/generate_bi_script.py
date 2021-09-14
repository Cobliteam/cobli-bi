import inspect
import os

import requests
from PySimpleGUI import PySimpleGUI as sg
from dotenv import load_dotenv

import initial
from gui import gui

load_dotenv()

initialSource = inspect.getsource(initial)


def check_api_keys(fleet_data: dict):
    for idx, key in enumerate(fleet_data):
        response = requests.get(
            'https://api.cobli.co/api-keys/external-auth', headers={'cobli-api-key': fleet_data[key]})
        if response.status_code != 200:
            modal_button = sg.popup_yes_no(
                f"Algo de errado aconteceu na coleta de dados da API, usando a chave {fleet_data[key]}. "
                f"Deseja revisar as chaves inseridas?",
                title="Erro com chave de API"
            )
            if modal_button == 'Yes':
                return idx
            exit()

    generate_script(fleet_data)


def generate_script(fleet_data: dict):
    script_string = f"{initialSource}\n\n"
    script_string += f'devices = get_devices_data({fleet_data})\n'
    script_string += f'checklists = get_checklist_data({fleet_data})\n'
    script_string += f'proofs_of_conclusion = get_pocs_data({fleet_data}, start_datetime, end_datetime)\n'
    script_string += f'costs = get_costs_data({fleet_data}, start_datetime, end_datetime)\n'
    script_string += f'incidents = get_incidents_data({fleet_data}, start_datetime, end_datetime)\n'
    script_string += f'vehicle_performance = get_vehicle_performance_data({fleet_data}, start_datetime, end_datetime)\n'
    script_string += f'driver_performance = get_driver_performance_data({fleet_data}, start_datetime, end_datetime)\n'

    os.makedirs(os.path.expanduser('~/cobliBI'), exist_ok=True)
    with open(os.path.expanduser('~/cobliBI/main_file.txt'), 'w') as main_file:
        main_file.write(script_string)


gui(check_api_keys)
