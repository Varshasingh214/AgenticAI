import sys

# sys.argv is a list which contains all the command line arguments; it always takes string value
# sys.argv[0] is the name of script itself

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operation = int(sys.argv[3])

result = 0

if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    result = num1/num2

else:
    print(" wrong choice")

# positional argument: we rely on the order of arguments to give the value to parameters.
print(f"{num1} {num2} {operation} gives {result}")


