import subprocess
import requests
import urllib.request
import os

file_path = 'main'
serverName = 'server'
def installServer():
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    os.chdir(file_path)
    installerName = 'fabric-installer.jar'
    with urllib.request.urlopen('https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.3/fabric-installer-1.0.3.jar') as f:
        with open(installerName, 'wb') as file:
            file.write(f.read())
    
    
    subprocess.run(['java', '-jar', installerName, serverName, '-downloadMinecraft'])
    
    
def startServer():
    port = "25564"
    with open('server.properties', 'r+') as file:
        data = file.readlines()
        print(data)
        
        for idx, line in enumerate(data):
            if (line.split('=')[0] == 'server-port'):
                line = 'server-port=' + port + '\n'
                data[idx] = line
                break

        file.write(''.join(data))
        print(data)
                
    subprocess.run(['java', '-jar', 'fabric-server-launch' + '.jar', 'nogui'])
    
installServer()
startServer()