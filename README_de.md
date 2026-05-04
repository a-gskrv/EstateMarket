# Wohnungsvermietungsprojekt

## Projektziel

Entwicklung einer voll funktionsfähigen Back-End-Anwendung für ein Wohnungsvermietungssystem, einschließlich der Verwaltung von Inseraten sowie Such- und Filterfunktionen nach verschiedenen Parametern.

---

# Beschreibung der Anwendungsfunktionalität

## Verwaltung von Inseraten

### 1. Inserat erstellen

Der Benutzer gibt Informationen über die Immobilie ein:

- Titel
- Beschreibung
- Standort
- Preis
- Anzahl der Zimmer
- Immobilientyp (Wohnung, Haus usw.)

### 2. Inserat bearbeiten

Der Benutzer kann beliebige Informationen eines bestehenden Inserats ändern.

### 3. Inserat löschen

Der Benutzer kann sein Inserat aus der Datenbank löschen.

### 4. Verfügbarkeit des Inserats verwalten

Wechsel des Inseratstatus (aktiv/inaktiv), um das Inserat vorübergehend auszublenden oder wieder sichtbar zu machen.

---

## Suche und Filterung

### 1. Suche nach Schlüsselwörtern

Der Benutzer gibt Schlüsselwörter ein, nach denen in Titeln und Beschreibungen der Inserate gesucht wird.

### 2. Filterung nach Parametern

- **Preis** — Möglichkeit, einen Mindest- und Höchstpreis anzugeben
- **Standort** — Möglichkeit, eine Stadt oder einen Bezirk in Deutschland anzugeben
- **Anzahl der Zimmer** — Möglichkeit, einen Bereich der Zimmeranzahl anzugeben
- **Immobilientyp** — Möglichkeit, den Immobilientyp auszuwählen: Wohnung, Haus, Studio usw.

### 3. Sortierung der Ergebnisse

- Möglichkeit der Sortierung nach Preis (aufsteigend/absteigend)
- Nach Hinzufügungsdatum (neueste/älteste)

---

## Benutzerauthentifizierung und Autorisierung

### 1. Benutzerregistrierung

Der Benutzer gibt seine Daten zur Erstellung eines Kontos ein:

- Name
- E-Mail
- Passwort

### 2. Anmeldung

Eingabe von E-Mail und Passwort für den Zugriff auf das Konto.

### 3. Rollenbasierte Zugriffsrechte

- **Mieter** — kann Inserate ansehen und filtern
- **Vermieter** — kann eigene Inserate erstellen, bearbeiten und löschen

---

## Buchung

### 1. Buchung erstellen

Der Benutzer kann eine Unterkunft für bestimmte Daten buchen.

### 2. Buchungen anzeigen

Der Benutzer kann seine aktiven und abgeschlossenen Buchungen ansehen.

### 3. Buchung stornieren

Der Benutzer kann eine Buchung vor einem bestimmten Datum stornieren.

### 4. Buchung bestätigen

Der Vermieter kann Buchungsanfragen bestätigen oder ablehnen.

---

## Bewertungen und Rezensionen

### 1. Bewertung hinterlassen

Ein Benutzer, der die Unterkunft gemietet hat, kann eine Bewertung und Rezension für ein bestimmtes Inserat hinterlassen.

### 2. Rezensionen anzeigen

Möglichkeit, alle Rezensionen für ein bestimmtes Inserat anzusehen.

---

## Zusätzliche Funktionen

### 1. Sortierung nach Beliebtheit

Nach Anzahl der Aufrufe oder Bewertungen.

### 2. Suchverlauf

- Speicherung von Suchbegriffen — Speicherung der vom Benutzer verwendeten Suchbegriffe in einer separaten Tabelle
- Anzeige beliebter Suchanfragen — die am häufigsten verwendeten Suchanfragen werden zuerst angezeigt

### 3. Verlauf der Inseratsaufrufe

- Speicherung von Aufrufen — Speicherung von Informationen über jeden Aufruf eines bestimmten Inserats durch den Benutzer
- Anzeige beliebter Inserate — Inserate mit den meisten Aufrufen werden zuerst angezeigt

---

## Technische Anforderungen

- Django — wird für die Entwicklung der Hauptlogik der Anwendung, Datenbankverwaltung und API-Erstellung verwendet
- MySQL — Hauptdatenbank zur Speicherung von Inseraten und Benutzerdaten

---

## Zusätzliche Technologien

- Docker — wird für die Containerisierung der Anwendung verwendet
- AWS — Bereitstellung der Anwendung in der AWS-Cloud mit Diensten wie:
  - EC2 (virtuelle Server)
  - und anderen erforderlichen Diensten