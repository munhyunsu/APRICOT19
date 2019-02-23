import sys
import pickle
import statistics

from operator import itemgetter

from scrap_data import get_data

def main():
    with open('asn.pickle', 'rb') as f:
        asn_data = pickle.load(f)
    print('Load data: {0}'.format(list(asn_data.keys())))

    ctr = input('Input the country code: ')
    ctr = ctr.strip()
    
    print('ASNs: {0}'.format(asn_data[ctr]))

    asn_hege = dict()
    asn_name = dict()

    for asn in asn_data[ctr]:
        for result in get_data(asn)['results']:
            asn = int(result['asn'])
            hege = float(result['hege'])
            name = result['asn_name']
            if asn not in asn_hege:
                asn_hege[asn] = list()
            asn_hege[asn].append(hege)
            asn_name[asn] = name

    asn_avg = list()
    for key in asn_hege.keys():
        asn_avg.append((key, statistics.mean(asn_hege[key])))
    asn_avg.sort(key=itemgetter(0), reverse=False)
    asn_avg.sort(key=itemgetter(1), reverse=True)

    for key, value in asn_avg:
        print('ASN: {0:7d} - {1:1.4f}'.format(key, value))


if __name__ == '__main__':
    main()
