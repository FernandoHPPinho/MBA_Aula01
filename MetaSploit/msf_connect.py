#!/usr/bin/python

from pymetasploit3.msfrpc import *
from pymetasploit3.msfconsole import *
import sys


###

MSG_CONN = '[*] - Keep Walking - Conexao via MSFRPCD - like magic'
MSG_CONS = '[*] - Look - Exploiting right now - The Power of Metasploit '

def printline_number(number):
    print('='* + int(number))

printline_number(70)
printline_number(70)
print (str(MSG_CONN))

try:
    client = MsfRpcClient('123',ssl=False, port=55553)
except:
    print("[!] - Erro ao conectar ao Msfrpcd, verifique o servico")
    printline_number(70)
    sys.exit(1)
else:
    print("[*] - Conexao com Msfrpcd realizada com sucesso!")
    print(str(MSG_CONS))
finally:
    print()
    print("[*] - Good Hunter")
    printline_number(70)

