import random

pk = input("Type your private key - ")
print("Your private key - "+pk)
print(" ")
mined = random.randint(1, 1000)
minehash = mined
print(str(mined)+" CPN mined")
mk = hex(minehash)
print(mk+" - mining key")
input()