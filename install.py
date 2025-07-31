from subprocess import Popen, PIPE, STDOUT, run
import requests
import urllib.request
import os
import shutil

def installServer(serverName, game_version, server_port):
    current_dir = os.getcwd()
    file_path = "Servers/" + serverName
    # Create main server directory and change the working directory
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    os.chdir(file_path)
    
    
    # Downloads the fabric installer from their website
    installerName = 'fabric-installer.jar'
    with urllib.request.urlopen('https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.3/fabric-installer-1.0.3.jar') as f:
        with open(installerName, 'wb') as file:
            file.write(f.read())
    
    # Install the fabric and minecraft server
    run(['java', '-jar', installerName, 'server', '-downloadMinecraft', '-mcversion', game_version])
    
    
    ## The eula.txt and properties file need to be created before the server is launched so the server does not crash when starting the first time.
    ## As I understand it the fabric server is meant to crash the first time as it creates the eula.txt and server.properties and all other files, so the user can change them and then start the server again.
    ## The code here is meant to not make the server crash the first launch
    # Creates eula file so server can start
    with open('eula.txt', 'w+') as file:
        file.write('eula=True')
    
    with open('../../default.properties', 'r+') as serverFile:
        data = serverFile.readlines()
        print(data)
        
        for idx, line in enumerate(data):
            if (line.split('=')[0] == 'server-port'):
                line = 'server-port=' + server_port + '\n'
                data[idx] = line
                break

        # file.write(''.join(data))
        with open('server.properties', 'w') as propertiesFile:
            propertiesFile.write(''.join(data))
        print(data)
    
    print(os.getcwd())
    if not os.path.exists('config'):
         os.makedirs('config')
         
    fabricProxySecret = ''
    with open('../../Proxy/forwarding.secret', 'r') as forwardingFile:
        fabricProxySecret = forwardingFile.read()
    with open('../../configs/FabricProxy-Lite.toml', 'r') as proxyFile:
        data = proxyFile.readlines()
        
        for idx, line in enumerate(data):
            if (line.split('=')[0] == 'secret '):
                
                line = 'secret = "' + fabricProxySecret + '"\n'
                data[idx] = line
                break

        with open('config/FabricProxy-Lite.toml', 'w') as newProxyFile:
            newProxyFile.write(''.join(data))
        
    os.chdir(current_dir)
    
def installProxy():
    currentDir = os.getcwd()
    os.chdir(currentDir + '/Proxy')
    run(['java', '-Xms1G', '-Xmx1G', '-XX:+UseG1GC', '-XX:G1HeapRegionSize=4M', '-XX:+UnlockExperimentalVMOptions', '-XX:+ParallelRefProcEnabled', '-XX:+AlwaysPreTouch', '-XX:MaxInlineLevel=15', '-jar', 'velocity.jar'], input='end \n'.encode())
                
    os.chdir(currentDir)