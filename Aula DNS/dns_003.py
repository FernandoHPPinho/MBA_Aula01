#!/usr/bin/python3.6
import dns.resolver
from termcolor import colored

myquery = dns.resolver.Resolver()
domain = "uol.com.br" 
lista = [ 'www','www1', 'www2', 'www3', 'admin', 'route', 'vpn', 'siem', 'fw', 'firewall' ]

def dns_tipoa(_host):
    try:
        _answers = myquery.query(_host, 'AAAA')

        for _hostA in _answers:
            return  _hostA
    except:
        pass

def dns_listquery():
    for _word in lista:
        _host = str(_word + "." + domain)
        dns_result = dns_tipoa(_host)
        
        if dns_result is not None:
            print(colored('[*]', 'cyan'),_word, "--> ", _host, dns_result)


dns_listquery()
