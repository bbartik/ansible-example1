import json
import csv
import sys

# open file and read data into a string, replacing the neewlines

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    file_data = file.read().replace('\n', '')

# convert the data to python list based on json format
# NOTE: the csv writer object requires a list to write data from

converted_data = json.loads(file_data)

# open csv file for writing and create the csv writer object

output_file = file_name[:-3] + "csv"
output_file = open(output_file, 'w')
csvwriter = csv.writer(output_file)

# initialize counter

count = 0

# Each interface object has "INTF|IPADDR|STATUS|PROTO"
# and we only want those at the top row.  The first time 
# through we add those to the csv file by using the "keys" 
# method. In subsquent counts we use "values".

for line in converted_data:
      if count == 0:
             header = line.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(line.values())
output_file.close()