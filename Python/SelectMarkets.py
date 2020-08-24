filename = 'company_codes.csv'
file = open(filename, 'r')

selected = {}

line = file.readline()

while line:
    line = line.strip()
    id, name = line.split(',')
    line = file.readline()

    if len(id) > 5: continue #Exclude Options
    if not id[4].isdigit(): continue

    if id[-1].isdigit():
        selected[id] = name


file.close()

codes = list(selected.keys())
codes.sort()

file = open('processed_codes.csv', 'w')

for i in codes:
	str_lin = '%s, %s' %(i, selected[i])
	print(str_lin, file=file)

file.close()


