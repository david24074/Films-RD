# Website
Alle stappen hieronder gaan ervan uit dat ze uitgevoerd worden in dezelfde folder waar deze `README.md` staat.

## Installatie
De environment folder is meegestuurd maar kan opnieuw gegenereerd worden.  
Om dit te doen verwijder je de oude `venv` folder.  
Daarna maak je een nieuwe folder aan door het volgende commando uit te voeren `py -m venv venv`.  
Dan start je de environment via `.\venv\Scripts\activate`.  
De modules die wij gebruiken kunnen vervolgens geinstalleerd worden via `pip install -r requirements.txt`.  

## Database
Wij hebben de database meegestuurd en staat in `/src/data.sqlite`.  
Deze database kan opnieuw gegenereerd worden maar zal dan geen films meer bevatten en moeten dan handmatig toegevoegd worden.  
Daarom raden wij het aan om de geleverde database te gebruiken.  

## Server starten
Als de bovenstaande stappen zijn uitgevoerd dan kan de server gestart worden door het commando `py app.py` uit te voeren.  
Doe dit wel terwijl de environment nog aan staat.  