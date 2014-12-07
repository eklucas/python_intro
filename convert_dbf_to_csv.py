import csv
from dbfpy import dbf
import os
import sys

files = os.listdir(sys.argv[1])

for filename in files:
    if filename.endswith('.DBF'):
        print "Converting %s to csv" % filename
        csv_fn = filename[:-4]+ ".csv"
        with open(csv_fn,'wb') as csvfile:
            in_db = dbf.Dbf(filename)
            out_csv = csv.writer(csvfile)
            names = []
            for field in in_db.header.fields:
                names.append(field.name)
            out_csv.writerow(names)
            for rec in in_db:
                out_csv.writerow(rec.fieldData)
            in_db.close()
            print filename, "Done..."
    else:
        print "Filename does not end with .dbf"
