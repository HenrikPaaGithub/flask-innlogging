# Flask Innloggingssystem

Dette er et enkelt innloggingssystem bygget med Flask og MariaDB. Systemet lar brukere registrere seg, logge inn og ut, med sikker passordhåndtering og databaseintegrasjon.

## Funksjoner

- Brukerregistrering med validering
- Sikker innlogging med passordhashing
- Responsivt og moderne brukergrensesnitt
- Databaseintegrasjon med MariaDB
- Flash-meldinger for brukerfeedback
- Beskyttede ruter som krever innlogging

## Teknisk Stack

- **Backend**: Flask 3.0.2
- **Database**: MariaDB
- **ORM**: SQLAlchemy
- **Autentisering**: Flask-Login
- **Passordhåndtering**: Werkzeug
- **Frontend**: HTML5, CSS3

## Installasjon

1. Klon repositoriet:
```bash
git clone [repository-url]
cd flask-innlogging
```

2. Installer avhengigheter:
```bash
pip install -r requirements.txt
```

3. Opprett MariaDB-database:
```sql
CREATE DATABASE innlogging_db;
CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'flask_password';
GRANT ALL PRIVILEGES ON innlogging_db.* TO 'flask_user'@'localhost';
FLUSH PRIVILEGES;
```

4. Opprett `.env`-fil i prosjektmappen:
```
SECRET_KEY=din-hemmelige-nøkkel-her
DATABASE_URL=mysql://flask_user:flask_password@localhost/innlogging_db
```

5. Start applikasjonen:
```bash
python3 app.py
```

## Prosjektstruktur

```
flask-innlogging/
├── app.py              # Hovedapplikasjon
├── requirements.txt    # Python-avhengigheter
├── .env               # Miljøvariabler
└── templates/         # HTML-maler
    ├── home.html      # Hjemmeside
    ├── login.html     # Innloggingsside
    └── register.html  # Registreringsside
```

## Sikkerhet

- Passord hashes med Werkzeug's sikre hashing-funksjon
- SQL-injection beskyttelse gjennom SQLAlchemy
- CSRF-beskyttelse inkludert i Flask
- Sikker sesjonshåndtering med Flask-Login

## Design

Applikasjonen har et moderne og responsivt design med:
- Konsistent fargepalett
- Responsivt layout som fungerer på alle skjermstørrelser
- Moderne typografi og spacing
- Interaktive hover-effekter
- Tydelige feilmeldinger og feedback
- Tilgjengelighetsfunksjoner som autocomplete

## Bruk

1. Åpne `http://localhost:5000` i nettleseren
2. Registrer en ny bruker på `/register`
3. Logg inn med dine opplysninger på `/login`
4. Se velkomstsiden på `/`
5. Logg ut på `/logout`

## Utvikling

For å utvikle videre på prosjektet:
1. Aktiver debug-modus i `app.py`
2. Endre miljøvariabler i `.env`
3. Modifiser databasemodellen i `app.py`
4. Oppdater HTML-maler i `templates/`

## Lisens

Dette prosjektet er lisensiert under MIT-lisensen. 