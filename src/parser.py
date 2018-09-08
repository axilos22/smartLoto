import csv

with open("res/db.csv","r") as dbFile:
    reader = csv.reader(dbFile, delimiter=";")
    for row in reader:
        print(row)
        # msg = ", ".join(row)
        # print(msg)