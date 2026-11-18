import terminal


"""
US-07: Nach Kategorie filtern
"""
def kategorie_filtern(vertraege):
    terminal.clear_screen()
    print("\n--- NACH KATEGORIEN FILTERN ---")
    if not vertraege:
        print("Keine Verträge vorhanden.")
        terminal.wait_2s()
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
        terminal.wait_2s()
        return

# Gefundene Verträge in neuer Liste sammeln
    gefundene = []
    for vertrag in vertraege:
           if vertrag ["kategorie"] == gewaehlte_kat:
            gefundene.append(vertrag)

# Ergebnisse in einer Liste ausgegeben
    terminal.clear_screen()
    print(f"--- Verträge in Kategorie '{gewaehlte_kat}' ---")
    print(f"{'ID':<4} | {'Name':<15} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
    print("=" * 55)
    for v in gefundene:
            print(f"{v['id']:<4} | {v['name']:<15} | {v['betrag']:<7.2f} CHF | {v['frist_tage']:<4} Tage | {v['notiz']}")

# Warten auf Input
    input("\nDrücke [Enter], um zum Hauptmenü zurückzukehren...")

"""
US-08 Kündigungsfrist überprüfen
"""

def kurze_fristen_anzeigen(vertraege):
    terminal.clear_screen()
    print("\n --- Verträge mit kurzer Kündigungsfrist (<= 30 TAge) ---")

    if not vertraege:
        print("Keine Verträge vorhanden.")
        terminal.wait_2s()
        return

# Filtern nach Frist <= 30 Tage

    kurze_fristen = []
    for vertrage in vertraege:
        if vertrage ["frist_tage"] <= 30:
            kurze_fristen.append(vertrage)

    if not kurze_fristen:
        print("Keine Vertrage mit kurzer Kündigungsfrist vorhanden.")
    else:
        print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Betrag':<10} | {'Frist':<8} | {'Notiz'}")
        print("="*70)

        for vertrag in kurze_fristen:
            print(f"{vertrag['id']:<4} | {vertrag['name']:<15} | {vertrag['kategorie']:<12} | {vertrag['betrag']:<7.2f} CHF | {vertrag['frist_tage']:<4} Tage | {vertrag['notiz']}")

    input("\nDrücke [Enter], um zum Hauptmenü zurückzukehren...")


"""
US-10: Vertäge nach Kosten sortieren
"""
def berechne_monatsbetrag(vertrag):
    # Jährliche Beträge durch 12 teilen, um faire Monatskosten zu erhalten
    if vertrag["rhythmus"] in ["jährlich", "jaehrlich"]:
        return vertrag["betrag"] / 12
    return vertrag["betrag"]
# Hilfsfunktion zu US-10

def kosten_sortieren(vertraege):
    terminal.clear_screen()
    print("\n--- VERTRÄGE NACH KOSTEN SORTIERT (TEUERSTE ZUERST) ---")

    # Prüfen, ob die Liste leer ist (Truthiness)
    if not vertraege:
        print("Keine Vertäge vorhanden.")
        input("\nDrücke [Enter], um zum Hauptmenü zurückzukehren...")
        return

    # Alias vs Copy: Mit slicing [:] eine echte Kopie anlegen,damit die Originale-Reihenfolge der Vertäge in vertraege nicht verändert wird.
    sortierte_vertraege = vertraege[:]

    # (Nested Loops): Verschachtelte for-Schleifen zur Sortierung
    anzahl = len(sortierte_vertraege)
    for i in range(anzahl):
        for j in range(i + 1, anzahl):
            # Monatskosten vergleichen: Ist der hintere Vertrag teuerer, Plätze tauschen
            if berechne_monatsbetrag(sortierte_vertraege[j]) > berechne_monatsbetrag(sortierte_vertraege[i]):
                temp = sortierte_vertraege[i]
                sortierte_vertraege[i] = sortierte_vertraege[j]
                sortierte_vertraege[j] = temp

    # Tabellenkop mit f-Strings formatieren (< linksbündig)
    print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Monatsbetrag':<14} | {'Notiz'}")
    print("=" * 70)
    for v in sortierte_vertraege:
        monats_chf = berechne_monatsbetrag(v)
        print(f"{v['id']:<4} | {v['name']:<15} | {v['kategorie']:<12} | {monats_chf:<10.2f} CHF | {v['notiz']}")

    # Pause via Input(), bis der Nutzer Enter drückt
    input("\nDrücke [Enter], um zum Hauptmenü zurückzukehren...")


"""
US-11: Nach dem Namen eines Abos suchen
"""