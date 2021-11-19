values = []
my_file=open('shampoo_sales.csv', 'r')
for line in my_file:
    elements=line.split(',')
    values=line.split(',')
    if (elements[0]!='Date'):
        date=elements[0]
        value=elements[1]
sum(values)
print(sum(values))
#print(my_file.read())
my_file.close 