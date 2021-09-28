import random
from typing import Counter

colorlist = ["oranje","blauw","groen","bruin"]


mnmamnt = input("Hoeveel M&M's wil je in je zak? ")

def addToBag(count):
    mnmzak = []

    for i in range(int(count)):
        choice = random.choice(colorlist)
        mnmzak.append(choice)

    
    return mnmzak

print(addToBag(mnmamnt))


