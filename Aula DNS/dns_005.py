#!/usr/bin/python

import dns.resolver
from termcolor import colored
from threading import *

msgattackipv4 = " Iniciando o FOOTPRINT - DNS Bruteforce - IPv4" 
msgattackipv6 = " Iniciando o FOOTPRINT - DNS Bruteforce - IPv6" 
myquery = dns.resolver.Resolver()
domain = "uol.com.br" 

### IPv4
def dns_tipoa(_host):
    try:
        _answers = myquery.query(_host, 'A')

        for _hostA in _answers:
            return  _hostA
    except:
        pass

def dns_listquery_ipv4(_word):
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
                dns_listquery_ipv4(machine)

            except: 
                pass

### IPv6


def dns_tipoipv6(_host):
    try:
        _answers = myquery.query(_host, 'AAAA')

        for _hostA in _answers:
            return  _hostA
    except:
        pass

def dns_listquery_ipv6():
    for _word in lista:
        _host = str(_word + "." + domain)
        dns_result = dns_tipoipv6(_host)
        
        if dns_result is not None:
            print(colored('[*]', 'cyan'),_word, "--> ", _host, dns_result)


def bruteforce_dns_ipv6(_wordlist,_target):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")
        
            if not machine:
                break 

            try:
                dns_listquery_ipv6(machine)

            except: 
                pass



### IPv4 enumeration
def func_ipv4_enum():
    fastway = Thread(target=bruteforce_dns_ipv4,args=("wordlist.txt",domain))
    print( colored('[*]','blue'), msgattackipv4)
    fastway.start()

### IPv6 enumeration
def func_ipv6_enum():
    fastway = Thread(target=bruteforce_dns_ipv6,args=("wordlist.txt",domain))
    print( colored('[*]','blue'), msgattackipv6)
    fastway.start()


def func_attack():
    func_ipv4_enum()
    func_ipv6_enum()
    
func_attack()


