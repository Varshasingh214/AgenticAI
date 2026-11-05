import configparser

env = 'SIT'

# object of configParser:
config = configparser.ConfigParser()
config.read('calcparam.properties')
# print(config.sections())
if not env:
    env = 'DEFAULT'
    print(config[env]['n1'])

# read values from config file
num1=int(config[env]['num1'])
num2=int(config[env]['num2'])
operation= int(config[env]['operation'])

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

