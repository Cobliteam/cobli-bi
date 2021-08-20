import platform
import os
from shutil import which

def installing_libraries():
    if platform.system() != "Windows":
        return

    if which("python") is None:
        if not os.path.isfile('./python.exe'):
            print("fazendo download do python")
            os.system("curl https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -o python.exe --silent")
        print("instalando python no seu computador...")
        os.system(".\python.exe /passive")
        os.system("pip install -q pandas matplotlib requests openpyxl")

windows_requirements_function_name = 'installing_libraries'