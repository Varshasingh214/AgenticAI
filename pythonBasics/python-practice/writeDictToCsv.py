import csv

mydict={"name":"varsha", "company":"citi", "designation":"TL"}

# field name:
fields = ['name','company', 'designation']

# name of csv file
filename = 'mycsv.csv'

# writing to csv file
with open(filename, 'a') as f:
    # creating csv dict writer object
    writer = csv.DictWriter(f, fieldnames=fields)
    # writing headers (fieldnames)
    writer.writeheader()
    # writing data rows
    writer.writerow(mydict)