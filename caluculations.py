"""
Calculations - Logik & Berechnungen für den Recurring Cost Tracker
"""

from datetime import date

def tage_bis_datum(ablaufdatum_str):
    """
    Berechnet die verbleibenden Tage bis zum Ablaufdatum.
    Liest das Format 'YYYY-MM-DD' ein.
    """
    teile = ablaufdatum_str.split("-")
    jahr = int(teile[0])
    monat = int(teile[1])
    tag = int(teile[2])

    ablauf = date(jahr, monat, tag)
    heute = date.today()
    differenz = (ablauf - heute).days
    return differenz

def ablauf_erinnerung_pruefen(vertraege):
    """
    Liegt das Ablaufdatum eines Abos in 7 oder weniger Tagen in der Zukunft,
    wird direkt beim Start der Anwendung vor dem Hauptmenü eine Warnmeldung ausgeben.
    """
    warnungen_vorhanden = False
    for vertrag in vertraege:
        if "ablaufdatum" not in vertrag or not vertrag["ablaufdatum"]:
            continue

        verbleibende_tage = tage_bis_datum(vertrag["ablaufdatum"])

        #liegt in 7 oder weniger Tagen in der Zukunft (0 bis 7 Tage)
        if 0 <= verbleibende_tage <= 7:
            print(f"Warnung: Das Abonnoment '{vertrag['name']}' läuft in {verbleibende_tage} Tagen ab am {vertrag['ablaufdatum']}!")
            warnungen_vorhanden = True
    if warnungen_vorhanden:
        print("=" * 35)

# User Story 5
def monatsbetrag_berechnen(betrag, rhythmus):
    #rechnet nicht-monatliche Verträge auf Monatsbetrag um.
    rhythmus_bereinigt = rhythmus.strip().lower()
    if rhythmus_bereinigt == "jährlich" or rhythmus_bereinigt == "jaerlich":
        return betrag / 12.0
    #Standart: monatlich
    else:
        return betrag

def monatsueberblick_anzeigen(vertraege):
    """
    Finanzielle Monatsauswertung:
    - Umrechnung auf Monatsbeträge
    - Gruppierung nach Kategorie mit Zwischensummen
    - Gesamttotal aller Fixkosten
    """
    if len(vertraege) == 0:
        print("\nKeine Verträge vorhanden.\n")
        return 0.0

    #Alle eindeutigen Kategorien sammeln
    kategorien = set()
    for vertrag in vertraege:
        kategorien.add(vertrag["kategorie"])

    gesamttotal = 0.0
    print("\n" + "=" * 35)
    print("Finanzieller Monatüberblick")
    print("=" * 35)

    for kat in sorted(kategorien):
        print(f"\nKategorie: {kat}")
        zwischensumme = 0.0

        for vertrag in vertraege:
            if vertrag["kategorie"] == kat:
                monatlicher_anteil = monatsbetrag_berechnen(vertrag["betrag"], vertrag["rhythmus"])
                zwischensumme += monatlicher_anteil
                print(f"  - {vertrag['name']}: CHF {monatlicher_anteil:.2f}/Mt. ({vertrag['betrag']:.2f} {vertrag['rhythmus']})")

        print(f"--> Zwischensumme {kat}: CHF {zwischensumme:.2f}")
        gesamttotal += zwischensumme

    print("-" * 35)
    print(f"Gesamttotal Monatskosten: CHF {gesamttotal:.2f}")
    print("=" * 35 + "\n")

    return gesamttotal

# User Story 6
def budget_pruefen(vertraege, max_budget):
    # Warnung bei >= 90 % Auslastung des Monatsbudgets.
    if max_budget <= 0:
        return

    monatliche_gesamtkosten = 0.0

    for vertrag in vertraege:
        monatliche_gesamtkosten += monatsbetrag_berechnen(
            vertrag["betrag"], vertrag["rhythmus"]
        )

    grenzwert = max_budget * 0.90

    if monatliche_gesamtkosten >= grenzwert:
        print("Achtung: Nur noch weniger als 10 % des Monatsbudgets verfügbar!")











#USer Story 4: Startalert vor dem Hauptmenü
ablauf_erinnerung_pruefen(vertraege)
running = True
while running:
    show_menu()
    choice = input("Bitte wähle eine Option (0-7:) ").strip()
    if choice =="1":
        pass
    elif choice == "2":
        print("-> [In Arbeit / User Story 2] Stamm-Tabelle anzeigen...")
    elif choice == "3":
        #User Story 5
        monatsueberblick_anzeigen(vertraege)
    elif choice == "4":
        #User Story 6
        gesamtkosten =0.0
        for v in vertraege:
            gesamtkosten += monatsbetrag_berechnen(v["betrag"], v["rhythmus"])
        print(f"\nAktuelle Monatskosten: CHF {gesamtkosten:.2f}")
        print(f"Maximalbudget CHF {max_budget:.2f}")
        budget_pruefen(vertraege, max_budget)
        print()
    elif choice == "0":
        running = False
    else:
        print("Ungültige Eingabe!")