import pickle

data = dict()

with open('asn.txt', 'r', encoding='utf-8') as f:
    for line in f:
        splited_line = line.split(' ')
        asn = splited_line[0].strip()
        ctr = splited_line[-1].strip()
        if ctr not in data:
            data[ctr] = list()
        data[ctr].append(asn)

with open('asn.pickle', 'wb') as f:
    pickle.dump(data, f)

