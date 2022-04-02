import os.path
import requests
import filecmp
import shutil
import subprocess
import time

if os.path.exists("config.json") == False:
    username=input("Username di Reddit: ")
    password=input("Password di Reddit: ")
    client_ID=input("ID creato al passo 2: ")
    client_secret=input("Secret creato al passo 2: ")
    f=open("config.json","a")
    f.write('{"thread_delay": 2,"unverified_place_frequency": false,"workers": {"')
    f.write(username)
    f.write(' ": {"password": "')
    f.write(password)
    f.write('","client_id": "')
    f.write(client_ID)
    f.write('","client_secret": "')
    f.write(client_secret)
    f.write('","start_coords":')
    f.write('[0, 0]')
    f.write('}}}')
    f.close()


def run():
    print("Script launched")
    process = subprocess.Popen(args=["python", "./main.py"], stdout=subprocess.PIPE)
    return process

exec(open('main.py').read())
process = run()

# verifica ogni minuti
t_end = time.time() + 60 * 10
while time.time() < t_end:
    url = 'https://raw.githubusercontent.com/italyplace/rplace/main/art.png1'
    r = requests.get(url, allow_redirects=True)
    open('ntemp.bin', 'wb').write(r.content)
    if not filecmp.cmp('ntemp.bin', 'temp.bin'):
        print("Update found!")
        shutil.copyfile('ntemp.bin', 'temp.bin')
        process.terminate()
        process = run()

