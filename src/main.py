import os
import platform
from shutil import which

if platform.system() == "Windows" and which("python") is None:
    if not os.path.isfile('./python.exe'):
        print("Fazendo download do Python")
        os.system("curl https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -o python.exe --silent")
    print("Instalando Python no seu computador...")
    os.system(".\python.exe /passive")
    os.system("pip install -q pandas matplotlib requests openpyxl")

apiKeyList = input('Por favor, digite as chaves de API das frotas desejadas, separadas por vírgula: \n\n')

with open("../output/data.py", "w") as dataFile:
    dataFile.write(apiKeyList)

os.system("python ../src/generate_bi_script.py")