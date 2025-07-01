import subprocess
import os

def startProxy():
    os.chdir('Proxy')
    
    subprocess.run(['java', '-jar', 'velocity.jar'])
    
    
startProxy()