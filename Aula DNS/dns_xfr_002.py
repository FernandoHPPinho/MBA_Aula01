#!/usr/bin/python

import dns.query
import dns.zone

domain = 'anarelo.dojo'
target = 'ns.yellow.dojo'

try:
    transfzone = dns.zone.from_xfr(dns.query.xfr(target, domain))

    for _machines in transfzone:
        print('[+] -', str(_machines) + '.' + domain)

except:
    print('[!] - Falha transferencia de zona dominio:',  domain, 'NS:' , target)
