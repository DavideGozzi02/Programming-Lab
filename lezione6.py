class CSVfile():

    def __init__(self,file_name):
        self.name=file_name
        if not isinstance(file_name, str):
            raise Exception ('il file non è una stringa')
            
    def get_data(self):
        data=[]
        #inserisco manualmente l'inizio dell'intervallo e sanitizzo òe possibili eccezioni
        try:
            x=int(input("inserisci l'inizio dell'intervallo:"))
        except Exception as e:
            print("{} non è convertibile in int".format(x))
            print("ho trovato questo errore: {}".format(e))
        if not isinstance(x, int) or (x<0):
            raise Exception("{} non è un numero intero positivo".format(x))
        if (x>len(self.name)):
            raise Exception("{} è più grande del numero di linee del file".format(x))

        #inserisco manualmente la fine dell'intervallo e sanitizzo òe possibili eccezioni
        try:
            y=int(input("inserisci l'inizio dell'intervallo:"))
        except Exception as e:
            print("{} non è convertibile in int".format(x))
            print("ho trovato questo errore: {}".format(e))
        if not isinstance(y, int) or y<0:
            raise Exception("{} non è un numero intero positivo".format(y))
        if (y>len(self.name)):
            raise Exception("{} è più grande del numero di linee del file".format(y))
        if (x>y):
            raise Exception(" la fine dell'intervallo {} è minore del suo inizio {}".format(y,x))
        openedfile=open(self.name,'r')
        for line in openedfile:
            elements=line.split(',')
            if (elements[0]!='Date'):
                try:
                    data.append(elements[0])
                except:
                    raise Exception ("non è stato possibile convertire il file in una lista")
        return data[x:y]
    def _str_(self):
        return 'CSVfile {}'.format(self.name)

my_file=CSVfile('shampoo_sales.csv')
dataM=my_file.get_data()
for line in dataM:
    print (line)