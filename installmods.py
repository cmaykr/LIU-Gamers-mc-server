import requests
import urllib
import json
import os


def installMods(serverName):
    with open('serverList.json', 'r') as file:
        data = json.load(file)
        
        print([serverName])
        game_version = data["servers"][serverName]['game_version']
        for mod in data["servers"][serverName]["mods"]:
            print(mod)
            installMod(mod, game_version, "Servers/" + serverName + "/mods")
        
def installMod(modName, game_version, directory):
    res = requests.get("https://api.modrinth.com/v2/project/" + modName + "/version?game_versions=[%22" + game_version + "%22]") 
    data = res.json()
    
    versionIndex = -1
    for idx, version in enumerate(data):
        for loader in version["loaders"]:
            if loader == "fabric":
                versionIndex = idx
    
    if versionIndex == -1:
        raise ValueError("Mod" + modName + " for game version " + game_version + " and fabric type not found. Check for mistype or if mod exists for this version.")
    URI = res.json()[versionIndex]["files"][0]["url"]
    filename = res.json()[versionIndex]["files"][0]["filename"]
    
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    with urllib.request.urlopen(URI) as f:
        with open(os.path.join(directory, filename), 'wb') as file:
            file.write(f.read())