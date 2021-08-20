import inspect
from productivity import getProductivityDataFrame, productivity_function_name
from costs import getCostsDataFrame, costs_function_name
from incidents import getIncidentsDataFrame, incidents_function_name
from windows_requirements import installing_libraries, windows_requirements_function_name
import os
from dotenv import load_dotenv

load_dotenv()

productivityScript = inspect.getsource(getProductivityDataFrame)
costsScript = inspect.getsource(getCostsDataFrame)
incidentsScript = inspect.getsource(getIncidentsDataFrame)
windowsRequirementsScript = inspect.getsource(installing_libraries)

fleetNameList = [{
    'fleetName': 'a',
    'apiKey': os.getenv("API_KEY")
},
    {
    'fleetName': 'b',
    'apiKey': os.getenv("API_KEY")
}]


with open("src/initial.py", "r") as initialFile, \
        open('output/main_file.py', 'w') as main_file:
        main_file.write(initialFile.read() + '\n\n')
        main_file.write(windowsRequirementsScript + '\n\n' + f"{windows_requirements_function_name}()" + '\n\n')
        main_file.write(costsScript + '\n')
        main_file.write(incidentsScript + '\n')
        main_file.write(productivityScript + '\n')
        for fleet in fleetNameList:
            main_file.write(
                f"costsFunction_{fleet.get('fleetName')} = {costs_function_name}('{fleet.get('apiKey')}')\n\n")
            main_file.write(
                f"incidentsFunction_{fleet.get('fleetName')} = {incidents_function_name}('{fleet.get('apiKey')}')\n\n")
            main_file.write(
                f"productivityFunction_{fleet.get('fleetName')} = {productivity_function_name}('{fleet.get('apiKey')}')\n\n")
