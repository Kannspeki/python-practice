
#!/usr/bin/env python3

# 2022-05-13 

import sys

length = int(input('Lenght of sequence: '))

def sum(l):
    z = 0
    w = [1]

    if l >= 10000:
        safe = input('Such large sequence might cause slowdown. Want to proceed? y/n ')
        if safe == 'n' or safe == 'N':
            sys.exit(1)
    for i in range(l - 2):
        z = z + w[i - 1]
        w.append(z)
    print(0, end=', ')    
    print(", ".join(map (str, w)))



sum(length)


    




