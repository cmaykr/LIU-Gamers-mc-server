import os
import subprocess
import json

def killServer(processName):
    subprocess.run(['tmux', 'kill-session', '-t', processName])
    
with open("serverList.json", 'r') as jsonfile:
    data = json.load(jsonfile)
    
    print("Killing proxy server...")
    killServer("Proxy")
    for serverName in data:
        print("Killing " + serverName + " server...")
        killServer(serverName)