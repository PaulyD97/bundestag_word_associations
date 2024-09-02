# Readme - Dokumentation des Projekts "bundestag_word_associations"
Im Rahmen des Seminars "Computational Social Science: Themen und Positionen im Deutschen Bundestag", angeboten von Dr. Sven Banisch am Karlsruher Institut für Technologie, wurde eine App entwickelt, die die Möglichkeit bietet Wortassoziationen in den Bundestagsreden der Legislaturperiode 19 und 20 zu untersuchen. Diese Dokumentation dient dazu die Daten, den Code und die Methoden zu erklären sowie eine beispielhafte Nutzung der App aufzuzeigen.
## 1. Datenvorbereitung (Jupyter-Notebook "data_preparation.ipynb")
Für das Projekt werden die Reden aus den Bundestagsdebatten der Legislaturperiode 19 und 20 genutzt. In der Legislaturperiode 20 sind alle Reden bis einschließlich 12.04.2024 berücksichtigt. Die Reden wurden als JSON-Datei für die Seminarteilnehmenden zur Verfügung gestellt, die Daten sind aber grundsätzlich auch auf der Webseite des Bundestags verfügbar. Bei den JSON-Dateien für die beiden Legislaturperioden handelt es sich um eine Liste, die Dictionaries beinhaltet. Ein Dictionary ist eine Rede mit dem Text, dem Datum, dem Abgeordneten und weiteren Metadaten. Für dieses Projekt ist lediglich der Text, also die Rede an sich notwendig.

Folgende Schritte werden zur Vorbereitung der Daten durchgeführt:
- Satzzeichen entfernen,
- Lemmatisierung (Reduzieren der Wörter auf Stammform),
- Kleinschreibung aller Wörter,
- Wörter mit Länge von einem oder zwei Zeichen löschen,
- Stoppwörter entfernen (Liste von github.com/solariz/german_stopwords),
- Tokenisierung (Wörter werden als einzelne Strings gespeichert).

Im Anschluss daran wird eine Matrix mit den 2.500 häufigsten Wörtern in den Bundestagsreden gebildet. Die symmetrische Matrix ist 2.500 x 2.500 groß. Die Zeilen- sowie Spaltenbeschriftung sind jeweils die 2.500 Wörter. Die Einträge in der Matrix sind das gemeinsame Auftreten (co-occurence) von zwei Wörtern entsprechend der Zeile und Spalte. Zwei Wörter werden als gemeinsam auftretend gezählt, wenn sie beide in einem Fenster vorkommen, dass 40 Wörter groß ist. Das Fenster bewegt sich über alle Reden.
