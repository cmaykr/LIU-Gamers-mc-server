import subprocess
import requests
import urllib.request
import os
import install
import installmods
import json
import shutil
    
with open('serverList.json', 'r') as file:
    data = json.load(file)
    for i, serverName in enumerate(data):
        installmods.installMods(serverName)
        game_version = data[serverName]["game_version"]
        install.installServer(serverName, game_version, str(25556 + i))
        
        src = 'worlds/' + serverName
    
        dst = 'Servers/' + serverName + '/world'
        shutil.copytree(src, dst, dirs_exist_ok=True)
