"""
Calculations - Logik &amp; Berechnungen für den Recurring Cost Tracker
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
    """rechnet nicht-monatliche Verträge auf Monatsbetrag um."""
    rythmus_bereinigt = rhythmus.strip().lower()
    if rythmus_bereinigt in ["jährlich", "jaehrlich"]:
        return betrag / 12
    return betrag