import subprocess
import requests
import urllib.request
import os

def startServer():
    os.chdir('main')
    
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
    
startServer()