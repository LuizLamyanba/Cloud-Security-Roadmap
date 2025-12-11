import csv 
import os

os.makedirs('removed headerfile', exist_ok=True)

for csvfile in os.listdir('.'):
    if not csvfile.endswith('.csv'):
        continue
    print('removing header from ' + csvfile+'...')


    csvobj = open(csvfile)
    csvread = csv.reader(csvobj)
    rows = list(csvread)
    del rows[0]
    csvobj.close()

    writeobj = open(os.path.join('removed headerfile',csvfile), mode = 'w', newline = '' )
    csvwrite = csv.writer(writeobj)
    csvwrite.writerows(rows)
    writeobj.close()






