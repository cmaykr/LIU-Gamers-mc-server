import subprocess
import os
import json

def startProxy():
    os.chdir('Proxy')
    
    subprocess.Popen(['java', '-jar', 'velocity.jar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
def startServer(serverPath):
    rootPath = os.getcwd()
    os.chdir(serverPath)
    print(serverPath)
    print(os.getcwd())
    subprocess.Popen(['java', '-jar', 'fabric-server-launch' + '.jar', 'nogui'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)   
    os.chdir(rootPath)
    
    
rootPath = os.getcwd()
startProxy()
os.chdir(rootPath)
with open('serverList.json', 'r') as serverListFile:
    data = json.load(serverListFile)
    for serverName in data:
        # print('Servers/' + serverName)
        startServer('Servers/' + serverName)
        