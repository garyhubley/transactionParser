#! /usr/bin/python3

import pymodules.scotia as scotia
import pymodules.rbc as rbc
import pymodules.cibc as cibc
import pymodules.triangle as triangle

import csv
import sys
import os

from datetime import datetime

SUCCESS = 0
FAIL = -1

        # [ rbc.rbc, 'rbc visa', 'rbcVisa.csv' ],
filenames = [
        [ scotia.scotia, 'Mutual cheq', 'mutual.csv' ],
        [ rbc.rbc, 'gary cheq', 'gary.csv' ],
        [ cibc.cibc, 'costco', 'costco.csv' ],
        [ triangle.triangle, 'triangle', 'triangle.csv' ],
        [ cibc.cibc, 'Chris cheq', 'chrisCheq.csv'],
        [ cibc.cibc, 'chris visa', 'chrisVisa.csv'] 
            ]

def filecheck(prefix):
    ret = SUCCESS
    for f in filenames:
        path = prefix + f[2]
        if not os.path.exists(path):
            print(f"{path} doesn't exist")
            ret = FAIL

    return ret

def usage():
    print("usage: ./main.py <csvDirectory>")

def addCategories(filename, writer):
    inputFile = open(filename)
    reader = csv.reader(inputFile)

    for row in reader:
        page = row[2]
        table = row[0]
        category = row[1]

        newrow = [page] + [table] + [category]
        writer.writerow(newrow)

def main():
    if len(sys.argv) != 2:
        usage()
        return -1

    prefix = sys.argv[1]

    if filecheck(prefix) != SUCCESS:
        return -1

    outputFilename = prefix + datetime.today().strftime('%Y.%m.%d.transactions.csv')
    outputFile = open(outputFilename, 'w', newline='')
    writer = csv.writer(outputFile, dialect= 'excel')

    # Write header row
    header = ["account"] + ["date"] + ["description"] + ["expenseType"] 
    header += ["amount"] + ["page"] + ["table"] + ["category"]
    writer.writerow(header) 

    for i in range(len(filenames)):
        filenames[i][0](writer, filenames[i][1], prefix + filenames[i][2])

    return SUCCESS

if __name__ == "__main__":
    main()
