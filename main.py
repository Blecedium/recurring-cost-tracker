"""
Recurring Cost Tracker - Hauptprogramm

Zur Steuerung der Konsole und für den Kontrollfluss.
"""

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