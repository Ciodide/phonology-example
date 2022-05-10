from corpus import load_corpus
from cmu_dict import load_cmu_dict
from constraint import sibilant_clash, hiatus, sibilant_clash_with_hiatus
from maxent import load_data, maxent_likelihood
import pandas as pd
import numpy as np
from scipy.optimize import minimize

corpus = load_corpus('SixDarwinBooks_clean.txt')
#corpus = load_corpus('SixAustenNovels_clean.txt')
dictionary = load_cmu_dict()
#sibilant_words_counter, sibilant_bigrams_counter = sibilant_clash(corpus, dictionary)
#print(sibilant_words_counter, sibilant_bigrams_counter)
#freq = [sibilant_bigrams_counter['Xs_sX'], sibilant_bigrams_counter['Xk_sX'], sibilant_bigrams_counter['Xs_kX'], sibilant_bigrams_counter['Xk_kX']]
#hiatus_words_counter, hiatus_bigrams_counter = hiatus(corpus, dictionary)
#freq = [hiatus_bigrams_counter['XV_VX'], hiatus_bigrams_counter['XC_VX'], hiatus_bigrams_counter['XV_CX'], hiatus_bigrams_counter['XC_CX']]
bigrams_counter = sibilant_clash_with_hiatus(corpus, dictionary)
freq = [bigrams_counter['Xs_sX'], bigrams_counter['Xs_kCX'], bigrams_counter['Xs_VX'], bigrams_counter['XkC_sX'], bigrams_counter['XV_sX'], bigrams_counter['XkC_kCX'], bigrams_counter['XkC_VX'], bigrams_counter['XV_kCX'], bigrams_counter['XV_VX']]
data = load_data("maxent_test.csv")
data['Frequency'] = freq
print(data)
x0 = [1]*len(data.columns[3:])
opt = minimize(fun = maxent_likelihood, x0=x0, args=(data), method='BFGS')
print("Weight:", opt.x, " likelihood:", -opt.fun)

#HK-S 0.06113318  0.34285944
#HK-W 0.06730072 0.36333339
#USA-W 0.07427381 0.35220012
#Phli-S 0.01514785  0.32694284
#Phli-W 0.11860449 0.31257461
#Sing-S 0.10661552  0.37590492
#Sing-W 0.12727718 0.31388243
#SixDarwinBooks 0.20157821 0.39970697
