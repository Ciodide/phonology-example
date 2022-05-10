import pandas as pd
import numpy as np
from scipy.optimize import minimize


def load_data(filename):
    data = pd.read_csv(filename).fillna(0)
    return data

def maxent_likelihood(weight_lst, data):
    tmp_data = data.copy(deep=True)
    constraint_lst = tmp_data.columns[3:]
    for col, weight in zip(constraint_lst, weight_lst):
        tmp_data[col] = tmp_data[col]*weight
    tmp_data['H'] = tmp_data[constraint_lst].sum(axis=1)
    tmp_data['eH'] = np.exp(-tmp_data['H'])
    Z = tmp_data['eH'].sum()
    tmp_data['P'] = tmp_data['eH']/Z
    tmp_data['lnP'] = np.log(tmp_data['P'])
    L = 0
    for freq, lnp in zip(tmp_data['Frequency'], tmp_data['lnP']):
        L += freq*lnp
    print(-L)
    print(tmp_data['P']*sum(tmp_data['Frequency']))
    return -L        

#data = load_data("test2.csv")
#x0 = [0]*len(data.columns[3:])
#opt = minimize(fun = maxent_likelihood, x0=x0, args=(data), method='BFGS')
#print("Weight:", opt.x, " likelihood:", -opt.fun)
