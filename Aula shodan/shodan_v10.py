#!/usr/bin/python

import shodan
shodan_mykey='boYedPn8iDWi6GDSO6h2kz72VLt6bZ3S'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_item='Microsoft-IIS/8.0 country:"BR"'
shodan_item='Microsoft-IIS/8.0'
shodan_result = shodan_api.search(shodan_item)

def shodan_search():
    print('Buscar por:', shodan_item)
    print('Numero de ocorrencia:',shodan_result['total'])

    print('[*] - ........:: TOP 100 ::......',shodan_result['total'])

    count = 1
    
    for _result in shodan_result['matches']:
        print('[+] - Possivel alvo',count, 'IP:', _result['ip_str'])
        count = count +1
        
shodan_search()

