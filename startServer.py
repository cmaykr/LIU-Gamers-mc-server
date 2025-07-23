import subprocess
import os
import json

def startProxy():
    os.chdir('Proxy')
    
    print("Starting proxy server...")
    subprocess.Popen(['tmux', 'new-session', '-d', '-s', 'Proxy', 'java -Xms1G -Xmx1G -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar velocity.jar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
def startServer(serverPath, serverName):
    rootPath = os.getcwd()
    os.chdir(serverPath)
    print("Starting " + serverName + " server...")
    subprocess.Popen(['tmux', 'new-session', '-d', '-s', serverName, 'java -jar fabric-server-launch.jar nogui'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
    os.chdir(rootPath)
    
    
PIDs = []
rootPath = os.getcwd()
startProxy()
os.chdir(rootPath)
with open('serverList.json', 'r') as serverListFile:
    data = json.load(serverListFile)
    for serverName in data:
        startServer('Servers/' + serverName, serverName)
        
        