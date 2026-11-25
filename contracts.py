"""
Vertragsverwaltung und bearbeitung
"""
import terminal
import storage


def vertrag_erfassen(vertraege):
    """
    US-01 Erfässt einen Vertrag und fügt diesen der Liste hinzu
    """
    terminal.clear_screen()
    terminal.zeige_titel("Neuen Vertrag erfassen")

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
                print(terminal.MSG_POSITIVE_ZAHL)
            else:
                break
        except ValueError:
            print(terminal.MSG_POSITIVE_ZAHL)

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
                print(terminal.MSG_POSITIVE_ZAHL)
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
    storage.daten_speichern(vertraege)
    print(f"Vertrag {name} erfolgreich erfasst.")
    terminal.wait_2s()


def uebersicht_anzeigen(vertraege):
    """
    US-02 Formatierte Tabellenanzeige aller Verträge
    """
    terminal.clear_screen()
    terminal.zeige_titel("Gesamtübersicht aller Verträge")
    if not vertraege:
        print(terminal.MSG_KEINE_VERTRAEGE)
        terminal.wait_2s()
        return

# Verträge in einer Liste mit Überschriften ausgegeben
    terminal.zeige_tabelle(vertraege)

# Warten auf Input
    terminal.pause_enter()


def vertrag_bearbeiten(vertraege):
    """
    US-03 Bearbeiten eines bestehenden Vertrag
    """
    terminal.clear_screen()
    terminal.zeige_titel("Vertrag bearbeiten")

    if not vertraege:
        print(terminal.MSG_KEINE_VERTRAEGE)
        terminal.wait_2s()
        return

# Übersicht für die Aktuellen Verträge anzeigen
    terminal.zeige_tabelle(vertraege)

# Prüfung Eingabe (Zahl)
    try:
        ziel_id = int(input("Gib die ID des zu bearbeitenden Vertrag ein: "))
    except ValueError:
        print(terminal.MSG_UNGUELTIGE_EINGABE)
        terminal.wait_2s()
        return
    
    ziel = None
    for v in vertraege:
        if v["id"] == ziel_id:
            ziel = v
            break

# Prüfung eingegebene Zahl in Vertrag IDs vorhanden
    if ziel is None:
        print(f"Vertrag mit ID {ziel_id} nicht gefunden.")
        terminal.wait_2s()
        return
    print(f"\nBearbeite Vertrag '{ziel['name']}'. [Enter = alten Wert behalten]\n")

# Felder einzeln druchgehen zum bearbeiten

    # Name
    eingabe = input(f"Name [{ziel['name']}]: ").strip()
    if eingabe:
        ziel["name"] = eingabe

    # Kategorie
    eingabe = input(f"Kategorie [{ziel['kategorie']}]: ").strip().capitalize()
    if eingabe:
        ziel["kategorie"] = eingabe

    # Betrag
    while True:
        eingabe = input(f"Betrag in CHF [{ziel['betrag']:.2f}]: ").strip()
        if not eingabe:
            break
        try:
            neuer_betrag = float(eingabe)
            if neuer_betrag <= 0:
                print(terminal.MSG_POSITIVE_ZAHL)
            else:
                ziel['betrag'] = neuer_betrag
                break
        except ValueError:
            print(terminal.MSG_POSITIVE_ZAHL)

    # Zahlungsrythmus (monatlich / jährlich)
    eingabe = input(f"Zahlungsrythmus [{ziel['rhythmus']}]: ").strip().lower()
    if eingabe in ["monatlich", "jährlich", "jaehrlich"]:
        ziel['rhythmus'] = eingabe

    # Ablaufdatum
    eingabe = input(f"Ablaufdatum [{ziel['ablaufdatum']}]: ").strip()
    if eingabe:
        ziel["ablaufdatum"] = eingabe

    # Kündigungsfrist
    while True:
        eingabe = input(f"Kündigungsfrist in Tagen [{ziel['frist_tage']}]: ").strip()
        if not eingabe:
            break
        try:
            neue_frist = int(eingabe)
            if neue_frist < 0:
                print(terminal.MSG_POSITIVE_ZAHL)
            else:
                ziel['frist_tage'] = neue_frist
                break
        except ValueError:
            print(terminal.MSG_POSITIVE_ZAHL)

    # Notiz
    eingabe = input(f"Notiz [{ziel['notiz']}]: ").strip()
    if eingabe:
        ziel['notiz'] = eingabe

    storage.daten_speichern(vertraege)
    print(f"\nVertrag '{ziel['name']}' erfolgreich aktualisiert.")
    terminal.wait_2s()


def vertrag_loeschen(vertraege):
    """
    US-09: Löscht einen Vertrag nach ID
    """
    terminal.clear_screen()
    terminal.zeige_titel("Vertrag löschen")
    if not vertraege:
            print(terminal.MSG_KEINE_VERTRAEGE)
            terminal.wait_2s()
            return

# Übersicht aller Verträge anzeigen
    print("\nVorhandene Verträge:")
    terminal.zeige_tabelle(vertraege)

# Prüfung Eingabe (Zahl)    
    try:
        ziel_id = int(input("Gebe die ID des zu löschenden Vertrages ein: "))
    except ValueError:
        print(terminal.MSG_UNGUELTIGE_EINGABE)
        terminal.wait_2s()
        return

# Prüfung eingegebene Zahl & bei gültigkeit löschung Vertrag
    for v in vertraege:
        if v["id"] == ziel_id:
            bestätigung = (input(f"Möchtest du '{v['name']}' wirklich löschen? (j/n): ").strip().lower())
            if bestätigung == "j":
                vertraege.remove(v)
                storage.daten_speichern(vertraege)
                print("Vertrag erfolgreich gelöscht.")
                terminal.wait_2s()
            else:
                print("Löschen abgebrochen.")
                terminal.wait_2s()
            return
    print(f"Vertrag mit ID {ziel_id} nicht gefunden.")
    terminal.wait_2s()