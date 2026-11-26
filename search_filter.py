"""
Auswertungs-, Filter- und Sortierfunktionen
"""
import terminal
import contracts



def kategorie_filtern(vertraege):
    """
    US-07: Nach Kategorie filtern
    """
    terminal.clear_screen()
    terminal.zeige_titel("Nach Kategorie filtern")
    if not vertraege:
        print(terminal.MSG_KEINE_VERTRAEGE)
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
    terminal.zeige_titel(f"Verträge in Kategorie '{gewaehlte_kat}'")
    terminal.zeige_tabelle(gefundene)

# Warten auf Input
    terminal.pause_enter()


def kurze_fristen_anzeigen(vertraege):
    """
    US-08 Kündigungsfrist überprüfen
    """
    terminal.clear_screen()
    terminal.zeige_titel("Verträge mit kurzer Kündigungsfrist (<= 30 Tage)")

    if not vertraege:
        print(terminal.MSG_KEINE_VERTRAEGE)
        terminal.wait_2s()
        return

# Filtern nach Frist <= 30 Tage

    kurze_fristen = []
    for vertrag in vertraege:
        if vertrag ["frist_tage"] <= 30:
            kurze_fristen.append(vertrag)

    if not kurze_fristen:
        print("Keine Verträge mit kurzer Kündigungsfrist vorhanden.")
    else:
        terminal.zeige_tabelle(kurze_fristen)

    terminal.pause_enter()
    


def berechne_monatsbetrag(vertrag):
    """
    US-10: Vertäge nach Kosten sortieren
    """
    # Jährliche Beträge durch 12 teilen, um faire Monatskosten zu erhalten
    if vertrag["rhythmus"] in ["jährlich", "jaehrlich"]:
        return vertrag["betrag"] / 12
    return vertrag["betrag"]
# Hilfsfunktion zu US-10

def kosten_sortieren(vertraege):
    terminal.clear_screen()
    terminal.zeige_titel("VERTRÄGE NACH KOSTEN SORTIERT (TEUERSTE ZUERST)")

    # Prüfen, ob die Liste leer ist (Truthiness)
    if not vertraege:
        print(terminal.MSG_KEINE_VERTRAEGE)
        terminal.wait_2s()
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

    # Tabellenkopf mit f-Strings formatieren (< linksbündig)
    print(f"{'ID':<4} | {'Name':<15} | {'Kategorie':<12} | {'Monatsbetrag':<14} | {'Notiz'}")
    print("=" * 70)
    for v in sortierte_vertraege:
        monats_chf = berechne_monatsbetrag(v)
        print(f"{v['id']:<4} | {v['name']:<15} | {v['kategorie']:<12} | {monats_chf:<10.2f} CHF | {v['notiz']}")
    print("=" * 70)

    # Pause via Input(), bis der Nutzer Enter drückt
    terminal.pause_enter()


def untermenu_anzeigen(vertraege):
    """
    Steuert das Untermenu für die verschiedenen Ansichten
    """

    # Falls keine Verträge vorhanden sind, direkt abweisen
    if not vertraege:
        print(terminal.MSG_KEINE_VERTRAEGE)
        terminal.wait_2s()
        return

    # Eingabe aufforderung und prüfung der Eingabe
    while True:
        terminal.show_submenu()
        choice_input = input("Bitte wähle eine Ansicht (0-4): ").strip()
        try:
            sub_choice = int(choice_input)
        except ValueError:
            print(terminal.MSG_SUBMENU_ZAHLEN_UNGUELTIG)
            terminal.wait_2s()
            continue

        if sub_choice == 1:
            contracts.uebersicht_anzeigen(vertraege)
        elif sub_choice == 2:
            kategorie_filtern(vertraege)
        elif sub_choice == 3:
            kurze_fristen_anzeigen(vertraege)
        elif sub_choice == 4:
            kosten_sortieren(vertraege)
        elif sub_choice == 0:
            break
        else:
            print(terminal.MSG_SUBMENU_ZAHLEN_UNGUELTIG)
            terminal.wait_2s()

"""
US-11: Nach dem Namen eines Abos suchen
"""