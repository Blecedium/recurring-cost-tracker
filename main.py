"""
Recurring Cost Tracker - Hauptprogramm

Zur Steuerung der Konsole und für den Kontrollfluss.
"""

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