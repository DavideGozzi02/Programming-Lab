class CSVFile():
    def  __init__(self, file):
        self.name=name

    def get_data(self):
        file_list = []   
        openedfile = open(self.file_name, 'r')
        for line in openedfile:
            elements = line.split(',')
            if elements[0] != "Date"
                lineElements = line.split (',')
                lineElements [1] = lineElements [1].strip()
            file_list.append(lineElements)
        return file_list 

shampooFile = CSVFile ('shampoo_sales.csv')
shampoo_sales = shampooFile.get_data()

for line in shampooList:
    print(line)