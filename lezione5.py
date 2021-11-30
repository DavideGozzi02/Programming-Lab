class CSVfile():

    def _init_(self,file_name):
        self.name=file_name
        
    def get_data(self):
        try:
            openedfile=open(self,'r')
        except Exception as e:
            print ("il file in questione non esiste")
            print ("ho avuto questo errore:{}".format(e))  
        data=[]
        for line in openedfile:
            elements=line.split(',')
            if (elements[0]!='Date'):
                data.append(elements)
        return data
    def _str_(self):
        return 'CSVfile {}'.format(self.name)

class CSVfilenumerico:

    def _init_(self,file_name):
        self.name=file_name

    def change_type(self):
        openedfile=open(self.name, 'r')
        sales=[]
        for line in openedfile:
            elements=line.split(',')
            if(elements[1]!='Sales\n'):
                try:
                    my_num=float(elements[1])
                except Exception as e:
                    print("non è convertibile in float {}".format(elements[1]))
                    print("ho trovato questo errore: {}".format(e))
                    my_num='\n'
                sales.append(my_num)
        return sales

my_file=CSVfile('shampoo_sales.csv')
my_file2=CSVfilenumerico('shampoo_sales_lezione5.csv')
sales=my_file2.change_type()
for item in sales:
    print (item)