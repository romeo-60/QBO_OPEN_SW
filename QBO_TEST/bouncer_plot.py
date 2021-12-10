#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
#acquisizione dati
pd.read_csv("DataSeq.csv")

#salvare i dati dentro una variabile
dataset = pd.read_csv("DataSeq.csv")

#print ('dataset',dataset)
print ("*****************")
counter = dataset['n_sequence']
hight = dataset['n_cycle']
print('counter',counter, 'hight', hight)
print ("----------------")
#--------
# titolo del grafico
plt.title("bouncer_plot")
# testo dell'asse x
plt.xlabel("counter")
# testo dell'asse y
plt.ylabel("hights")
# sfondo a griglia
plt.grid()
# dimensioni de grafico
plt.rcParams['figure.figsize'] = [15,10] #altezza,lunghezza
#la funzione per creare il grafico è molto semplice
plt.scatter(counter,hight, label="hight", c='blue', marker='o', s=2)
plt.plot(counter, hight, color='red', linewidth=2) # Create a red line with linewidth 2.
#definire la leggenda del grafico
plt.legend()
#salviamo il grafico
plt.savefig("bouncer.png")
#mostriamo il grafico
plt.show()