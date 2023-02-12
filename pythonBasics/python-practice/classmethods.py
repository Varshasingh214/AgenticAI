'''
Class methods: is a method which is bound to a class.
'''
class Animal:

    # n = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @classmethod
    def times(cls, t=2):
        n = t
        return n

    def increment_salary(self,t):
        print("new sal : ", self.salary * Animal.times())

    #using classmethod as an alternative constructor
    @classmethod
    def from_str(cls,tiger_string):
        fname,lname, salary = tiger_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod
    def isgreater(size):
        if size == tiger:
            return True
        else:
            return False

# call
cat = Animal('bobby', 'khan' , 100)
dog = Animal('tommy', 'singh', 200)
tiger = Animal.from_str("shera-thakur-250")                   # from_str is for parsing the string

print(Animal.isgreater(tiger))
cat.increment_salary(3)
dog.increment_salary(2)
print(tiger.fname)
print(tiger.increment_salary(2))