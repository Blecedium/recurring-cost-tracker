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
    terminal.clear_screen()
    terminal.zeige_willkommen()


    vertraege = storage.daten_laden()

    # US-04: Erinnerung vor dem Menu anzeigen
    hat_warnung = calculations.ablauf_erinnerung_pruefen(vertraege)
    if hat_warnung:
        terminal.pause_enter()
    else:
        terminal.wait_4s()

    while True:
        terminal.show_menu()
        choice_input = input("Bitte wähle eine Option (0-5): ").strip()
        try:
            choice = int(choice_input)
        except ValueError:
            print(terminal.MSG_MENU_ZAHLEN_UNGUELTIG)
            terminal.wait_2s()
            continue

        if choice == 1:
            contracts.vertrag_erfassen(vertraege)
        elif choice == 2:
            search_filter.untermenu_anzeigen(vertraege)
        elif choice == 3:
            contracts.vertrag_bearbeiten(vertraege)
        elif choice == 4:
            contracts.vertrag_loeschen(vertraege)
        elif choice == 5:
            calculations.monatsauswertung_anzeigen(vertraege)
        elif choice == 0:
            print("Programm wird beendet. Tschüss!")
            storage.daten_speichern(vertraege)
            break
        else:
            print(terminal.MSG_MENU_ZAHLEN_UNGUELTIG)
            terminal.wait_2s()

if __name__ == "__main__":
    main()