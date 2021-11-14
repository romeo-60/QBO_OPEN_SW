#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
#acquisizione dati
pd.read_csv("DataSeq.csv")

#salvare i dati dentro una variabile
dataset = pd.read_csv("DataSeq.csv")
print (dataset)
print ("*****************")
n_sequence = dataset['n_sequence']
n_cycle = dataset['n_cycle']
print(n_sequence,n_cycle)
print ("----------------")
#--------
# titolo del grafico
plt.title("Storico Clienti")
# testo dell'asse x
plt.xlabel("giorni")
# testo dell'asse y
plt.ylabel("avventori")
# sfondo a griglia
plt.grid()
# dimensioni de grafico
plt.rcParams['figure.figsize'] = [15,10] #altezza,lunghezza
#la funzione per creare il grafico è molto semplice
plt.scatter(n_sequence,n_cycle, label="avventori_giorno", c='blue', marker='o', s=2)
#definire la leggenda del grafico
plt.legend()
#salviamo il grafico
plt.savefig("Seq_work.png")
#mostriamo il grafico
plt.show()