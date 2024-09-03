# Readme - Dokumentation des Projekts "bundestag_word_associations"
Im Rahmen des Seminars "Computational Social Science: Themen und Positionen im Deutschen Bundestag", angeboten von Dr. Sven Banisch am Karlsruher Institut für Technologie, wurde eine App entwickelt, die die Möglichkeit bietet Wortassoziationen in den Bundestagsreden der Legislaturperiode 19 und 20 zu untersuchen. Diese Dokumentation dient dazu die Daten, den Code und die Methoden zu erklären, die Nutzung von Streamlit vorzustellen sowie eine beispielhafte Nutzung der App aufzuzeigen. Die Wahl der Methode orientiert sich an Fuhse et al. (2019) [^1].

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

Im nächsten Schritt wird aus dem gemeinsamen Auftreten zweier Wörter die Wortassoziation dieser beiden Wörter berechnet. Dafür wird die Häufigkeit des gemeinsamen Auftretens durch die Häufigkeit des Auftretens beider Wörter an sich geteilt:

$$Wortassoziation = \frac{absolutes gemeinsames Auftreten}{absolutes Auftreten Wort 1 * absolutes Auftreten Wort 2}$$

Zum Schluss wird die Matrix mit den Assoziationen in "data/coo_matrix.h5" gespeichert und kann so weiterverwendet werden.

## 2. Berechnung des Netzwerkgraphen (Python-Skript "build_network_with_word.py")

Das Python-Skript "build_network_with_word.py" beinhaltet eine Methode aus der ein Netzwerkgraph (mit Bibliothek "networkx") erstellt wird. Dafür wird ein Wort eingegeben. Dieses Wort können später die User:innen in der App wählen. Es werden in der 2.500 x 2.500 Matrix mit den Wortassoziationen die 39 Wörter gesucht, die die höchste Assoziation mit dem eingegeben Wort haben. Somit entsteht eine symmetrische 40 x 40 Matrix mit Wortassoziationen. Die Einträge (Assoziationen) werden logarithmiert, um später im Graphen besser visualisiert werden zu können.

Der Netzwerkgraph wird mit den 40 Wörtern als Knoten erstellt. Die Größe der Knoten ergibt sich aus der Stärke der Assoziation zu dem von den User:innen gewählten Wort. Die Kantengewichte zwischen den Knoten entsprechen ebenfalls der Stärke der Assoziationen. Allerdings werden nur die 10 % der Kanten mit dem größten Gewicht (also stärkste Assoziation) angezeigt. Zum Schluss wird der networkx-Graph zurückgegeben.

## 3. Frontend

Die App wird mit Streamlit gebaut und ist erreichbar unter "bundestagwords.streamlit.app". Die Webseite/App enthält die Homepage (Homepage.py), das Netzwerk (pages/2_Network.py) und diese Readme-Datei (pages/3_Readme.py).

Bei der Seite "Network" hat der/die User:in die Möglichkeit ein Wort auszuwählen, für das das Netzwerk gebildet wird. Zur Bildung des Netzwerks bedient sich das Python-Skript der Methode aus dem Skript "build_network_with_word.py", der das gewählte Wort übergeben wird. Der durch die Methode erhaltene networkx-Graph wird als pyvis-Graph in einer HTML-Datei gespeichert. Die HTML-Datei bzw. der Graph wird dann direkt in der Website eingebettet.

## 4. Beispiel mit Wort "rechtsextrem"

![Alt-Text](/dataReadme/network_rechtsextrem.PNG)


[^1]: **Fuhse, J.; O. Stuhler; J. Riebling; J. Martin (2019):** Relating social and symbolic relations in quantitative text analysis. A study of parliamentary discourse in the Weimar Republic. In: *Poetics 78.* DOI: 10.1016/j.poetic.2019.04.004.
