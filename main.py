# Simula, utilizzando delle classi Python, le code ad accesso controllato di un supermercato. 
# Una coda attende di essere servita e di accedere alle code delle singole casse.
# Quando una delle code delle casse è vuota o ha spazio libero (dovrebbe avere una dimensione massima), 
# segnala al prossimo cliente in attesa di andare verso quella cassa. 
# La scelta di come rappresentare il processo e il risultato, e la strategia sono libere.
# Il lavoro è da eseguire in coppia, in pair programming.
# Se possibile consegnare il codice attraverso Github.

# Suggerimento di Mattia compagno: le casse sono classi, le file sono definite da classi e costituiscono un array.

import random as r
from Classes import Clienti,Casse

# Definizione liste: il programma ha bisogno di liste
# per simulare lo scorrimento della fila


arr_clienti=[Clienti(i) for i in range(9,(r.randint(12,33)] # La lista di persone in attesa nella coda "principale"
                                                            # Generiamo gli oggetti direttamente nella lista
                                                                # Visto che sono identici, sarà utile per richiamarne
                                                                    # i metodi.

print(arr_clienti)

# Funzioni
list_casse =[Casse(i) for i in range (3)] #I generatori funzionano solo con le liste/array. Non con le tuple.
                                                            # Il limite superiore del range di possibili clienti sarà un randint.


try:
    for i in range(len(arr_clienti)): 
        for obj in list_casse: # Dobbiamo iterare il metodo per ogni oggetto presente nella lista, altrimenti
                                # non agiranno in contemporanea, come dovrebbero
            obj.trafficline(arr_clienti)
            print(obj)
        for obj in list_casse:
            obj.transaction(obj.array_fila[0].products) #Necessario specificare l'indice perché altrimenti andrà fuori index.
            print(obj)

except IndexError: # Arrivati alla fine del loop, il metodo transaction non riesce più a pescare indici dalla lista clienti.
                    # Poiché è previsto che ad un certo punto non ci siano più clienti, inseriamo un pass per far continuare
                    # il programma.
    pass
        

