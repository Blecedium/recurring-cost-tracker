import json
import config


"""
Lädt die Verträge aus der JSON-Datei. 
Falls die Datei noch nicht exisitert, wird eine leere Liste zurückgegeben.
"""
def daten_laden():
    try:
        with open(config.DATEI_PFAD, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]


"""
Speichert die aktuelle Liste der Verträge in der JSON Datei
"""
def daten_speichern(vertraege):
    with open(config.DATEI_PFAD, "w", encoding="utf-8") as datei:
        json.dump(vertraege, datei,  indent=4, ensure_ascii=False)