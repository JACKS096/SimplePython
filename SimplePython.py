
class Parrot:

    
    species = "птица"

    
    def __init__(self, name, age):
        self.name = name
        self.age = age


kesha = Parrot(" еша", 10)
cookie = Parrot(" уки", 15)


print(" еша Ч {}".format(kesha.__class__.species))
print(" уки тоже {}".format(cookie.__class__.species))


print("{} Ч {}-летний попугай".format(kesha.name, kesha.age))
print("{} Ч {} летний попугай".format(cookie.name, cookie.age))