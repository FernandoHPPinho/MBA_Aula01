#!/usr/bin/python


import whois
target = "google.com"

querywhois = whois.query(target)


print(querywhois.name)

print(querywhois.creation_date)
print(querywhois.expiration_date)
print(querywhois.registrar)
print(querywhois.last_updated)

for _domain in querywhois.name_servers:
    print(_domain)
