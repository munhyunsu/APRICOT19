#!/bin/bash

echo "Download ASN files"
wget https://ftp.ripe.net/ripe/asnames/asn.txt -O asn.txt

echo "Convert file encoding to UTF-8"
iconv -f LATIN1 -t UTF-8 asn.txt -o asn_utf-8.txt
mv asn_utf-8.txt asn.txt

echo "Create python3 venv"
python3 -m venv ./venv

echo "Install(pip3) some package"
source ./venv/bin/activate
pip3 install --upgrade pip setuptools
pip3 install -r requirements.txt

echo "Create pickle"
python3 create_asn_country_pickle.py

echo "Done! you can execute start.py"
echo "Command: python3 start.py"

