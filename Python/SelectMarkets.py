filename = 'company_codes.csv'
file = open(filename, 'r')

lots_selected = []
frac_selected = []

line = file.readline()

while line:
    id, name = line.split(',')
    if id[-1].isdigit():
        lots_selected.append(id)
        print('Stock: %s' %id)
    elif id[-1] == 'F':
        frac_selected.append(id)

    line = file.readline()