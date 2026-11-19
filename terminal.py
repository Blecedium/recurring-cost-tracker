"""
Hilfsfunktionen für die Benutzeroberfläche und Textausgaben
"""


import os
import subprocess
import time


def clear_screen():
    """
    Funktion um das Terminal zu leeren
    """
    command = "cls" if os.name =="nt" else "clear"
    subprocess.run(command, shell=True)
    print("\n")


def show_menu():
    """
    Gibt das Menu in der Konsole aus
    """
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
    print("8: Kostensortierung")
    print("0: Programm beenden")
    print("=" * 35)


def wait_2s():
    """
    Lässt das Terminal 2 Sek. warten
    """
    time.sleep(2)


def wait_4s():
    """
    Lässt das Terminal 4 Sek. warten
    """
    time.sleep(2)


# Wiederkehrende Text-Variablen
MSG_KEINE_VERTRAEGE = "\nKeine Verträge vorhanden."
MSG_UNGUELTIGE_EINGABE = "\nUngültige Eingabe."
MSG_ZURUECK_MENU = "\n Drücke [Enter], um zum Hauptmenü zurückzukehren..."


# Willkommens Nachricht
def zeige_willkommen():
    print("=" * 55)
    print("WILLKOMMEN BEIM RECURRING COST TRACKER")
    print("Verwalte deine laufenden Fixkosten, behalte dein Budget")
    print("=" * 55 + "\n")


# Einheitliche Tabellenausgabe
def zeige_tabelle(vertraege):
    print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
    print("=" * 70)
    for vertrag in vertraege:
        print(f"{vertrag['id']:<4} | {vertrag['name']:<15} | {vertrag['kategorie']:<12} | "
            f"{vertrag['betrag']:<7.2f} CHF | {vertrag['frist_tage']:<4} Tage | {vertrag['notiz']}"
        )