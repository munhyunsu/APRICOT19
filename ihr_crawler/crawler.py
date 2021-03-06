import time
import requests

def get_hegemony(originasn, timebin='2019-02-22+00:00'):
    url = 'https://ihr.iijlab.net/ihr/api/hegemony/?af=4&format=json&ordering=-hege&originasn={0}&timebin={1}'.format(originasn, timebin)

    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None
        
def get_transit(asn, timebin='2019-02-22+00:00'):
    url = 'https://ihr.iijlab.net/ihr/api/hegemony/?af=4&format=json&ordering=-hege&asn={0}&timebin={1}'.format(asn, timebin)

    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None

def get_percent(ctr):
    url = 'http://v6data.data.labs.apnic.net/ipv6-measurement/Economies/{0}/{0}.asns.json?m=0.01'.format(ctr)

    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    print(get_hegemony(originasn=2501))

