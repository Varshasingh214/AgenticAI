import argparse
import configparser

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-e", "--env", help="Execution Environment Name")
parser.add_argument("-n1", "--num1", help="1st Number ")
parser.add_argument("-n2", "--num2", help="Execution Environment Name")
parser.add_argument("-o", "--operation", help="Execution Environment Name")

# Read arguments from command line
args = parser.parse_args()

# get env name from runtime params:
env = args.env
n1 = args.num1
n2 = args.num2
op = args.operation

# object of configParser:
config = configparser.ConfigParser()
config.read('calcparam.properties')
print(config.sections())

# read values from config file
num1=int(config[env]['num1'])
num2=int(config[env]['num2'])
operation= int(config[env]['operation'])

# overwrite config with runtime params
if n1 is not None:
    print("overwriting num1 of config with runtime num1")
    num1 = int(n1)
if n2:
    print("overwriting num2 of config with runtime num2")
    num2 = int(n2)
if op:
    print("overwriting operation of config with runtime operation")
    operation = int(op)


result = 0

if True:
    print(f"Displaying first num as: {num1}")
    print(f"Displaying second num as: {num2}")
    print(f"Displaying Operation as: {operation}")

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

