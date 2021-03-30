from ast import literal_eval

balance = 0
check = str
ptrx = str
pk = str
print("Welcome to PyCoin Wallet!")
print(" ")
print("/create - create wallet")
print("/import - import wallet (private key)")
print(" ")
wlcmd = input("$cmd = ")
if wlcmd == "/create":
    print("Wallet created!")
    print(" ")
    i = 1
    while i > 0:
        prblnc = balance + 2403671917315073614680224758485033610754121567618907204083050215737715695785
        print("Cmd list:")
        print("/receive - get PyCoin")
        print("/send - send your PyCoin (generate transaction key)")
        print("/pk - show your private key (for importing your wallet)")
        print("/balance - show your balance")
        print(" ")
        cmd = input("$wallet = ")
        if cmd == "/pk":
            pk = hex(prblnc)
            print(" ")
            print("Your private key - "+ pk)
            print(" ")
        if cmd == "/balance":
            print(" ")
            print("Your balance - "+ str(balance)+ " CPN")
            print(" ")
        if cmd == "/receive":
            trxk = input("Paste transaction/mining key - ")
            if trxk == check:
                print("Fail")
            if trxk == ptrx:
                print("Fail")
            if trxk == pk:
                print("Fail")
            else:
                res = literal_eval(trxk)
                newbalance = balance + res - 2403671917315073614680224758485033610754121567618907204083050215737715695785
                balance = newbalance
                print("Transaction confirmed!")
                print("New balance - " + str(balance)+ " CPN")
                print(" ")
                check = trxk
        if cmd == "/send":
            amnt = int(input('Type amount of funds - '))
            if amnt < balance:
                if amnt < 0:
                   print('Fail')
                else:
                   balance = int(balance) - int(amnt)
                   pamnt = amnt + 2403671917315073614680224758485033610754121567618907204083050215737715695785
                   ptrx = hex(pamnt)
                   print('Send this transaction key to receiver - ' + str(ptrx))
            else:
                print('Not enough funds to make this operation :(')
            print('Final balance - ' + str(balance)+ " CPN")
if wlcmd == "/import":
    pkimpt = input("Type your private key - ")
    res = literal_eval(pkimpt)
    newbalance = balance + res - 2403671917315073614680224758485033610754121567618907204083050215737715695785
    balance = newbalance
    print("Wallet imported!")
    print("Your balance - "+str(balance)+" CPN")
    print(" ")
    i = 1
    while i > 0:
        prblnc = balance + 2403671917315073614680224758485033610754121567618907204083050215737715695785
        print("Cmd list:")
        print("/receive - get PyCoin")
        print("/send - send your PyCoin (generate transaction key)")
        print("/pk - show your private key (for importing your wallet)")
        print("/balance - show your balance")
        print(" ")
        cmd = input("$wallet = ")
        if cmd == "/pk":
            pk = hex(prblnc)
            print(" ")
            print("Your private key - "+ pk)
            print(" ")
        if cmd == "/balance":
            print(" ")
            print("Your balance - "+ str(balance)+ " CPN")
            print(" ")
        if cmd == "/receive":
            trxk = input("Paste transaction/mining key - ")
            if trxk == check:
                print("Fail")
            if trxk == ptrx:
                print("Fail")
            if trxk == pk:
                print("Fail")
            else:
                res = literal_eval(trxk)
                newbalance = balance + res - 2403671917315073614680224758485033610754121567618907204083050215737715695785
                balance = newbalance
                print("Transaction confirmed!")
                print("New balance - " + str(balance)+ " CPN")
                print(" ")
                check = trxk
        if cmd == "/send":
            amnt = int(input('Type amount of funds - '))
            if amnt < balance:
                if amnt < 0:
                   print('Fail')
                else:
                   balance = int(balance) - int(amnt)
                   pamnt = amnt + 2403671917315073614680224758485033610754121567618907204083050215737715695785
                   ptrx = hex(pamnt)
                   print('Send this transaction key to receiver - ' + str(ptrx))
            else:
                print('Not enough funds to make this operation :(')
            print('Final balance - ' + str(balance)+ " CPN")
