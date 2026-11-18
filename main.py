"""
Recurring Cost Tracker - Hauptprogramm
"""

import calculations
import contracts
import search_filter
import storage
import terminal



def main():
    """
    Zur Steuerung der Konsole und für den Kontrollfluss.
    """
    print("Willkommen beim Recurring Cost Tracker")
    print("Verwalte deine Fixkosten, Kündigungsfristen und behalte dein Budget im Blick.\n")

    vertraege = storage.daten_laden()
    calculations.ablauf_erinnerung_pruefen(vertraege)

    running = True
    while running:
        terminal.show_menu()
        choice = input("Bitte wähle eine Option (0-8): ")

        if choice == "1":
            contracts.vertrag_erfassen(vertraege)
        elif choice == "2":
            contracts.uebersicht_anzeigen(vertraege)
        elif choice == "3":
            contracts.vertrag_bearbeiten(vertraege)
        elif choice == "4":
            contracts.vertrag_löschen(vertraege)
        elif choice == "5":
            search_filter.kategorie_filtern(vertraege)
        elif choice == "6":
            calculations.monatsauswertung_anzeigen(vertraege)
        elif choice == "7":
            search_filter.kurze_fristen_anzeigen(vertraege)
        elif choice == "8":
            search_filter.kosten_sortieren(vertraege)
        elif choice == "0":
            print("Programm wird beendet. Tschüss!")
            storage.daten_speichern(vertraege)
            running = False
        else:
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 0 bis 8 wählen!")
            terminal.wait_2s()

if __name__ == "__main__":
    main()