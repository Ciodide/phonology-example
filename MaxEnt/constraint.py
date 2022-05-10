import pandas as pd
import string 

def contain_punctuation(str):
    for i in str:
        if i in string.punctuation:
            return True
    return False

def sibilant_clash(corpus, dictionary):
    sibilant_ipa_lst = ['s', 'z', 'ʂ', 'ʐ', 'ɕ', 'ʑ', 'ʃ', 'ʒ']
    sibilant_arpabet_lst = ['S', 'Z', 'SH', 'ZH']
    not_found = dict()
    not_found_word_counter = 0
    not_found_bigrams_counter = 0
    words_counter = {
        'sX': 0,
        'kX': 0,
        'Xs': 0,
        'Xk': 0
    }
    bigrams_counter = {
        'Xs_sX': 0,
        'Xs_kX': 0,
        'Xk_sX': 0,
        'Xk_kX': 0
    }
    # Data from independent words
    for word in corpus:
        if word in dictionary:
            if dictionary[word][0].arpabet in sibilant_arpabet_lst:
                words_counter['sX'] += 1
            else:
                words_counter['kX'] += 1
            if dictionary[word][-1].arpabet in sibilant_arpabet_lst:
                words_counter['Xs'] += 1
            else:
                words_counter['Xk'] += 1
        elif not contain_punctuation(word):
            not_found_word_counter += 1
            if word in not_found:
                not_found[word] += 1
            else:
                not_found[word] = 1
                
    for car, cdr in zip(corpus[:-1], corpus[1:]):
        if car in dictionary and cdr in dictionary:
            sibilant_car = dictionary[car][-1].arpabet in sibilant_arpabet_lst
            sibilant_cdr = dictionary[cdr][0].arpabet in sibilant_arpabet_lst
            if sibilant_car and sibilant_cdr:
                bigrams_counter['Xs_sX'] += 1
            elif sibilant_car and not sibilant_cdr:
                bigrams_counter['Xs_kX'] += 1
            elif not sibilant_car and sibilant_cdr:
                bigrams_counter['Xk_sX'] += 1
            else:
                bigrams_counter['Xk_kX'] +=1
        elif not(contain_punctuation(car) and contain_punctuation(cdr)):
            not_found_bigrams_counter += 1

    df_not_found = pd.DataFrame(not_found, index=['count']).T
    print(df_not_found.sort_values(by='count', ascending=False).head(20))
    return words_counter, bigrams_counter

def hiatus(corpus, dictionary):
    vowels_arpabet_lst = ['AA', 'AE', 'AH', 'AO', 'W', 'AW', 'Y', 'AY', 'EH', 'R', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
    not_found = dict()
    not_found_word_counter = 0
    not_found_bigrams_counter = 0
    words_counter = {
        'VX': 0,
        'CX': 0,
        'XV': 0,
        'XC': 0
    }
    bigrams_counter = {
        'XV_VX': 0,
        'XV_CX': 0,
        'XC_VX': 0,
        'XC_CX': 0
    }
    # Data from independent words
    for word in corpus:
        if word in dictionary:
            if dictionary[word][0].arpabet in vowels_arpabet_lst:
                words_counter['VX'] += 1
            else:
                words_counter['CX'] += 1
            if dictionary[word][-1].arpabet in vowels_arpabet_lst:
                words_counter['XV'] += 1
            else:
                words_counter['XC'] += 1
        elif not contain_punctuation(word):
            not_found_word_counter += 1
            if word in not_found:
                not_found[word] += 1
            else:
                not_found[word] = 1
                
    for car, cdr in zip(corpus[:-1], corpus[1:]):
        if car in dictionary and cdr in dictionary:
            vowels_car = dictionary[car][-1].arpabet in vowels_arpabet_lst
            vowels_cdr = dictionary[cdr][0].arpabet in vowels_arpabet_lst
            if vowels_car and vowels_cdr:
                bigrams_counter['XV_VX'] += 1
            elif vowels_car and not vowels_cdr:
                bigrams_counter['XV_CX'] += 1
            elif not vowels_car and vowels_cdr:
                bigrams_counter['XC_VX'] += 1
            else:
                bigrams_counter['XC_CX'] +=1
        elif not(contain_punctuation(car) and contain_punctuation(cdr)):
            not_found_bigrams_counter += 1

    df_not_found = pd.DataFrame(not_found, index=['count']).T
    print(df_not_found.sort_values(by='count', ascending=False).head(20))
    return words_counter, bigrams_counter

def sibilant_clash_with_hiatus(corpus, dictionary):
    sibilant_arpabet_lst = ['S', 'Z', 'SH', 'ZH']
    vowels_arpabet_lst = ['AA', 'AE', 'AH', 'AO', 'W', 'AW', 'Y', 'AY', 'EH', 'R', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
    bigrams_counter = {
        'Xs_sX': 0,
        'Xs_kCX': 0,
        'Xs_VX': 0,
        'XkC_sX': 0,
        'XV_sX': 0,
        'XkC_kCX': 0,
        'XkC_VX': 0,
        'XV_kCX': 0,
        'XV_VX': 0
    }
    # Data from independent words 
    for car, cdr in zip(corpus[:-1], corpus[1:]):
        if car in dictionary and cdr in dictionary:
            sibilant_car = dictionary[car][-1].arpabet in sibilant_arpabet_lst
            sibilant_cdr = dictionary[cdr][0].arpabet in sibilant_arpabet_lst
            vowels_car = dictionary[car][-1].arpabet in vowels_arpabet_lst
            vowels_cdr = dictionary[cdr][0].arpabet in vowels_arpabet_lst
            if sibilant_car and sibilant_cdr:
                bigrams_counter['Xs_sX'] += 1
            if sibilant_car and not sibilant_cdr and not vowels_cdr:
                bigrams_counter['Xs_kCX'] += 1
            if sibilant_car and vowels_cdr:
                bigrams_counter['Xs_VX'] += 1
            if not sibilant_car and not vowels_car and sibilant_cdr:
                bigrams_counter['XkC_sX'] += 1
            if vowels_car and sibilant_cdr:
                bigrams_counter['XV_sX'] += 1
            if not sibilant_car and not vowels_car and not sibilant_cdr and not vowels_cdr:
                bigrams_counter['XkC_kCX'] += 1
            if not sibilant_car and not vowels_car and vowels_cdr:
                bigrams_counter['XkC_VX'] += 1
            if vowels_car and not sibilant_cdr and not vowels_cdr:
                bigrams_counter['XV_kCX'] += 1
            if vowels_car and vowels_cdr:
                bigrams_counter['XV_VX'] += 1

    return  bigrams_counter
