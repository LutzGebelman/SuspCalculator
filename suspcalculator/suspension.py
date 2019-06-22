def susp():
    from decimal import Decimal
    import os

    i = 0
    stab = "antiroll bars: "
    spring = "springs: "
    damp = "dampers: "

    while i != 1:  
        os.system('cls' if os.name == 'nt' else 'clear')

        minfin = "Enter minimum value for front "
        maxfin = "Enter maximum value for front "
        minrin = "Enter minimum value for rear "
        maxrin = "Enter maximum value for rear "

        a = int(input("What are you calculating?\n1 - Antiroll Bars\n2 - Springs\n3 - Dampers\n\n"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if a == 1:
            b = "antiroll bars: "

        elif a == 2:
            b = "springs: "
            
        elif a == 3:
            b = "dampers: "

        else:
            input("Invalid character entered")
            break

        minfin = minfin + b
        maxfin = maxfin + b
        minrin = minrin + b
        maxrin = maxrin + b

        fwp = Decimal(input("Enter front load: "))

        os.system('cls' if os.name == 'nt' else 'clear')

        if fwp >= 1:
            fwp=fwp/100

        rwp = Decimal(1-fwp)

        fdmin = Decimal(input(minfin))
        fdmax = Decimal(input(maxfin))

        os.system('cls' if os.name == 'nt' else 'clear')

        rdmin = Decimal(input(minrin))
        rdmax = Decimal(input(maxrin))

        os.system('cls' if os.name == 'nt' else 'clear')

        resoltf = ((fdmax-fdmin)*fwp)+fdmin
        resoltr = ((rdmax-rdmin)*rwp)+rdmin

        resoltf = round(resoltf,1)
        resoltr = round(resoltr,1)

        
        print("value for front " + b, resoltf)
        print("value for rear " + b, resoltr)
        
        if a == 3:
            resfc = resoltf*Decimal(0.6)
            resrc = resoltr*Decimal(0.6)

            resfc = round(resfc, 1)
            resrc = round(resrc, 1)

            print("value for front damper on bump stiffness: ", resfc)
            print("value for rear damper on bump stiffness: ", resrc )

        if int(input("\nSave result?\n 1 - yes\n 0 - no\n\n")) == 1:
            f = open('history.txt', 'a+')
            f.write("\nValue for front " + b + str(resoltf) + "\nValue for rear " + b + str(resoltr) )
            f.close()
        i = i+1