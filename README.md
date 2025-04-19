Projektbeschreibung
Dieses Repository enthält den Code zur Durchführung der in der Bachelorarbeit beschriebenen Analyse von EKG-Daten mittels KI. Ziel des Projekts ist die Entwicklung und Evaluation von Modellen zur Klassifikation und Regression zur geschlechterspezifischen EKG Diagnostik von Herzinfarkten.

Datenvorverarbeitung
Die Aufbereitung und Sortierung der Datensätze erfolgt imn Sortierprogramm. Hierbei werden die ursprünglichen EKG-Datensätze in drei separate vereinfachte Datensätze unterteilt:

Ein kombinierter Datensatz mit EKGs aller Geschlechter,
Ein geschlechtsspezifischer Datensatz mit ausschließlich männlichen Probanden,
Ein geschlechtsspezifischer Datensatz mit ausschließlich weiblichen Probanden.

Diese standardisierten Datensätze bilden die Grundlage für das Training und die Validierung der neuronalen Netze.

Modelltraining und Validierung
Zur Modellierung werden zwei verschiedene neuronale Netze verwendet:

Ein Klassifikationsmodell
Ein Regressionsmodell

Beide Modelle werden jeweils separat mit den zuvor beschriebenen Datensätzen trainiert und validiert. Die Evaluation erfolgt anschließend mithilfe der Programme NN Test Klassifikation und NN Test Regression, welche die trainierten Modelle anhand separater Testdatensätze überprüfen.

Vereinfachtes Modell
Für die in der Arbeit erläuterte vereinfachte Modellvariante steht ein separates Sortierprogramm zur Verfügung. Dieses sortiert die Datensätze gemäß der vereinfachten Klassifikationskriterien.

Im Gegensatz zur vollständigen Modellvariante erfolgen Training, Validierung und Test des vereinfachten Modells innerhalb desselben Programms. Dadurch wird der gesamte Analyseprozess für diese Variante vereinfacht.

Zur grafischen Darstellung der EKG-Daten steht ein separates Visualisierungsprogramm zur Verfügung. Dieses ermöglicht die Darstellung einzelner EKG-Signale aus den Datensätzen.

Mit der Ergänzung AUC und F1 wurde zu der bestehenden Accuracy auch noch AUC und F1 berechnet für das Klassifikationsmodell.

Mit dem Programm Crossvalidation können beliebig viele Programme erstellt werden jeweils mit einer anderen Durchmischung  der Trainings und Validierungsdaten. mit derm Crossvalidation Testdatensatz können dann die Programme mit dem Testdatensatz getestet werden.
