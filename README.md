# GUIDA PER I VOLONTARI BOT ITALIA

Il bot scarica in automatico le coordinate all'avvio e l'immagine con un controllo ogni 5 minuti (che riavvia il bot).  
Inoltre c'è un setup iniziale in cui crea il file di configurazione facendo delle domande al primo avvio.

## FAQ

### Mi si è piantato su `main:set_pixel_and_check_ratelimit:220`

Il bot è partito stai tranquillo, succede ad alcuni e stiamo cercando di capire ma per noi il bot funziona (verifica di usare l'ultima versione).

### Account multipli

Se volete usare più di un account potete modificare il file config.json **dopo il primo avvio** e seguire le istruzioni che trovate su https://github.com/rdeepak2002/reddit-place-script-2022.  
Cn gli account multipli è il caso di usare dei proxy se vi blocca, guardate il link.

### Come mette i pixel

C'è un parametro che permette di configurare nel file di configurazione da dove deve controllare i pixel, parte di base da `0,0` e poi ogni volta verifica se per strada incontra pixel sbaglaiti e corregge.  
Con il link sopra trovate maggiori informazioni, suggerisce negli account multipli di far controlalre seizioni diverse.

### Per chi ha la 2FA

Il bot non funziona con quella!

### Per chi accede da social login

Dovete vedere l'username che usate e impostare una password dentro Reddit!

### Mi dice Rate limit

Normale, il bot ha bisogno di tempo e il browser non si aggiorna in tempo reale al millisecondo. Lasciatelo stare, al limite riavviatelo.

### Sono su Windows ma mi dice errore alias

Noi usiamo il comando `python` probabilmente hai `python3` quindi vedi di aggiungere un alias.

## Installare

### PASSO 1

#### Windows

- Scaricare e installare Python da questo link: https://www.python.org/ftp/python/3.10.3/python-3.10.3-amd64.exe
- Scaricare questo progetto da pulsante verde in alto a destra, poi Download Zip e estraete il contenuto. Per eventuali aggiornamenti del bot (non dell'overlay) questo passaggio andrà ripetutto

### Linux

Minimo Python 3.9!

- `apt install python3 python3-pip`     - debian/ubuntu
- `yum install python3 python3-pip`     - redhat/centos/fedora
- `pacman -S python3 python3-pip`       - arch/manjaro
- `xbps-install -S python3 python3-pip` - void 

### PASSO 2

Mentre l'installazione avanza, aprire questo link: https://www.reddit.com/prefs/apps

- Cliccare su are you a developer? create an app...
- Inserire ciò che si vuole in name e description.
- Selezionare il bottone SCRIPT (non web/app)
- Inserire http://google.com/ su redirect uri.
- Potete lasciare bianco l'altro link.
- Cliccare su create app.
- TENERE APERTA QUESTA PAGINA PER IL PASSO 3!!!

### PASSO 3

- Estrarre lo zip qui sotto (tutto nella stessa cartella) e lanciare il file start.bat
- Inserire Username di Reddit.
- Inserire Password di Reddit.
- L'ID creato al passo 2 sta sotto la scritta "personal use script".
- Il Secret creato al passo 2 sta a sinistra della scritta "secret".

#### Windows

Cliccate su `start.bat` vi apre una finestra da lasciare aperta

#### Linux

Da terminale lanciate `start.sh`, per chi vuole c'è il Dockerfile già pronto (con questo comando evitiamo che muoia). 


#### Docker

Costruite l'immagine lanciando il comando seguente dalla directory in cui si trova Dockerfile:

```
docker build . -t place-bot
```
fate partire un nuovo container lanciando il comando:

```
docker run -d --restart unless-stopped place-bot
```
