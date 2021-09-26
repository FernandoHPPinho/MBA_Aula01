#!/usr/bin/python
import dns.resolver
import argparse
from termcolor import colored

myquery = dns.resolver.Resolver()
domain = "megacorpone.com" 
query_type = [ 'SOA', 'NS', 'MX', 'TXT' ]


def func_dnsfoot(_domain):
    print("OK")
    for _type in query_type:
        answers = myquery.query(_domain, _type)
        
        for _result in answers:
            print(colored('[*] Registro ' + _type + '  ->', 'green'), _result)

def func_main():
    parser = argparse.ArgumentParser(description='DNS Python - Register Enumeration')
    parser.add_argument('--domain', action="store", dest="domain",  default=domain)
    option = parser.parse_args() 
    domaintarget = option.domain
    func_dnsfoot(domaintarget)


if __name__ == '__main__':
    func_main()


