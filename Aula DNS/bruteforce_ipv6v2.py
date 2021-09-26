#!/usr/bin/python
import dns.resolver
from threading import *

myquery = dns.resolver.Resolver()
domain = "yahoo.com"

def func_a(_target):
    question = myquery.query(_target, 'AAAA')

    for _addr in question:
        print('[+] - ' + _target + '---->' + str(_addr))

def bruteforce_dns_ipv6(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break

            try:
                target = machine + "." + domain
                func_a(target)
            except:
                pass

#bruteforce_dns_ipv6("file.txt"et
thread_ipv6 = Thread(target=bruteforce_dns_ipv6,args=('file.txt',))
thread_ipv6.start()

