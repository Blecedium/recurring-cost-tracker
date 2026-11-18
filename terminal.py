import os
import subprocess
import time


"""
Funktion um das Terminal zu leeren
"""
def clear_screen():
    command = "cls" if os.name =="nt" else "clear"
    subprocess.run(command, shell=True)
    print("\n")


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
    print("8: Kostensortierung")
    print("0: Programm beenden")
    print("=" * 35)


"""
Lässt das Terminal 2 Sek. warten
"""
def wait_2s():
    time.sleep(2)