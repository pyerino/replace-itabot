# GUIDA PER I VOLONTARI BOT ITALIA

Il bot scarica in automatico le coordinate all'avvio e l'immagine con un controllo ogni 5 minuti (che riavvia il bot).  
Inoltre c'è un setup iniziale in cui crea il file di configurazione facendo delle domande al primo avvio.

**Il bot inteso come programma si aggiorna riscaricando lo zip, verificate di avere l'ultima versione se avete problemi!**

## FAQ

### Mi dice banned, moriremo tutti!

No su r/place non puoi fare un tubo, per ilresto non hai problemi.

### Mi si è piantato su `main:set_pixel_and_check_ratelimit:220` o su `Loaded image size`

Per caso usi l'accesso con Google? Verifica la password configurata che altrimenti non si collega.

### Sono su Windows la finestra si apre e si chiude

Stai usando il bot aggiornato? Hai python 3.10 installato? Hai letto il Passo 1?

### Sono su Windows ma mi dice errore alias

Noi usiamo il comando `python` probabilmente hai `python3` quindi vedi di aggiungere un alias.
Windows 11, su App --> App e funzionalità --> Altre impostazioni --> Alias di esecuzione App --> Togli la spunta da programma di installazione app (python.exe), ce ne sono 2.

### Perchè devo aspettare 20 minuti?

Il tuo account è limitato, devi attivarlo con un email per aspettare 5 minuti invece di 20.

### Account multipli

Se volete usare più di un account potete modificare il file config.json **dopo il primo avvio** e seguire le istruzioni che trovate su https://github.com/rdeepak2002/reddit-place-script-2022.  
Cn gli account multipli è il caso di usare dei proxy se vi blocca, guardate il link.

### Come mette i pixel

C'è un parametro che permette di configurare nel file di configurazione da dove deve controllare i pixel, parte di base da `0,0` e poi ogni volta verifica se per strada incontra pixel sbagliati e corregge.  
Con il link sopra trovate maggiori informazioni, suggerisce negli account multipli di far controlalre sezioni diverse.

### Per chi ha la 2FA

Il bot non funziona con quella!

### Per chi accede da social login

Dovete vedere l'username che usate e impostare una password dentro Reddit!

### Mi dice Rate limit

Normale, il bot ha bisogno di tempo e il browser non si aggiorna in tempo reale al millisecondo. Lasciatelo stare, al limite riavvialo.  
Reddit potrebbe anche limitarti perchè fanno dei controlli...

## Installare

### PASSO 1

- Scaricare questo progetto da pulsante verde in alto a destra, poi Download Zip e estraete il contenuto. Per eventuali aggiornamenti del bot (non dell'overlay) questo passaggio andrà ripetuto.

#### Windows

- Scaricare e installare Python da questo link: https://www.python.org/ftp/python/3.10.3/python-3.10.3-amd64.exe
- **Su Windows avrete problemi sicuramente perchè è Windows** leggete [questa guida](https://phoenixnap.com/kb/how-to-install-python-3-windows) e le **FAQ** prima di chiedere aiuto

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

- Lanciare il file start.bat
- Inserire Username di Reddit.
- Inserire Password di Reddit.
- L'ID creato al passo 2 sta sotto la scritta "personal use script".
- Il Secret creato al passo 2 sta a sinistra della scritta "secret".

#### Windows

Cliccate su `start.bat` vi apre una finestra da lasciare aperta

#### Linux

Da terminale lanciate `start.sh`

#### Docker

Per chi vuole c'è il Dockerfile già pronto.

Build della DOcker image:
```
docker build . -t place-bot
```

Per eseguirlo:

```
docker run -ti --restart unless-stopped place-bot
```
