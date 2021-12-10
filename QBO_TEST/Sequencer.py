#!/usr/bin/python3
import csv

class w_s():
    
    def __init__(self, sequence, seq, n_cycle, alpha, beta):
        
        """Class constructor

        It is the constructor of the class. It does:
            - receive the number of sequences as input
            - for each integer between 1 and the number of sequences 
            - the following calculation criteria must be applied:
            - if it is even, divide it by two
            - otherwise multiply it by three and add one to it
            -the calculation sequence ends with the result of the operations = 1
            - S = number of sequences
            - O = number of operations
            - P = quantity of even numbers
            - D = quantity of odd numbers
        """
        #self.index_data = []
        #self.sequence = 1
        #self.seq = 1
        #self.n_calc = seq
        #self. n_cycle = 0
        #self.alpha = alpha
        #self.beta = beta 
    
    def discriminator(self, seq, n_cycle, n_alpha, n_beta, counter, index_data):
        #print ("seq",seq)
        n_calc = seq
        if n_calc % 2 == 0:
            #alpha = n_calc
            n_calc = int(n_calc / 2)
            n_alpha += 1
            # print ("alpha =","  ",alpha)
            #print ("n_alpha =","   ",n_alpha)
        else:
            #beta = n_calc
            n_calc = (n_calc *3)+1
            n_beta += 1
            #print ("beta =","   ", beta)
            #print ("n_beta ="," ", n_beta)
        #print ("n_calc",n_calc)

        if n_calc == 1:
            counter +=1
            n_cycle = n_alpha + n_beta
            print ("end of operations for", counter-1)
            print ("n_alpha =", "   ", n_alpha)
            print ("n_beta =","    ", n_beta)
            print ("n_cycle =","   ",n_cycle)
            print ("********************")
            # write index_data
            sequence_work = counter-1
            index_data.append([sequence_work, n_cycle, n_alpha, n_beta])
        else:
            seq = n_calc
            #n_cycle += 1
            w_s.discriminator(self, seq, n_cycle, n_alpha, n_beta, counter,index_data)
        return index_data

    def sequencer(self):
        global data_work
        n_cycle = 0
        n_alpha = 0
        n_beta = 0
        counter = 0
        index_data = []
        print("-------")
        print("indice vuoto", index_data)
        print ("-----")
        for seq in range(sequence):
            seq = seq+1
            counter += 1
            print("seq =","   ", seq)
            w_s.discriminator(self, seq, n_cycle, n_alpha, n_beta, counter, index_data)
        #return seq
        # save file data_work
        data_work = [('n_sequence', 'n_cycle', 'n_alpha', 'n_beta')]
        #print ("index_data", index_data)
        print ("lunghezza indice", len(index_data))
        print ("primo elemento di index_data",index_data[0])
        for i in (index_data):
            data_work.append(i)
        print ("data_work", data_work)
    # def write_data (self,index_data):
    #     indice = index_data
    #     print ("index_data", indice)


if __name__=='__main__':
    """ Main void.

    Is the main void executed when started. It does:
    - request for inputation number of sequences
    - calculation of the result starting from 1 up to the number of sequences
    - print data table S, O, P, D

    """
    while True:
        try:
            sequence = int(input("inserire un numero intero positivo di sequenze "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    
    #n_calc = seq
    #n_cycle = 0
    #n_alpha = 0
    #n_beta = 0
    print ("numero sequenze ", sequence)
    print("----")
    #print ("start discrimination....")
    print ("start sequencer for ", sequence)
    w_s.sequencer(sequence)
    print ("end of global operations")
    with open('DataSeq.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_work)