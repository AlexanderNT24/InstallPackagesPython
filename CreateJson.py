import json 
import os

localPath = os.getcwd()
numberIterations=int(input("Number of Modules: "))

proyectData={}
proyectData['proyect'] = []
dependencies=[]


for index in range(1,numberIterations+1) :
    dependency=input(f"Module number {index}: ")
    dependencies.append(dependency)

proyectData['proyect'].append({
    'name': localPath,
    'dependencies':dependencies
})

with open('proyect.json', 'w') as file:
    json.dump(proyectData, file,indent=4)