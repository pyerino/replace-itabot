import os.path
import requests
import filecmp
import shutil
import subprocess
import time
import json

if os.path.exists("config.json") == False:
    username = input("Username di Reddit: ")
    password = input("Password di Reddit: ")
    client_ID = input("ID creato al passo 2: ")
    client_secret = input("Secret creato al passo 2: ")
    f = open("config.json", "a")
    config = {}
    config['thread_delay'] = 2
    config['unverified_place_frequency'] = False
    config['workers'] = {}
    config['workers'][username] = {
        'password': password, 'client_id': client_ID, 'client_secret': client_secret, 'start_coords': [0, 0]}
    json.dump(config, f)
    f.close()


def run():
    print("Script launched")
    process = subprocess.Popen(args=["python", "./main.py"], stdout=subprocess.PIPE)
    return process


def download_image(process=''):
    url = 'https://raw.githubusercontent.com/italyplace/rplace/main/art.png'
    r = requests.get(url, allow_redirects=True)
    open('ntemp.bin', 'wb').write(r.content)
    if not os.path.exists('temp.bin') or not filecmp.cmp('ntemp.bin', 'temp.bin'):
        print("Update found!")
        shutil.copyfile('ntemp.bin', 'temp.bin')
        # riavvio il processo quando sono nel loop
        if process != '':
            process.terminate()
            process = run()
            return process
    return process


# scarico l'immagine all'avvio per vedere se ci sono aggiornamenti
download_image()
process = run()

# verifica ogni 5 minuti per aggiornamenti
t_end = time.time() + 60 * 5
while time.time() < t_end:
    process = download_image(process)
