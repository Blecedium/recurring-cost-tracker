# Recurring Cost Tracker - Abo- & Vertragsverwaltung (Console)

Eine einfache Konsolen-Anwendung in Python, mit der Studierende ihre wiederkehrenden Fixkosten (wie Miete, Krankenkasse oder Abonnements) an einem zentralen Ort verwalten können.

Das Programm hilft dabei, den Überblick über die monatlichen Ausgaben zu behalten, das persönliche Budget zu prüfen und Kündigungsfristen rechtzeitig zu erkennen.

---

## Hauptfunktionen

* Verträge verwalten: Neue Fixkosten eingeben, anzeigen, ändern und löschen.
* Kategorien und Filter: Ausgaben nach Bereichen (wie Wohnen oder Freizeit) filtern.
* Kosten berechnen: Gesamte Monats- und Jahreskosten automatisch zusammenrechnen.
* Erinnerung und Budget: Warnung bei ablaufenden Kündigungsfristen und Budgetüberschreitungen.
* Speichern und Laden: Automatische Speicherung in der Datei vertraege.json.

---

## Analyse
### Problem
Viele Studierende und Privatpersonen verlieren den Überblick über ihre laufenden Abonnemente, Verträge und regelmässigen Zahlungen (z. B. Miete, Krankenkasse, Streaming). Dadurch werden Kündigungsfristen verpasst und unnötige monatliche Fixkosten bezahlt.

Der "Recurring Cost Tracker" löst dieses Problem über eine übersichtliche Konsolenanwendung. Nutzerinnen und Nutzer können ihre bestehenden Verträge erfassen, in einer Gesamtübersicht anzeigen, bearbeiten, nach Kategorien filtern, Verträge mit kurzen Kündigungsfristen gezielt identifizieren sowie gekündigte Verträge löschen. Zusätzlich bietet das Programm eine Monatsauswertung mit Budget-Warnung, eine Kostensortierung sowie eine Textsuche. 

Rolle | Beschreibung
| :--- | :--- |
Nutzer/Nutzerin | Erfasst, verwaltet, filtert, durchsucht und löscht eigene Abonnemente und Verträge, um monatliche Fixkosten, Budgets und Kündigungsfristen im Blick zu behalten.

## User Story

Alle Beträge werden in Schweizer Franken (CHF) geführt.

### US-01 Vertrag neu erfassen (Cyrill Schreyvogel)
Als Nutzer möchte ich neue Fixkosten (wie Netflix, Miete oder mein Handyabo) mit Name, Betrag, Rhythmus und Kündigungsfrist erfassen, damit ich alle meine laufenden Kosten an einem zentralen Ort sammle.

Akzeptanzkriterien
* Nach vollständiger Eingabe von Name (z. B. "Netflix"), Betrag (z. B. 19.90), Zahlungsrhythmus ("monatlich") und Kündigungsfrist in Tagen (z. B. 30) wird der Vertrag gespeichert und die Meldung "Vertrag erfolgreich erfasst." angezeigt.
* Wird beim Betrag Text (z. B. "zwanzig") oder ein Wert <= 0 eingegeben, wird die Meldung "Ungültiger Betrag! Bitte positive Zahl eingeben." angezeigt und wiederholt die Abfrage.

---

### US-02 Gesamtübersicht (Cyrill Schreyvogel)
Als Nutzer möchte ich alle erfassten Fixkosten in einer formatierten Terminal-Tabelle sehen, damit ich auf einen Blick alle meine Verträge und deren Grunddaten erkennen kann.

Akzeptanzkriterien
* Beim Aufruf werden alle Verträge in einer Tabelle dargestellt und die Werte mit genau zwei Dezimalstellen (19.90 CHF).
* Sind im Programm noch keine Verträge hinterlegt, erscheint der Hinweis "Keine Verträge vorhanden."

---

### US-03 Einträge bearbeiten (Cyrill Schreyvogel)
Als Nutzer möchte ich bestehende Verträge editieren können (z. B. Preisanpassung), damit ich Konditionsänderungen ohne Neuerfassung aktualisieren kann.

Akzeptanzkriterien
* Nach Eingabe einer gültigen ID (z. B. 1) kann ein neuer Betrag (z. B. 21.90) eingegeben werden, wird ein Feld mit der Enter-Taste leer gelassen, bleibt der bisherige Wert unverändert erhalten.
*  Wird eine ID eingegeben, die im System nicht existiert (z. B. 73), zeigt das Programm "Vertrag mit ID 73 nicht gefunden." an und kehrt ohne Absturz ins Menü zurück.

---

### US-04 Erinnerung Ablauf Abo (Babith Sinnathurai)
Als Nutzer möchte ich beim Programmstart automatisch gewarnt werden, wenn ein Abonnement in den nächsten 7 Tagen abläuft, damit ich rechtzeitig über eine Verlängerung oder Kündigung nachdenken kann.

Akzeptanzkriterien
* Liegt das Ablaufdatum eines Abos in 7 oder weniger Tagen in der Zukunft, wird direkt beim Start der Anwendung vor dem Hauptmenü eine Warnmeldung ausgegeben.
* Liegen alle Ablaufdaten mehr als 7 Tage in der Zukunft, startet das Programm direkt mit dem Hauptmenü ohne zusätzliche Warnmeldung.

---

### US-05 Monatsüberblick (Babith Sinnathurai)
Als Nutzer möchte ich eine finanzielle Monatsauswertung sehen, bei der alle Ausgaben auf Monatsbeträge umgerechnet, nach Kategorien gruppiert und mit Zwischensummen sowie einem Gesamttotal angezeigt werden, damit ich meinen monatlichen Finanzbedarf genau kenne.

Akzeptanzkriterien
* Beim Aufruf des Monatsüberblicks werden alle Fixkosten dargestellt.
* Nicht-monatliche Verträge werden für die Monatsrechnung automatisch auf den Monatsbetrag umgerechnet.

---

### US-06 Hinweis Überschreitung des Budgets (Babith Sinnathurai)
Als Nutzer möchte ich einen Maximalbetrag angeben können, welche mich darauf hinweist wenn es nur noch 10 % bis zum Maximalbetrag hat, bei meinem letzten Eintrag, damit ich vorplanen kann für den restlichen Monat.

Akzeptanzkriterien
* Erreichen die monatlichen Fixkosten 90 % oder mehr des Maximalbudgets, erscheint der Warnhinweis "Achtung: Nur noch weniger als 10 % des Monatsbudgets verfügbar!".
* Liegt die Gesamtsumme unter 90 % des Budgets (oder wurde kein Limit definiert), erscheint kein Warnhinweis.

---

### US-07 Nach Kategorie filtern (Thilaxan Balachandran)
Als Nutzer möchte ich Verträge nach Kategorien filtern, damit ich eine bestimmte Ausgabe schnell finde.

Akzeptanzkriterien
* Nach Auswahl einer Kategorie (z. B. "Wohnen") werden in der Ergebnistabelle ausschliesslich Verträge angezeigt, die dieser Kategorie zugeordnet sind.
* Gibt es in der ausgewählten Kategorie keine Verträge, erscheint die Rückmeldung "Keine Verträge in der Kategorie Wohnen vorhanden."

---

### US-08 Kündigungsfrist überprüfen (Thilaxan Balachandran)
Als Nutzer möchte ich mir mit einem Klick alle Verträge mit kurzen Kündigungsfristen anzeigen lassen, damit ich Verträge mit schnellem Handlungsbedarf sofort im Blick habe.

Akzeptanzkriterien

* Bei Auswahl der Option "Kurze Fristen anzeigen" werden ausschliesslich Verträge aufgelistet, deren Kündigungsfrist 30 Tage oder weniger beträgt.
* Gibt es keine Verträge mit einer Frist von 30 oder weniger Tagen, erscheint ein Hinweis wie "Keine Verträge mit kurzer Kündigungsfrist vorhanden".

---

### US-09 Vertrag löschen (Thilaxan Balachandran)
Als Nutzer möchte ich gekündigte Verträge aus der Liste löschen, damit sie nicht mehr mitberechnet werden.

Akzeptanzkriterien

* Nach Eingabe einer vorhandenen Vertrags-ID und Bestätigung einer Sicherheitsabfrage wird der Vertrag gelöscht und die Meldung "Vertrag erfolgreich gelöscht." ausgegeben.
* Wird die Sicherheitsabfrage mit "Nein" beantwortet oder eine ungültige ID eingegeben, bleibt die Vertragsliste unverändert.

---

### US-10 Einfache Sortierfunktion für die Anzeige (Vithuschan Jeyatharan)
Als Nutzer möchte ich Verträge nach Kosten sortieren können. Zum Beispiel, dass ich meine teuersten Abos sofort ganz oben sehe.

Akzeptanzkriterien:
Bei Auswahl von „Nach Kosten sortieren“ wird die Liste so sortiert ausgegeben, dass der Vertrag mit dem höchsten Monatsbetrag ganz oben in der ersten Zeile steht.

---

### US-11 Schnelle Textsuche (Vithuschan Jeyatharan)
Als Nutzer möchte ich nach dem Namen eines Abos suchen können, damit ich einen bestimmten Eintrag direkt finde ohne die ganze Liste durchzulesen.

Akzeptanzkriterien:
Nach Eingabe eines Textbegriffs (z. B. "Spotify") werden alle Verträge aufgelistet, deren Name diesen Text enthält.
Ergibt die Suche keinen Treffer, wird eine Meldung wie "Kein Vertrag mit dem Suchbegriff gefunden." angezeigt.

---

### US-12 Zusätzliches Notizfeld (Vithuschan Jeyatharan)
Als Nutzer möchte ich eine kurze Textnotiz zu einem Vertrag hinterlegen können, wie zum Beispiel Kundennummer oder Login-E-Mail, damit ich alle relevanten Infos zum Abo direkt parat habe.

Akzeptanzkriterien:
Beim Erfassen oder Bearbeiten kann eine Textnotiz hinterlegt werden, die in der Vertragsansicht angezeigt wird.

---

### Projektanforderungen

Die Anwendung erfüllt alle drei zentralen Anforderungen des Moduls:

1. Interaktive App (Konsoleneingabe)
    Die komplette Steuerung erfolgt über ein menügeführtes Konsoleninterface ('main.py'). Nutzerinnen und Nutzer wählen Aktionen über Ziffern im Hauptmenü aus, geben Vertragsdaten ein und erhalten formatierte Tabellen sowie Statusmeldungen zurück.
2. Datenvalidierung (Input Checking)
    Alle Benutzereingaben werden vor der Verarbeitung geprüft:
    * Menüauswahlen prüfen auf gültige Optionen (if/elif/else)
    * Numerische Eingaben (Vertrags-IDs, Beträge in CHF, Kündigungsfristen in Tagen) werden mittels 'try/except ValueError' sowie Bereichsprüfungen ('>0' bzw. '>=0') validiert, sodass falsche Eingaben abgefangen werden und das Programm nicht abstürzt.
    * Sicherheitsabfragen vor dem Löschen verhindern versehentlichen Datenverlust.
3. Dateiverarbeitung (Read/Write)
    * Input & Output ('vertraege.json')
        Beim Programmstart werden gespeicherte Verträge über 'daten_laden()' aus der Datei 'vertraege.json' geladen (existiert die Datei noch nicht oder ist sie leer, wird eine leere Liste '[]' zurückgegeben). Nach Änderungen (Erfassen, Bearbeiten, Löschen) werden die Daten über 'daten_speichern()' dauerhaft in 'vertraege.json' gesichert.

## Implementierung
### Technologie
* Python 3.13
* Entwicklungsumgebung: VS Code / GitHub Codespaces/Terminal

### Repository-Struktur

recurring-cost-tracker/
|--- main.py                # Hauptprogramm, Konsolenmenü, Benutzerinteraktion & Steuerungslogik
|--- vertraege.json         # Datenspeicher für alle erfassten Verträge (Input/Output)
|--- README.md              # Projektdokumentation & User Stories


## Team & Aufteilung

Name | Verantwortung / User Stories
| :--- | :--- |
Cyrill Schreyvogel | US-01, US-02, US-03 & US-12: Vertrag erfassen, Gesamtübersicht, Einträge bearbeiten & Notizfeld
Babith Sinnathurai | US-04, US-05 & US-06: Ablauf-Erinnerung beim Start, Monatsüberblick & Budget-Warnung (calculations.py)
Thilaxan Balachandran | US-07, US-08 & US-09: Nach Kategorie filtern, kurze Kündigungsfristen (<= 30 Tage) anzeigen & Vertrag löschen sowie Projektdokumentation (README.md)
Vithuschan Jeyatharan | US-10 & US-11: Nach Kosten sortieren & schnelle Textsuche

## Lizenz