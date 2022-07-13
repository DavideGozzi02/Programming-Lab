class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        #controllo che il file si possa aprire e leggere
        try:
            openedfile = open(self.name, 'r')
            openedfile.readline()
        except:
            raise ExamException ("Errore in apertura del file")
            return None

            
        result = []

        #creo una lista che userò per controllare che gli epoch siano ordinati 
        epoch = []
        previous_epoch = -1
       
        for line in openedfile:
            #creo una lista "new" che sarà l'elemento della lista "result"
            new = []
            datas = line.split(',',1)      #massimo 2 elementi
            error_found = False
            #controllo di non essere sulla prima riga del file
            if (datas[0] != 'epoch'): 
                #provo che l'epoch sia convertibile in float se non lo è verrà saltato 
                try:
                    datas[0]=float(datas[0])
                
                except:
                    error_found= True
                    print("un epoch non è solo numerico", datas[0])
                    continue
                #provo che la temperatura sia convertibile in float e converto l'epoch in int
                    
                try:    
                    new.append(int(datas[0]))
                    new.append(float(datas[1]))
                    epoch.append(int(datas[0]))
                except: 
                    print("problema nella conversione della riga:",datas)
                    error_found = True
                    continue
                    
                #controllo che gli epoch siano ordinati e non ci siano duplicati 
                if (int(datas[0]) <= previous_epoch): 
                    raise ExamException("gli epoch non sono ordinati o sono duplicati")
                    
                #se non ho trovato errori allora aggiungo i valori a result     
                if (error_found == False): 
                    result.append(new)
                    previous_epoch = int(datas[0])
                
        #controllo che il file non fosse vuoto
        if len(result)==0:
            raise ExamException("errore in apertura, il file è vuoto")

        
        openedfile.close()

        return result

        


def compute_daily_max_difference(time_series):

    result = []
    previous_day = -1  #parto da un giorno che non può essere nella lista 
    
#itero nella time series
    for item in time_series:
        #creo una lista dove salvo i valori di ogni giorno
        new = []
        #trovo il giorno del item che sto considerando 
        current_day = item[0] - (item[0]%86400)
        
        #se il giorno è diverso da quello dell'item precedente
        if (current_day != previous_day):
            #itero una seconda volta sulla time_series
            for liste in time_series:
                #controllo se l'elemento che sto considerando nel secondo for ha la stessa data del item
                if (liste[0] - (liste[0]%86400) == current_day):
                    #se ha la stessa data salvo la temperature in new
                    new.append(liste[1])
                    
            #controllo che ci sia più di una misurazione per giorno 
            if (len(new) > 1):
                result.append((max(new) - min(new)))
            else: 
                result.append(None)
                
        previous_day = current_day

    return result
    