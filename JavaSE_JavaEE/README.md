# Java
Insieme di esempi riutilizzabilit Java SE e Java EE

Indice:
* test-multithreading: Esempio di test unitario per invocazioni concorrenti multithreading.
* mapper-classi-astratte: Esempio di mapper manager che seleziona a partire dalla classe concreta ricevuta il corretto mapper relativo.
* model-generator-from-xsd: Utilizzo del plugin "jaxb2-maven-plugin" per auto-generare classi del modello a partire da uno schema xsd.
* circuit-breaker: Implementazione del pattern Circuit Breaker, utilizzato per wrapper una chiamata remota e, al verificarsi di un numero di errori configurati per unità di tempo, impedire momentaneamente la chiamata esterna ritornando un errore o un valore di default, diminuendo così il numero di thread in attesa di risposte dal sistema esterno.