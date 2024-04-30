#!/usr/bin/python3

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()

for line in data.splitlines():
    print("- " + line.decode('utf-8'))
