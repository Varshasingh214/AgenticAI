#Available in python 3.7
from dataclasses import dataclass

@dataclass
class TestDC():
    name: str
    id: int
    address: str = 'Patna'

dict1 = {'address': 'Pune','name': 'vivek', 'id': 1}
dict2 = {'name': 'vivek', 'id': 1, 'address': 'Pune'}



class Testnew():

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def __eq__(self, other):
        self.a == other.a
        self.b == other.b


# person1 = TestDC(**dict1)
# print(person1.address)


obj1 = Testnew(2,3)
obj2 = Testnew(2,3)

print(id(obj1))
print(id(obj2))
print(obj1 == obj2)
