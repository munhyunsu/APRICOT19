import os
import json
import time
import random

from ihr_crawler.crawler import get_hegemony, get_transit
from ripe_crawler.crawler import get_prefix

def main():
    os.makedirs('./data/', exist_ok=True)
    for asn in range(1, 10000):
        filepath = os.path.join('./data/', '{0}.json'.format(asn))
        if os.path.exists(filepath):
            print('Exists: {0}'.format(filepath))
            continue
        data = get_hegemony(asn)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=True, ensure_ascii=False)
        print('Saved: {0}'.format(filepath))
        time.sleep(random.randint(1, 3))

def get_data(asn):
    os.makedirs('./data/', exist_ok=True)
    filepath = os.path.join('./data/', '{0}.json'.format(asn))
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    else:
        data = get_hegemony(asn)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=True, ensure_ascii=False)
        print('New saved: {0}'.format(filepath))
        time.sleep(random.randint(0, 3))
    return data

def is_stub(asn):
    os.makedirs('./data_transit/', exist_ok=True)
    filepath = os.path.join('./data_transit/', '{0}.json'.format(asn))
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    else:
        data = get_transit(asn)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=True, ensure_ascii=False)
        print('New transit saved: {0}'.format(filepath))
        time.sleep(random.randint(0, 3))
    stub = True
    asn = int(asn)
    for result in data['results']:
        if int(result['originasn']) != 0 and int(result['originasn']) != asn:
            stub=False
            break
    return stub


def get_customer(asn):
    os.makedirs('./data_prefix/', exist_ok=True)
    filepath = os.path.join('./data_prefix/', '{0}.json'.format(asn))
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
    else:
        data = get_prefix(asn)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=True, ensure_ascii=False)
        print('New prefix saved: {0}'.format(filepath))
        time.sleep(random.randint(0, 3))
    return data


if __name__ == '__main__':
    main()

