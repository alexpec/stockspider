import pandas as pd
import datetime
import numpy as np
import bovespa


files = ['2019'] #['2017', '2018', '2019']

company_names = {}

outputfile = 'outputdata.csv'
outputfile = open(outputfile, 'w')
print('Date,Stock Code,Price Open,Price Close,Price High,Price Low,Price Mean,Quantity,Volume', file=outputfile)

for year in files:
	file_str = '../TimeSeries/COTAHIST_A%s.TXT' %(year)
	bf = bovespa.File(file_str)
	for rec in bf.query():
		date = rec.date.strftime("%d/%m/%Y")
		dtime = datetime.datetime.strptime(date, "%d/%m/%Y")
		company_name = rec.company_name
		code = rec.stock_code
		price_close = rec.price_close
		price_high = rec.price_high
		price_low = rec.price_low
		price_mean = rec.price_mean
		price_open = rec.price_open
		quantity = rec.quantity
		volume = rec.volume

		if code not in company_names.keys():
			company_names[code] = company_name
			print("New company Added: %s - %s" %(code, company_name))

		str_line = '%s,%s,%.2f,%.2f,%.2f,%.2f,%.2f,%s,%s' %(
			date, code, price_open, price_close, price_high, price_low, price_mean, quantity, volume	
		)
		print(str_line, file=outputfile)
		#print(str_line)

outputfile.close()

codes = list(company_names.keys())
codes.sort()
codes_output = open('company_codes.csv', 'w')
for i in codes:
	str_line = '%s, %s' %(i, company_names[i])
	print(str_line, file=codes_output)
codes_output.close()

#https://medium.com/datadriveninvestor/stock-market-clustering-with-k-means-clustering-in-python-4bf6bd5bd685

