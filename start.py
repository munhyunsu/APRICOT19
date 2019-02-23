import sys
import pickle
import statistics

from operator import itemgetter

from scrap_data import get_data, is_stub, get_weight

ARGS = None


def main():
    as_dependency()

def as_dependency2():
    with open('asn.pickle', 'rb') as f:
        asn_data = pickle.load(f)
    print('\x1B[38;5;3mLoad data: \x1B[0m{0}'.format(list(asn_data.keys())))

    ctr = input('\x1B[1m\x1B[38;5;11mInput the country code: \x1B[0m')
    ctr = ctr.strip()

    print('\x1B[38;5;5mThe number of ASNs: \x1B[0m{0}'.format(len(asn_data[ctr])))

    asn_hege = dict()
    asn_name = dict()
    asn_active = set()

    for origin_asn in asn_data[ctr]:
        is_active = False
        tasn_hege = dict()
        tasn_name = dict()
        tasn_weight = dict()
        for result in get_data(origin_asn)['results']:
            asn = int(result['asn'])
            hege = float(result['hege'])
            name = result['asn_name']
            if asn not in tasn_hege:
                tasn_hege[asn] = list()
            tasn_hege[asn].append(hege)
            tasn_name[asn] = name
            if asn == int(origin_asn):
                is_active = True
        if is_active:
            for key in tasn_hege:
                if key not in asn_hege:
                    asn_hege[key] = list()
                asn_hege[key].extend(tasn_hege[key])
            asn_name.update(tasn_name)
            asn_active.add(origin_asn)

    asn_avg = list()
    for key in asn_hege.keys():
        asn_avg.append((key, sum(asn_hege[key])/len(asn_active)))
    asn_avg.sort(key=itemgetter(0), reverse=False)
    asn_avg.sort(key=itemgetter(1), reverse=True)

    for key, value in asn_avg:
        if ARGS.verbosity is not None:
            name = asn_name[key]
            print('\x1B[38;5;6mASN: \x1B[0m{0:7d} - {1:1.4f} ({2})'.format(key, value, name))
        else:
            print('\x1B[38;5;6mASN: \x1B[0m{0:7d} - {1:1.4f}'.format(key, value))

def as_dependency():
    with open('asn.pickle', 'rb') as f:
        asn_data = pickle.load(f)
    print('\x1B[38;5;3mLoad data: \x1B[0m{0}'.format(list(asn_data.keys())))

    ctr = input('\x1B[1m\x1B[38;5;11mInput the country code: \x1B[0m')
    ctr = ctr.strip()

    print('\x1B[38;5;5mThe number of ASNs: \x1B[0m{0}'.format(len(asn_data[ctr])))

    asn_hege = dict()
    asn_name = dict()
    asn_active = set()

    for origin_asn in asn_data[ctr]:
        is_active = False
        tasn_hege = dict()
        tasn_name = dict()
        tasn_weight = dict()
        for result in get_data(origin_asn)['results']:
            asn = int(result['asn'])
            hege = float(result['hege'])
            name = result['asn_name']
            if ARGS.stub is not None:
                if not is_stub(asn):
                    continue
            if asn not in tasn_hege:
                tasn_hege[asn] = list()
            tasn_hege[asn].append(hege)
            tasn_name[asn] = name
            if asn == int(origin_asn):
                is_active = True
        if is_active:
            for key in tasn_hege:
                if key not in asn_hege:
                    asn_hege[key] = list()
                asn_hege[key].extend(tasn_hege[key])
            asn_name.update(tasn_name)
            asn_active.add(origin_asn)

    asn_avg = list()
    for key in asn_hege.keys():
        #if ARGS.stub is not None:
        #    if not is_stub(key):
        #        continue
        if ARGS.weight is not None:
            weight = sum(asn_hege[key])/len(asn_active)*get_weight(ctr, key)/100
            #weight = sum(asn_hege[key])*get_weight(ctr, key)/100
        else:
            weight = sum(asn_hege[key])/len(asn_active)
        asn_avg.append((key, weight))
    asn_avg.sort(key=itemgetter(0), reverse=False)
    asn_avg.sort(key=itemgetter(1), reverse=True)

    for key, value in asn_avg:
        if ARGS.verbosity is not None:
            name = asn_name[key]
            print('\x1B[38;5;6mASN: \x1B[0m{0:7d} - {1:1.6f} ({2})'.format(key, value, name))
        else:
            print('\x1B[38;5;6mASN: \x1B[0m{0:7d} - {1:1.6f}'.format(key, value))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', action='count',
                        help='increase output verbosity')
    parser.add_argument('-s', '--stub', action='count',
                        help='only stub')
    parser.add_argument('-w', '--weight', action='count',
                        help='weighted value')

    ARGS = parser.parse_args()

    main()
