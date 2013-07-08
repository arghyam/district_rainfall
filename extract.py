#this is used for extracting data from the text files
#badly written but works
import csv
from os import listdir
from os.path import isfile, join
header_columns = ['state','district','year','JAN-RF','JAN-DEP','FEB-RF','FEB-DEP','MAR-RF','MAR-DEP','APR-RF','APR-DEP','MAY-RF','MAY-DEP','JUN-RF','JUN-DEP','JUL-RF','JUL-DEP','AUG-RF','AUG-DEP','SEP-RF','SEP-DEP','OCT-RF','OCT-DEP','NOV-RF','NOV-DEP','DEC-RF','DEC-DEP']

with open('distrainfall.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csvwriter.writerow(header_columns)

mypath ='/media/thej/data/distrainfall/scraped_data/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
#print onlyfiles

for file_name in onlyfiles:
	district_array = []
	names = file_name.split("-")
	state_name = names[0]
	district_name = names[1]
	scraped_data_folder_path = mypath + file_name
	line_number = 0
	print str(names)
	with open(scraped_data_folder_path) as f:
		content = f.readlines()
		for line in content:
			line_number = line_number +1
			printed_line = ""
			if line_number == 19 or line_number == 21 or line_number == 23 or line_number == 25 or line_number == 27:
				year_array = []
				year_array.append(state_name)
				year_array.append(district_name)
				year = line[0:4]
				year_array.append(year)
				start_index = 4
				end_index = 18
				i = 0
				while(i < 11):
					monthly = line[4+(13*i):18+(13*i)]
					#print monthly
					if monthly != "":
						parts = monthly.split()
						for part in parts:
							year_array.append(part)
					else:
						year_array.append("")
						year_array.append("")

						#print parts
					i = i +1
				district_array.append(year_array)

	with open('distrainfall.csv', 'a') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvwriter.writerows(district_array)
			