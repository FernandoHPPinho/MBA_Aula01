#!/usr/bin/python


import whois
target = "google.com"

def func_whois(_domain):
        querywhois = whois.query(_domain)
        print("[+] - Nome do dominio", querywhois.name)
        print("[+] - Data de criacao: ", querywhois.creation_date)
        print("[+] - Data de Expiracao? " , querywhois.expiration_date)
        print("[+] - Servidor Whois registrado:", querywhois.registrar)
        print("[+] - SData de ultima atualizacao", querywhois.last_updated)

        for _domain in querywhois.name_servers:
            print("[+] - Servidor de Nomes", _domain)

func_whois(target)
