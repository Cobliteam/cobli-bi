import os
import platform
from shutil import which

if platform.system() == "Windows" and which("python", mode=os.X_OK) == None:
    if not os.path.isfile('./installpython.exe'):
        print("Fazendo download do Python")
        os.system("curl https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -o installpython.exe --silent")
    print("Instalando Python no seu computador...")
    os.system(".\installpython.exe /quiet InstallAllUsers=1 PrependPath=1")
    os.system("pip install -q pandas matplotlib requests openpyxl")

os.system("python ../src/generate_bi_script.py")