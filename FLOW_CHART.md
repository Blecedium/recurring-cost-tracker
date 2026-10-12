# Control Flow & Decision Logic

Dieses Dokument beschreibt den Kontrollfluss (Control Flow) und die Entscheidungslogik (Decision Logic) für das Konsolenprogramm **Recurring Cost Tracker**

## Ablaufdiagramm (Flow Sketch)

```text
======================================================================
               FLOW SKETCH: RECURRING COST TRACKER
======================================================================

 [1. PROGRAMMSTART]
        │
        ▼
 [2. INITIALISIERUNG / OUTPUT]
        │  • Begrüssung des Nutzers anzeigen
        │  • Kündigungsfristen prüfen und Warnungen ausgeben (US-10)
        │
        ▼
 ┌───► [3. HAUPTSCHLEIFE: WHILE RUNNING]
 │      │
 │      ▼
 │   [4. INPUT: MENÜ ANZEIGEN & AUSWAHL ABFRAGEN]
 │      │  • Zeige Optionen:
 │      │      1: Vertrag erfassen (US-01)
 │      │      2: Gesamtübersicht (US-04)
 │      │      3: Vertrag bearbeiten (US-05)
 │      │      4: Vertrag löschen (US-02)
 │      │      5: Nach Kategorie filtern (US-07)
 │      │      6: Monatskosten & Budget (US-08, US-09)
 │      │      7: PDF-Bericht exportieren (US-11)
 │      │      0: Beenden
 │      │  • Abfrage: choice = input("Ihre Wahl: ")
 │      │
 │      ▼
 │   [5. PROCESSING: DECISION LOGIC (IF - ELIF - ELSE)]
 │      │
 │      ├── IF choice == "1":
 │      │     └─► Input Vertragsdaten -> Validierung -> Zur Liste hinzufügen
 │      │
 │      ├── ELIF choice == "2":
 │      │     └─► Daten formatieren -> Output: Tabelle im Terminal
 │      │
 │      ├── ELIF choice == "3":
 │      │     └─► ID abfragen -> Bestehende Daten aktualisieren
 │      │
 │      ├── ELIF choice == "4":
 │      │     └─► ID abfragen -> Bestätigung -> Aus Liste entfernen
 │      │
 │      ├── ELIF choice == "5":
 │      │     └─► Kategorie wählen -> Filter anwenden -> Gefilterte Tabelle
 │      │
 │      ├── ELIF choice == "6":
 │      │     └─► Monatsbeträge summieren -> Budget vergleichen -> Warnung bei Limit
 │      │
 │      ├── ELIF choice == "7":
 │      │     └─► Daten sammeln -> PDF generieren (fpdf2)
 │      │
 │      ├── ELIF choice == "0":
 │      │     └─► running = False -> Schleife beenden
 │      │
 │      └── ELSE:
 │            └─► Output: Fehlermeldung ("Ungültige Eingabe, bitte 0-7 wählen")
 │
 └──────┴─► [Zurück zum Menü, solange running == True]

        │
        ▼ (nach Auswahl "0")
 [6. PROGRAMMENDE]
        │  • Verabschiedung anzeigen
        ▼
      [STOP]
======================================================================
```

## Erläuterung der Programmsteuerung

1. **Kontrollfluss (Control Flow):**  
   Das Programm wird über eine zentrale `while`-Schleife gesteuert. Dadurch bleibt das Menü nach jeder Aktion aktiv und wiederholt sich so lange, bis der Nutzer bewusst `0` eingibt.

2. **Entscheidungslogik (Decision Logic):**  
   Die Auswertung der Menüauswahl erfolgt über eine strukturierte `if - elif - else`-Verzweigung. Jede Option ruft die zugehörige Programmfunktion auf. Bei falschen Eingaben fängt der `else`-Zweig den Fehler ab und verhindert einen Programmabsturz.
