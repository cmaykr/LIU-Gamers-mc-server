import subprocess
import requests
import urllib.request
import os
import shutil
import installmods

file_path = 'Servers/main'
serverName = 'server'
def installServer():
    current_dir = os.getcwd()
    print("Current directory" +  current_dir)
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
    subprocess.run(['java', '-jar', installerName, serverName, '-downloadMinecraft'])
    
    
    ## The eula.txt and properties file need to be created before the server is launched so the server does not crash when starting the first time.
    ## As I understand it the fabric server is meant to crash the first time as it creates the eula.txt and server.properties and all other files, so the user can change them and then start the server again.
    ## The code here is meant to not make the server crash the first launch
    # Creates eula file so server can start
    with open('eula.txt', 'w+') as file:
        file.write('eula=True')
       
    print(os.getcwd())
    # Cope the default properties file to the server directory 
    src = '../../default.properties'
    dst = 'server.properties'
    shutil.copyfile(src, dst)
    
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
    
    # os.chdir(current_dir)
    # installmods.installMods()
    # with open('../../Proxy/forwarding.secret', 'r') as file:
    #     secret = file.read()
        
    # with open('config/FabricProxy-Lite.toml') as file:
    #     data = file.readlines()
    #     for idx, line in enumerate(data):
    #         if (line.split('=')[0] == 'secret '):
    #             line = 'secret = ' + secret
        
    #     file.write(''.join(data))
    
# installServer()