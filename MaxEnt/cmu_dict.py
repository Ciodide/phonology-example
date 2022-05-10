import csv
import copy

class sound:
    def __init__(self, arpabet, stress=None):
        self.arpabet = arpabet
        self.stress = stress
    def __str__(self):
        return self.arpabet + ";" + str(self.stress)

def load_cmu_dict():
    cmu_dict = dict()
    with open("9_BreissHayesDictionary.txt", mode ='r') as cmu_dict_file:
        reader = csv.reader(cmu_dict_file, delimiter='\t')
        for row in reader:
            pronounce = []
            if row[0] in cmu_dict:
                continue
            for i in row[1].split(' '):
                if i[-1].isnumeric():
                    pronounce.append(sound(arpabet=i[:-1], stress=i[-1]))
                else:
                    pronounce.append(sound(arpabet=i))
            cmu_dict[row[0]] = pronounce
    return cmu_dict


            
        
