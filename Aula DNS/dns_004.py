#!/usr/bin/python3.6

import dns.resolver
from termcolor import colored
from threading import *

msgattack = " Iniciando o FOOTPRINT - DNS Bruteforce" 
myquery = dns.resolver.Resolver()
domain = "megacorpone.com" 

def dns_tipoa(_host):
    try:
        _answers = myquery.query(_host, 'A')

        for _hostA in _answers:
            return  _hostA
    except:
        pass

def dns_listquery(_word):
    _host = str(_word + "." + domain)
    dns_result = dns_tipoa(_host)
        
    if dns_result is not None:
        print(colored('[*]', "green"),_word, "--> ", _host, dns_result)


def bruteforce_dns_ipv4(_wordlist,_target):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")
        
            if not machine:
                break 

            try:
                dns_listquery(machine)

            except: 
                pass




### IPv4 enumeration
fastway = Thread(target=bruteforce_dns_ipv4,args=("word2.txt",domain))
print( colored('[*]','blue'), msgattack)
fastway.start()

### IPv6 enumeration
