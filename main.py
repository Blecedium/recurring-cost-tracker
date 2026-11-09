"""
Recurring Cost Tracker - Hauptprogramm
Zur Steuerung der Konsole und für den Kontrollfluss.
"""

import json
import os
import subprocess
import time
from calculations import (
    ablauf_erinnerung_pruefen,
    monatsueberblick_anzeigen,
    monatsbetrag_berechnen,
    budget_pruefen
)


"""
Stellt die Importierte json zur Verfügung
"""
DATEI_PFAD = "vertraege.json"


"""
Lädt die Verträge aus der JSON-Datei. Falls die Datei noch nicht exisitert, wird eine leere Liste zurückgegeben.
"""
def daten_laden():
    try:
        with open(DATEI_PFAD, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]


"""
Speichert die aktuelle Liste der Verträge in der JSON Datei
"""
def daten_speichern(vertraege):
    with open(DATEI_PFAD, "w", encoding="utf-8") as datei:
        json.dump(vertraege, datei,  indent=4, ensure_ascii=False)


"""
Funktion um das Terminal zu leeren
"""
def clear_screen():
    command = "cls" if os.name =="nt" else "clear"
    subprocess.run(command, shell=True)


"""
US-01 Erfässt einen Vertrag und fügt diesen der Liste hinzu
"""
def vertrag_erfassen(vertraege):
    clear_screen()
    print("\n--- NEUEN VERTRAG ERFASSEN ---")

 # Fortlaufende ID erstellen
    neue_id = max([v['id'] for v in vertraege], default=0) + 1

# Erfassen des Namen
    name = input("Name des Vertages / Abo: ").strip()
    while not name:
        print("Der Name darf nicht leer sein!")
        name = input("Name des Vertrages / Abo: ").strip()

# Erfassen der Kategorie
    kategorie = input("Kategorie (z.B. Streaming, Krankenkasse) [Standard: Sonstiges]: ").strip().capitalize()
    if not kategorie:
        kategorie = "Sonstiges"

 # Betrag erfassen
    while True:
        try:
            betrag_eingabe = input("Betrag in CHF (z.B. 17.90): ").strip()
            betrag = float(betrag_eingabe)
            if betrag <= 0:
                print("Ungültiger Betrag! Bitte positive Zahl eingeben.")
            else:
                break
        except ValueError:
            print("Ungültiger Betrag! Bitte positive Zahl eingeben.")

# Zahlungsrythmus erfassen
    rhythmus = input("Zahlungsrhythmus (monatlich / jährlich) [Standard: monatlich]: ").strip().lower()
    if rhythmus not in ["monatlich", "jährlich", "jaehrlich"]:
        rhythmus = "monatlich"

    # Ablaufdatum erfassen (optional)
    ablaufdatum = input("Ablaufdatum (YYYY-MM-DD, z.B. 2026-12-13) [optional]: ").strip()

# Kündigungsfrist in Tagen angeben
    while True:
        try:
            frist_eingabe = input("Kündigungsfrist in Tagen (z.B. 60) [Standard: 30]: ").strip()
            if not frist_eingabe:
                frist_tage = 30
                break
            frist_tage = int(frist_eingabe)
            if frist_tage <0:
                print("Bitte gültige Tageszahl (>=0) angeben!")
            else:
                break
        except ValueError:
            print("Ungültige Eingabe!")

# Notitz erfassen (optional)
    notiz = input("Kurze Notitz (z.B. Kundennummer) [optional]: ").strip()

# Vertrag dem Dictionarie hinzufügen
    neuer_vertrag = {
        "id": neue_id,
        "name": name,
        "kategorie": kategorie,
        "betrag": betrag,
        "rhythmus": rhythmus,
        "ablaufdatum": ablaufdatum,
        "frist_tage": frist_tage,
        "notiz": notiz,
    }

    vertraege.append(neuer_vertrag)
    print(f"Vertrag {name} erfolgreich erfasst.")
    time.sleep(2)
    

"""
US-02 Formatierte Tabellenanzeige aller Verträge
"""
def uebersicht_anzeigen(vertraege):
    clear_screen()
    print("\n--- GESAMTÜBERSICHT ALLER VERTRÄGE ---")
    if not vertraege:
        print("Keine Verträge vorhanden.")
        time.sleep(2)
        return

# Verträge in einer Liste mit Überschriften ausgeben
    print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
    print("=" * 70)
    for v in vertraege:
        print(f"{v['id']:<4} | {v['name']:<15} | {v['kategorie']:<12} | {v['betrag']:<7.2f} CHF | {v['frist_tage']:<4} Tage | {v['notiz']}")

# Warten auf Input
    input("\nDrücke [Enter], um zum Hauptmenü zurückzukehren...")

#USer Story 4: Startalert vor dem Hauptmenü
ablauf_erinnerung_pruefen(vertraege)
running = True
while running:
    show_menu()
    choice = input("Bitte wähle eine Option (0-7:) ").strip()
    if choice =="1":
        pass
    elif choice == "2":
        print("-> [In Arbeit / User Story 2] Stamm-Tabelle anzeigen...")
    elif choice == "3":
 #User Story 5
        monatsueberblick_anzeigen(vertraege)
    elif choice == "4":
#User Story 6
        gesamtkosten =0.0
        for v in vertraege:
            gesamtkosten += monatsbetrag_berechnen(v["betrag"], v["rhythmus"])
        print(f"\nAktuelle Monatskosten: CHF {gesamtkosten:.2f}")
        print(f"Maximalbudget CHF {max_budget:.2f}")
        budget_pruefen(vertraege, max_budget)
        print()
    elif choice == "0":
        running = False
    else:
        print("Ungültige Eingabe!")

"""
US-07: Nach Kategorie filtern
"""
def kategorie_filtern(vertraege):
    clear_screen()
    print("\n--- NACH KATEGORIEN FILTERN ---")
    if not vertraege:
        print("Keine Verträge vorhanden.")
        time.sleep(2)
        return
    
# Leere Liste & keine Duplikate
    kategorien = []
    for vertrag in vertraege:
        if vertrag ["kategorie"] not in kategorien:
            kategorien.append(vertrag["kategorie"])

# Verfügbare Kategorien angeben
    print("Verfügbare Kategorien")
    zaehler = 1
    for kat in kategorien:
        print(f" {zaehler}: {kat}")
        zaehler += 1

# Benutzereingabe & Umrechnung auf Listen-Index 
    eingabe = input(f"Bitte wähle eine Kategorie (1-{len(kategorien)}): ").strip()
    try:
        index = int(eingabe) - 1
        if index < 0:
            raise IndexError
        gewaehlte_kat = kategorien[index]
    except (ValueError, IndexError):
        print("Ungültige Auswahl! Bitte eine gültige Zahl aus der Liste eintragen.")
        time.sleep(2)
        return

# Gefundene Verträge in neuer Liste sammeln
    gefundene = []
    for vertrag in vertraege:
           if vertrag ["kategorie"] == gewaehlte_kat:
            gefundene.append(vertrag)

# Ergebnisse in einer Liste ausgeben
    clear_screen()
    print(f"--- Verträge in Kategorie '{gewaehlte_kat}' ---")
    print(f"{'ID':<4} | {'Name':<15} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
    print("=" * 55)
    for v in gefundene:
            print(f"{v['id']:<4} | {v['name']:<15} | {v['betrag']:<7.2f} CHF | {v['frist_tage']:<4} Tage | {v['notiz']}")

# Warten auf Input
    input("\nDrücke [Enter], um zum Hauptmenü zurückzukehren...")


"""
US-09: Löscht einen Vertrag nach ID
"""
def vertrag_löschen(vertraege):
    clear_screen()
    print("\n--- VERTRAG LÖSCHEN ---")
    if not vertraege:
            print("Keine Verträge vorhanden.")
            time.sleep(2)
            return

# Übersicht aller Verträge anzeigen
    print("\nVorhandene Verträge:")
    for v in vertraege:
        print(f" ID {v['id']}: {v['name']} | Notiz: {v['notiz']}")
    print("=" * 35)

# Prüfung Eingabe (Zahl)    
    try:
        ziel_id = int(input("Gebe die ID des zu löschenden Vertrages ein: "))
    except ValueError:
        print("Ungültige ID-Eingabe!")
        time.sleep(2)
        return

# Prüfung eingegebene Zahl & bei gültigkeit löschung Vertrag
    for v in vertraege:
        if v["id"] == ziel_id:
            bestätigung = (input(f"Möchtest du '{v['name']}' wirklich löschen? (j/n): ").strip().lower())
            if bestätigung == "j":
                vertraege.remove(v)
                print("Vertrag erfolgreich gelöscht.")
                time.sleep(2)
            else:
                print("Löschen abgebrochen.")
                time.sleep(2)
            return
    print(f"Vertrag mit ID {ziel_id} nicht gefunden.")
    time.sleep(2)


"""
Gibt ein Menu in der Konsole aus
"""
def show_menu():
    clear_screen()
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


"""
Steuerung der Konsole bzw. dem Menu
"""
def main():

    print("Willkommen beim Recurring Cost Tracker")
    vertraege = daten_laden()

    running = True
    while running:
        show_menu()
        choice = input("Bitte wähle eine Option (0-7): ")

        if choice == "1":
            vertrag_erfassen(vertraege)
            daten_speichern(vertraege)
        elif choice == "2":
            uebersicht_anzeigen(vertraege)
        elif choice == "3":
            print("-> [In Arbeit] Vertrag bearbeiten...")
        elif choice == "4":
            vertrag_löschen(vertraege)
            daten_speichern(vertraege)
        elif choice == "5":
            kategorie_filtern(vertraege)
        elif choice == "6":
            print("-> [In Arbeit] Monatskosten und Budget prüfen...")
        elif choice == "7":
            print("-> [In Arbeit] Kurze Kündigungsfristen anzeigen...")
        elif choice == "0":
            print("Programm wird beendet. Tschüss!")
            daten_speichern(vertraege)
            running = False
        else:
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 0 bis 7 wählen!")

if __name__ == "__main__":
    main()