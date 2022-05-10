def load_corpus(filename):
    data = open(filename, 'r').read()
    data = data.split(' ')
    return data

