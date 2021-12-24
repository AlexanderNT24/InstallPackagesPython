import json 
import subprocess
import sys

def install(nameDependency):
    subprocess.check_call([sys.executable, "-m", "pip", "install", nameDependency])

with open('proyect.json') as file:
    data = json.load(file)
    for dataProyect in data['proyect']:
        print(dataProyect)
        for dependency in dataProyect['dependencies']:
            print(dependency)
            install(dependency)
