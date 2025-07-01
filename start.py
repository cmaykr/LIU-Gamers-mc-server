import subprocess
import requests
import urllib.request
import os
import install

def startServer():         
    subprocess.run(['java', '-jar', 'fabric-server-launch' + '.jar', 'nogui'])
    
current_dir = os.getcwd()
print("Current directory" +  current_dir)
if not os.path.exists('Server/main'):
    install.installServer()
    
# with open(current_dir + '/Proxy/forwarding.secret', 'r') as file:
#     secret = file.read()
#     print("Secret: " + secret)
        
#     data = ""
#     with open(current_dir + '/Servers/main/config/FabricProxy-Lite.toml', 'r') as dstfile:
#         data = dstfile.readlines()
#     with open(current_dir + '/Servers/main/config/FabricProxy-Lite.toml', 'w') as dstfile:
#         print(data)
#         for idx, line in enumerate(data):
#             print(line)
#             if (line.split('=')[0] == 'secret '):
#                 print(idx)
#                 line = 'secret = ' + secret
#                 data[idx] = line
        
#         dstfile.write(''.join(data))

startServer()

    

