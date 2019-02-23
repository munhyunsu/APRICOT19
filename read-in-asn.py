import pickle

d = dict()
#asn_data = open('asn.txt', 'r', encoding='utf-8')

with open('asn-sample.txt', 'r', encoding='utf-8') as asn_data:
    for line in asn_data:
        asn = line.split(' ')[0]
        asn = asn.strip()
        ctr = line.split(' ')[-1]
        ctr = ctr.strip()
        if ctr not in d:
            d[ctr] = list()
        d[ctr].append(asn)

with open('asn.pickle', 'wb') as f:
    pickle.dump(d, f)

