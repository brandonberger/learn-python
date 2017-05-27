import csv
path = 'open-data/openaddress/us/fl/brevard.csv'

with open(path) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['test'], row['test2'])


#f = open('open-data/openaddress/us/fl/brevard.csv')
#csv_f = csv.reader(f)

#for row in csv_f:
#	print row[3]