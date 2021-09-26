#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
target = "yahoo.com"

def func_ns(_target):
    question = myquery.query(_target, 'NS')

    for _ns in question:
        print("[+] - ",_ns)


def func_mx(_target):
    question = myquery.query(_target, 'MX')

    for _mx in question:
        print(_mx)


def func_txt(_target):
    question = myquery.query(_target, 'TXT')

    for _txt in question:
        print(_txt)

print("#" * 60)
print("Consultas classicas de DNS - NS, MX, TXT")

def func_dnsenum(target):
    print("Lista de servidores TXT do dominio")
    func_txt(target)
    print()
    print("Lista de servidores DNS do dominio")
    func_ns(target)
    print()
    print("Lista de servidores MX (Mail exchange do dominio")
    func_mx(target)

func_dnsenum(target)
