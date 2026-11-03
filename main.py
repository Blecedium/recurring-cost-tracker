"""
Recurring Cost Tracker - Hauptprogramm

Zur Steuerung der Konsole und für den Kontrollfluss.
"""

import json

DATEI_PFAD = "vertraege.json"

def daten_laden():
    """Lädt die Verträge aus der JSON-Datei.
    Falls die Datei noch nicht exisitert, wird eine leere Liste zurückgegeben.
    """
    try:
        with open(DATEI_PFAD, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

def daten_speichern(vertraege):
    """Speichert die aktuelle Liste der Verträge in der JSON Datei"""
    with open(DATEI_PFAD, "w", encoding="utf-8") as datei:
        json.dump(vertraege, datei,  indent=4, ensure_ascii=False)


def uebersicht_anzeigen(vertraege):
    """US-02 Formatierte Tabellenanzeige aller Verträge"""
    print("\n--- GESAMTÜBERSICHT ALLER VERTRÄGE ---")
    if not vertraege:
        print("Keine Verträge vorhanden.")
        return

    print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
    print("=" * 70)
    for v in vertraege:
        print(f"{v['id']:<4} | {v['name']:<15} | {v['kategorie']:<12} | {v['betrag']:<7.2f} CHF | {v['frist_tage']:<4} Tage | {v['notiz']}")

def kategorie_filtern(vertraege):
    #US-07: Nach Kategorie filtern

    print("\n---Nach Kategorie filtern---")
    if len(vertraege) == 0:
        print("Keine Verträge vorhanden.")
        return
    
#Leere Liste & keine Duplikate
    kategorien = []
    for vertrag in vertraege:
        if vertrag ["kategorie"] not in kategorien:
            kategorien.append(vertrag["kategorie"])

#Verfügbare Kategorien angeben
    print("Verfügbare Kategorien")
    zaehler = 1
    for kat in kategorien:
        print(f" {zaehler}: {kat}")
        zaehler += 1
# Benutzereingabe &amp; Umrechnung auf Listen-Index 
    eingabe = input(f"Bitte wähle eine Kategorie (1-{len(kategorien)}): ").strip()
    index = int(eingabe) - 1
    gewaehlte_kat = kategorien[index]

# Gefundene Verträge in neuer Liste sammeln
    gefundene = []
    for vertrag in vertraege:
           if vertrag ["kategorie"] == gewaehlte_kat:
            gefundene.append(vertrag)

# Ergebnisse
    print(f"---verträge in Kategorie '{gewaehlte_kat}' ---")
    print(f"{'ID':<4} / {'Name': <15} / {'Betrag':<10} / {'Frist': <8}")
    print("=" * 70)
    for vertraeg in gefundene:
            print(f"{vertraeg['id']:<4} | {vertraeg['name']:<15} | {vertraeg['betrag']:<7.2f} CHF")
            

def vertrag_löschen(vertraege):
    """US-09: Löscht einen Vertrag nach ID."""
    print("\n--- VERTRAG LÖSCHEN ---")
    try:
        ziel_id = int(input("Gebe die ID des zu löschenden Vertrages ein: "))
    except ValueError:
        print("Ungültige ID-Eingabe!")
        return

    for v in vertraege:
        if v["id"] == ziel_id:
            bestätigung = (input(f"Möchtest du '{v['name']}' wirklich löschen? (j/n): ") 
            .strip()
            .lower())
            if bestätigung == "j":
                vertraege.remove(v)
                print("Vertrag erfolgreich gelöscht.")
            else:
                print("Löschen abgebrochen.")
            return
    print(f"Vertrag mit ID {ziel_id} nicht gefunden.")



def show_menu():
    """Gibt ein Menu in der Konsole aus"""
    print("=" * 35)
    print("   RECURRING COST TRACKER")
    print("=" * 35)
    print("1: Neuen Vertrag erfassen")
    print("2: Gesamtübersicht anzeigen")
    print("3: Vertrag bearbeiten")
    print("4: Vertrag löschen")
    print("5: Nach Kategorie filtern")
    print("6: Monatskosten und Budget prüfen")
    print("7: Kurze Kündigungsfristen anzeigen")
    print("0: Programm beenden")
    print("=" * 35)

def main():
    """Steuerung der Konsole"""
    print("Willkommen beim Recurring Cost Tracker")

    running =True
    while running:
        show_menu()
        choice = input("Bitte wähle eine Option (0-7): ")

        if choice == "1":
            print("-> [In Arbeit] Vertrag neu erfassen...")
        elif choice == "2":
            print("-> [In Arbeit] Gesamtübersicht anzeigen...")
        elif choice == "3":
            print("-> [In Arbeit] Vertrag bearbeiten...")
        elif choice == "4":
            print("-> [In Arbeit] Vertrag löschen...")
        elif choice == "5":
            print("-> [In Arbeit] Nach Kategorie filtern...")
        elif choice == "6":
            print("-> [In Arbeit] Monatskosten und Budget prüfen...")
        elif choice == "7":
            print("-> [In Arbeit] Kurze Kündigungsfristen anzeigen...")
        elif choice == "0":
            print("Programm wird beendet. Tschüss!")
            running = False
        else:
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 0 bis 7 wählen!")

if __name__ == "__main__":
    main()

