
class Parrot:

    
    species = "�����"

    
    def __init__(self, name, age):
        self.name = name
        self.age = age


kesha = Parrot("����", 10)
cookie = Parrot("����", 15)


print("���� � {}".format(kesha.__class__.species))
print("���� ���� {}".format(cookie.__class__.species))


print("{} � {}-������ �������".format(kesha.name, kesha.age))
print("{} � {} ������ �������".format(cookie.name, cookie.age))