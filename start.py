import sys
import pickle
import statistics

from operator import itemgetter

from scrap_data import get_data

ARGS = None


def main():
    with open('asn.pickle', 'rb') as f:
        asn_data = pickle.load(f)
    print('Load data: {0}'.format(list(asn_data.keys())))

    ctr = input('Input the country code: ')
    ctr = ctr.strip()
    
    print('The number of ASNs: {0}'.format(len(asn_data[ctr])))

    asn_hege = dict()
    asn_name = dict()
    active_asn = 0

    for origin_asn in asn_data[ctr]:
        for result in get_data(origin_asn)['results']:
            asn = int(result['asn'])
            hege = float(result['hege'])
            name = result['asn_name']
            if asn not in asn_hege:
                asn_hege[asn] = list()
            asn_hege[asn].append(hege)
            asn_name[asn] = name
            if asn == int(origin_asn):
                active_asn = active_asn + 1

    asn_avg = list()
    for key in asn_hege.keys():
        asn_avg.append((key, sum(asn_hege[key])/active_asn))
    asn_avg.sort(key=itemgetter(0), reverse=False)
    asn_avg.sort(key=itemgetter(1), reverse=True)

    for key, value in asn_avg:
        if ARGS.verbosity is not None:
            name = asn_name[key]
            print('ASN: {0:7d} - {1:1.4f} ({2})'.format(key, value, name))
        else:
            print('ASN: {0:7d} - {1:1.4f}'.format(key, value))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', action='count',
                        help='increase output verbosity')

    ARGS = parser.parse_args()

    main()
