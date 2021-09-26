#!/usr/bin/python

### skeletor libraries
import argparse
import sys
import dns.resolver
from pyfiglet import Figlet
from termcolor import colored

#### variaveis argpase - skeletor
nome_app = str(sys.argv[0])
msg_usage = "\n Usage: python3 " + nome_app + " -d <dominio alvo> -w <wordlist> \n" 
msg_domain = "Informe o dominio alvo" 
### variaveis do banner
msg_font=('puffy')
msg_banner="MyDNS Footprint" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'white')
msg_ok=colored('[+] - ','green') 
msg_att=colored('[!] - ','yellow') 
msg_wordlist = msg_att + "Informe a wordlist" 
msg_version = "Version: 0.1 " 

myquery = dns.resolver.Resolver()
target = "yahoo.com"

def func_version():
    print(msg_banner_color)
    print(" -------------------------------------------------------------------> " + msg_version)
    print()

func_version()
### skeletor

################ Inicio do seu codigo - funcao consultas classicas

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

#func_dnsenum(target)

################ Fim do seu codigo


################ Inicio do seu codigo - funcao forca bruta IPv4

 
################ Fim do seu codigo

################ Inicio do seu codigo - funcao forca bruta IPv6


################ Fim do seu codigo

    
################ Inicio do seu codigo - funcao traferencia de zona


################ Fim do seu codigo

    

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-d",'--domain', action="store", dest="domain",  help=msg_domain)
    option.add_argument("-w",'--wordlist', action="store", dest="wordlist", default='wordlist.txt',  help=msg_wordlist)
    option.add_argument("-v",'--version', action="store_true", dest="version",  help=msg_version)
    option_args = option.parse_args()

    if option_args.version:
        func_version()
    
    if option_args.domain == None:
        print(option.description)
        exit(0)
    else:
        func_dnsenum(option_args.domain)

    domaintarget = option_args.domain
    #func_XXXXXXXXX(domaintarget)

if __name__ == '__main__':
    func_main()
#
