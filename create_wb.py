import glob
import pandas

# create list of all the csv file names
files = glob.glob('*.csv')

# create excel writer object
writer = pandas.ExcelWriter('switch_data.xlsx', engine='xlsxwriter')

# loop through each file and write to workbook
for switch in files:
    df = pandas.read_csv(switch)
    df.to_excel(writer, sheet_name=switch[:-4])

writer.save()
