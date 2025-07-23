import subprocess
import os
import json

def startProxy():
    os.chdir('Proxy')
    
    print(os.getcwd())
    subprocess.Popen(['tmux', 'new-session', '-d', '-s', 'Proxy', 'java -jar velocity.jar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
def startServer(serverPath, serverName):
    rootPath = os.getcwd()
    os.chdir(serverPath)
    print(serverPath)
    print('java -jar' +  serverPath + '/fabric-server-launch.jar nogui')
    subprocess.Popen(['tmux', 'new-session', '-d', '-s', serverName, 'java -jar fabric-server-launch.jar nogui'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
    os.chdir(rootPath)
    
    
PIDs = []
rootPath = os.getcwd()
startProxy()
os.chdir(rootPath)
with open('serverList.json', 'r') as serverListFile:
    data = json.load(serverListFile)
    for serverName in data:
        # print('Servers/' + serverName)
        startServer('Servers/' + serverName, serverName)
        
        