import requests
import urllib
import json
import os


def installMods(serverName):
    current_dir = os.getcwd()
    os.chdir("/home/david/Documents/Minecraft Server")
    print(os.getcwd())
    with open('serverList.json', 'r') as file:
        data = json.load(file)
        print(data[serverName])
        print(data[serverName]['game_version'])
        game_version = data[serverName]['game_version']
        for mod in data[serverName]["mods"]:
            print(mod)
            installMod(mod, game_version, serverName)
            
    print(current_dir)
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
    

# with open('serverList.json', 'r') as file:
#     data = json.load(file)
#     for serverName in data:
#         print(serverName)
#         installMods(serverName)