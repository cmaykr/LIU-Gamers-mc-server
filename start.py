import subprocess
import requests
import urllib.request
import os
import install
import installmods
import json
import shutil

def startServer():
    os.chdir("Servers/main")         
    subprocess.run(['java', '-jar', 'fabric-server-launch' + '.jar', 'nogui'])
    
with open('serverList.json', 'r') as file:
    data = json.load(file)
    for serverName in data:
        print(serverName)
        installmods.installMods(serverName)
        game_version = data[serverName]["game_version"]
        install.installServer(serverName, game_version, "25564")

startServer()

    

