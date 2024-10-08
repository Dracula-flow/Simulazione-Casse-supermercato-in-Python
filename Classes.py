import random,time

class Clienti:
    def __init__(self,name):
        self.name=name
        self.products = random.randint(1,30) #numero random di prodotti

    def __repr__(self): # metodo che serve a rendere l'oggetto printabile
        return "Cliente:% s Prodotti:% s" % (self.name,self.products)


class Casse:
    def __init__(self,name):   
        self.name=name
        self.array_fila = []

    def __repr__(self): # metodo che serve a rendere l'oggetto printabile
        return "Cassa:% s Fila:% s" % (self.name,self.array_fila)

    def trafficline(self,array_foreign): #Definisce lo scorrimento dei clienti dalla fila principale a quella della cassa:
        try:
            if not self.array_fila: # equivalente if len(self.array_fila) < 1:
                
                self.array_fila.extend([array_foreign[0],array_foreign[1],array_foreign[2]]) #copio gli elementi dall'array clienti
                                                                                                #a quello delle casse.
                
                for x in range(3):
                
                    array_foreign.pop(0) #elimino gli elementi copiati, direttamente nell'array originale. 
            
            elif len(self.array_fila) < 2:
            
                self.array_fila.extend([array_foreign[0],array_foreign[1]])
            
                for x in range(2):
            
                    array_foreign.pop(0)
            
            elif len(self.array_fila) < 3:
            
                self.array_fila.append(array_foreign[0])
            
                array_foreign.pop(0)

        except IndexError: #Senza il break nel ciclo for in main, inizia ad andare in palla 
                            #perché non trova più elementi da aggiungere all'array
                            # cassa. Eccezione per far continuare lo svuotamento cassa.
            pass

    def transaction(self,products): #timer per simulare la transazione. 41 secondi di base in media + 2 secondi a prodotto.
                                    #Per esigenze di testing, commento la formula sennò devo aspettare ore.

        total_seconds = (products) # 41 + (products*2)
       
        while total_seconds > 0:
       
            time.sleep(1)
       
            total_seconds -= 1
       
        if self.array_fila[0] == self.array_fila[-1]: #Definisco la condizione di chiusura cassa. In questo caso,
                                                        # se il primo e ultimo elemento dell'array sono uguali, 
                                                            # esso viene eliminato e dopo un intervallo di tempo, viene
                                                            # stampato il messaggio di chiusura. Altrimenti, la fila continua
                                                            # a scorrere.
            self.array_fila.pop(0)
            
            time.sleep(10)
            
            print("La cassa " + str(self.name) + " chiude!")

        else:
            
            print("Avanti il prossimo!")
            
            self.array_fila.pop(0)


            


 