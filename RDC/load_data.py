import csv
from OTable import otable

def convert_to_int(lst):
    for i in range(len(lst)):
        if lst[i] == '':
            lst[i] = 0
        else:
            lst[i] = int(lst[i])
    return lst
            
def load_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        name = next(reader)
        abbrev = next(reader)
        for i, j in zip(name, abbrev) :
            if i != '':
                otable.add_con(i, j)

        otables = []
        current_otable = None
        for row in reader:
            if row[0] != '':
                if current_otable == None:
                    current_otable = otable(len(otables), row[0])
                else:
                    otables.append(current_otable)
                    del current_otable
                    current_otable = otable(len(otables), row[0])
            if row[2] != '':
                win = True
            else:
                win = False
            current_otable.add_can(row[1], convert_to_int(row[3:]), win)


        otables.append(current_otable)
        return otables
