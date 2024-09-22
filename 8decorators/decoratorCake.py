def addFrosting(func):
    def decoratedCake():
        print("before")
        func()
        print("After")
    return decoratedCake

@addFrosting       #backCake = addFrosting(bakeCake)
def bakeCake():
    print("Baking plain cake")

bakeCake()