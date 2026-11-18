"""
Hilfsfunktionen für die Benutzeroberfläche
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