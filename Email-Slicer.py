#!/usr/bin/env python3



def esp(e):
    if '@@' in e or '@' not in e:
        print('Invalid email format')
    else:
        split = email.split('@')
        user = split[0]
        domain = split[1]

        print('Username:', user)
        print('Domain:', domain)


email = input('email: ')
esp(email)        
