#!/usr/bin/python

import shodan
shodan_mykey='boYedPn8iDWi6GDSO6h2kz72VLt6bZ3S'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target='179.191.78.194'
shodan_host = shodan_api.host(shodan_target)

def shodan_portscan():
    for _line in shodan_host['data']:
        print("[+] - Porta Aberta:", _line['port'])


shodan_portscan()



