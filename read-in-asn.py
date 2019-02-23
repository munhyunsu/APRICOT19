import pickle
d = dict()
asn_data=open('ans-sample.txt','r')
for line in asn_data:
	asn = line.split(' ')[0]
	asn = asn.strip()
	ctr = line.split(' ')[-1]
	ctr = ctr.strip()
	if ctr not in d:
		d[ctr] = list()
	d[ctr].append(asn)
print(d)

