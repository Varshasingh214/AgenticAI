names = ['vivek', 'varsha', 'Shivang', 'Devansh']

nums = 123456789
check = True



for i, num in enumerate(str(nums)):

    if i == len(str(nums))-1:
        break

    if int(num) < int(str(nums)[i+1]):
        continue
    else:
        print("not a valid pandigital number")
        check = False
        break
        print("after break: ")

if check:
    print("its a valid pandigital number")

# i =0
# for name in names:
#
#     print(i, " -> " , name)
#     i+=1