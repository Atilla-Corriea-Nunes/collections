import random

colorlist = ["oranje","blauw","groen","bruin"]


mnmamnt = input("Hoeveel M&M's wil je in je zak? ")

def addToBag(count):
    mnmzak = {}

    for i in range(int(count)):
        choice = random.choice(colorlist)
        if choice in mnmzak:
            mnmzak[choice] += 1
        else:
            mnmzak.update({choice : 1})
    return mnmzak


sorted_bag = sorted(addToBag(mnmamnt).items(), key= lambda kv:
kv[1])


print(sorted_bag)

