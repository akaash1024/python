# def addFrosting(func):
#     def decoratedCake():
#         print("before")
#         func()
#         print("After")
#     return decoratedCake
# @addFrosting
# def bakeCake():
#     print("Baking plain cake")

# bakeCake()


def addFrosting(func):
    def decoratedCake():
        print("before")
        func()
        print("After")
    return decoratedCake

def bakeCake():
    print("Baking plain cake")
    
x = addFrosting(bakeCake)
x()