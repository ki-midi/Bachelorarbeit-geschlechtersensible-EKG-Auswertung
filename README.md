Projektbeschreibung
Dieses Repository enthält den Quellcode zur Durchführung der in der Bachelorarbeit beschriebenen Analyse von EKG-Daten mittels neuronaler Netze. Ziel des Projekts ist die Entwicklung und Evaluation von Modellen zur Klassifikation und Regression physiologischer Parameter basierend auf EKG-Signalen.

Datenvorverarbeitung
Die Aufbereitung und Sortierung der Datensätze erfolgt in einem eigens entwickelten Sortierprogramm. Hierbei werden die ursprünglichen EKG-Datensätze in drei separate Gruppen unterteilt:

Ein kombinierter Datensatz mit EKGs aller Geschlechter,

Ein geschlechtsspezifischer Datensatz mit ausschließlich männlichen Probanden,

Ein geschlechtsspezifischer Datensatz mit ausschließlich weiblichen Probanden.

Jeder dieser Datensätze wird auf eine einheitliche Stichprobengröße von 9715 EKGs reduziert. Diese standardisierten Datensätze bilden die Grundlage für das Training und die Validierung der neuronalen Netze.

Modelltraining und Validierung
Zur Modellierung werden zwei verschiedene neuronale Netze verwendet:

Ein Klassifikationsmodell

Ein Regressionsmodell

Beide Modelle werden jeweils separat mit den zuvor beschriebenen Datensätzen trainiert und validiert. Die Evaluation erfolgt anschließend mithilfe der Programme NN_Test_Klassifikation und NN_Test_Regression, welche die trainierten Modelle anhand separater Testdatensätze überprüfen.

Vereinfachtes Modell
Für die in der Arbeit erläuterte vereinfachte Modellvariante steht ein separates Sortierprogramm zur Verfügung. Dieses sortiert die Datensätze gemäß der vereinfachten Klassifikationskriterien.

Im Gegensatz zur vollständigen Modellvariante erfolgen Training, Validierung und Test des vereinfachten Modells innerhalb desselben Programms. Dadurch wird der gesamte Analyseprozess für diese Variante zentralisiert und vereinfacht.

Zur grafischen Darstellung der EKG-Daten steht ein separates Visualisierungsprogramm zur Verfügung. Dieses ermöglicht die Darstellung einzelner EKG-Signale aus den Datensätzen und dient der qualitativen Kontrolle sowie der Veranschaulichung der Eingangsdaten für die Modellierung.

Mit der Ergänzung AUC und F1 wurde zu der bestehenden Accuracy auch noch AUC und F1 berechnet für das Klassifikationsmodell.
