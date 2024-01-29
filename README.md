# Handhabung des Basic WSGI Packages

## Lege eine virtuelle Python-Umgebung an

```
python3 -m venv {myvenv}
```

## Aktiviere die virtuelle Umgebung

```
cd {myvenv}
source ./bin/activate
```

## Checke das Package aus

```
git clone https://github.com/kraeks/wsgi_base.git
```

## Installiere die Abhängigkeiten

```
cd wsgi_base
pip install -r requirements.txt
```

## Teste die Webapps

```
uwsgi --http :8000 --wsgi-file {appfile.py}
```

## Check der Datenbankeinträge für Übungen mit SQLite3

```
sqlite3 user_data.db
SELECT * FROM users;
.quit
```

