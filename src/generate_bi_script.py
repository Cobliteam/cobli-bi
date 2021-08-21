import inspect
import requests
from productivity import getProductivityDataFrame, productivity_function_name
from costs import getCostsDataFrame, costs_function_name
from incidents import getIncidentsDataFrame, incidents_function_name
import os
from dotenv import load_dotenv

load_dotenv()

productivityScript = inspect.getsource(getProductivityDataFrame)
costsScript = inspect.getsource(getCostsDataFrame)
incidentsScript = inspect.getsource(getIncidentsDataFrame)

with open("../output/data.py", "r") as dataFile:
    apiKeyList = dataFile.read() or os.getenv('API_KEY')
    parsedApiKeyList = apiKeyList.replace(' ', '').split(',')

os.remove("../output/data.py")

with open("../src/initial.py", "r") as initialFile, \
        open('../output/main_file.py', 'w') as main_file:
        main_file.write(initialFile.read() + '\n\n')
        main_file.write(costsScript + '\n')
        main_file.write(incidentsScript + '\n')
        main_file.write(productivityScript + '\n')
        for key in parsedApiKeyList:
            response = requests.get('https://api.cobli.co/api-keys/external-auth', headers={'cobli-api-key': key})
            
            if(response.status_code != 200):
                print(f"Algo de errado aconteceu na coleta de dados da API, usando a chave {key} \n\n")
                input("Pressione uma tecla para continuar!")
                exit()

            fleetId = response.headers.get('cobli-fleet-id').replace('.', '_').replace('-', '_')
            main_file.write(
                f"costsFunction_{fleetId} = {costs_function_name}('{key}')\n\n")
            main_file.write(
                f"incidentsFunction_{fleetId} = {incidents_function_name}('{key}')\n\n")
            main_file.write(
                f"productivityFunction_{fleetId} = {productivity_function_name}('{key}')\n\n")
