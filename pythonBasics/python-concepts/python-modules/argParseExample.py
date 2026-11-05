import argparse

# Initialize parser
# argparse module is used to create a parser object
parser = argparse.ArgumentParser()

# Adding optional argument
# add_argument() method is used to specify the arguments that the script can accept.
parser.add_argument("-n1", "--num1", help="pass 1st number")
parser.add_argument("-n2", "--num2", help="pass 2st number")
parser.add_argument("-o", "--operator", help="operation to perform")

# Read arguments from command line
# parse_args() method is used to parse the arguments provided by the user
args = parser.parse_args()

if True:
    print("Displaying first num as: {num1}")
    print("Displaying second num as:{num2}")
    print("Displaying Operation as: {operator}")

num1 = int(args.num1)
num2 = int(args.num2)
operation = int(args.operator)

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

# keyword argument: we explicitly define values to each parameters
print(f"the result is {result} ")

