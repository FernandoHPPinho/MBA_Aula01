#!/usr/bin/python
import argparse
import whois



msg_usage ="\n Use assim: ./whois_004.py -d <domini alvo> \n"
msg_domain = "Informe o nome do dominio alvo"

def func_whois(_domain):
        querywhois = whois.query(_domain)
        print("[+] - Nome do dominio", querywhois.name)
        print("[+] - Data de criacao: ", querywhois.creation_date)
        print("[+] - Data de Expiracao? " , querywhois.expiration_date)
        print("[+] - Servidor Whois registrado:", querywhois.registrar)
        print("[+] - SData de ultima atualizacao", querywhois.last_updated)

        for _domain in querywhois.name_servers:
            print("[+] - Servidor de Nomes", _domain)

def func_main():
        option = argparse.ArgumentParser(description=msg_usage)
        option.add_argument("-d","--domain", action="store", dest="domain", help=msg_domain)
        option_args = option.parse_args()

        if option_args.domain == None:
            print(option.description)
        
        domaintarget = option_args.domain
        func_whois(domaintarget)

if __name__ == '__main__':
    func_main()
