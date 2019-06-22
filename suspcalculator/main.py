import suspension
import os
f = open('history.txt', 'rt')

pend = 0

while pend != 1:
    os.system('cls')
    inmenu = int(input("1. Suspention Calculaton\n2. History\n3. Exit\n\n"))
    if inmenu == 1:
        suspension.susp()
    elif inmenu == 2:
        data = f.read()
        print(data)
        input()
    elif inmenu == 3:
        pend = 1
        f.close()