values = []
my_file=open('shampoo_sales.csv', 'r')
for line in my_file:
    values=my_file.split(',')
    mio_numero=float(values)
    somma=somma+mio_numero

print(somma)
print(my_file.read())
my_file.close 