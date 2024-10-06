Progetto in Python per il Corso "Tecniche di programmazione Python" presso Immaginazione & Lavoro, 2024.

Il programma genera: 
1- Un numero random di clienti di un supermercato, ognuno con un certo numero di prodotti.
2- 3 casse che si occuperanno di smaltire la coda.

Tutti gli elementi vengono generati direttamente in un array, visto che hanno proprietà tutto sommato identiche.

Sia i clienti che le casse sono oggetti generati tramite classi.
I clienti hanno solo le proprietà nome e numero prodotti.

La classe "Casse" è la più complessa.
Ogni cassa ha un nome e un array in cui trasferire i clienti dalla coda principale.
Il trasferimento e scorrimento delle file è simulato tramite aggiunta e rimozione contemporanea degli elementi degli array.
Le transazioni sono simulate tramite un countdown dipendente dal numero in prodotti in possesso del cliente.
Quando la singola cassa non ha più clienti e non riesce a prenderne altri dalla coda principale, si chiude dopo un intervallo di tempo.

Codice by Simone Avagliano e Lorenzo Pourpour.
