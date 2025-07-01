import requests
import urllib
import json
import os


def installMods():
    current_dir = os.getcwd()
    os.chdir("/home/david/Documents/Minecraft Server")
    with open('modList.json', 'r') as file:
        data = json.load(file)
        game_version = data["main"]["game_version"]
        serverDirectory = data["main"]["directory"]
        for mod in data["main"]["mods"]:
            print(mod)
            installMod(mod, game_version, serverDirectory)
            
    os.chdir(current_dir)
        
def installMod(modName, game_version, serverDirectory):
    # print("https://api.modrinth.com/v2/project/" + modName + "/version?game_versions=[%22" + game_version + "%22]")
    res = requests.get("https://api.modrinth.com/v2/project/" + modName + "/version?game_versions=[%22" + game_version + "%22]")
    
    print(res.json()[0]["files"][0]["url"])
    
    URI = res.json()[0]["files"][0]["url"]
    filename = res.json()[0]["files"][0]["filename"]
    
    
    if not os.path.exists("Servers/" + serverDirectory + "/mods"):
        os.makedirs("Servers/" + serverDirectory + "/mods")
    with urllib.request.urlopen(URI) as f:
        with open("Servers/" + serverDirectory + "/mods/" + filename, 'wb') as file:
            file.write(f.read())
    
installMods()