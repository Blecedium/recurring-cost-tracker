"""
Zentrale Texte und Tabellen-Ausgaben für die Konsole
"""

#1. Wiederkehrende Text-Variablen
MSG_KEINE_VERTRAEGE = "Keine Verträge vorhanden"
MSG_UNGUELTIGE_EINGABE = "Ungültige Eingabe"
MSG_ZURUECK_MENU = "\n Drücke [Enter], um zum Hauptmenü zurückzukehren ..."

#2. Funktionen Willkommensmeldung beim PRogrammstart
def zeige_willkommen():
    print("=" * 55)
    print("WILLKOMMEN BEIM RECURRING COST TRACKER")
    print("Verwalte deine laufenden Fixkosten, behalte dein Budget")
    print("=" * 55 + "\n")

#3. Funktion für die einheitliche Tabellenausgabe
def zeige_tabelle(vertraege):
    print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
    print("=" * 70)
    for vertrag in vertraege:
        print(f"{vertrag['id']:<4} | {vertrag['name']:<15} | {vertrag['kategorie']:<12} | "
            f"{vertrag['betrag']:<7.2f} CHF | {vertrag['frist_tage']:<4} Tage | {vertrag['notiz']}"
        )