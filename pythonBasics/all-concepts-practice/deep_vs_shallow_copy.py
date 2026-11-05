
import copy

#shallow copy
x = [3,2,1]
y=copy.copy(x)
y[0]= 5
print(x)
print(id(x))
print(y)
print(id(y))

print("-------applying deep copy")
x = [3,2,1]
y=copy.deepcopy(x)
y[0]= 9

print(x)
print(id(x))
print(y)
print(id(y))





