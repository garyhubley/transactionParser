#! /usr/bin/python3

import csv
import sys
import os

from datetime import datetime

SUCCESS = 0
FAIL = -1

filenames = [
        [ scotia.scotia, 'Mutual cheq', 'mutual.csv' ],
        [ rbc.rbc, 'gary cheq', 'gary.csv' ],
        [ rbc.rbc, 'rbc visa', 'rbcVisa.csv' ],
        [ cibc.cibc, 'costco', 'costco.csv' ],
        [ triangle.triangle, 'triangle', 'triangle.csv' ],
        [ cibc.cibc, 'Chris cheq', 'chrisCheq.csv'],
        [ cibc.cibc, 'chris visa', 'chrisVisa.csv'] 
            ]

def filecheck(path):
    ret = SUCCESS
    if not os.path.exists(path):
        print(f"{path} doesn't exist")
        ret = FAIL

    return ret

def usage():
    print("usage: ./extract.py <path to transaction csv>")

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

    inputFilePath = sys.argv[1]

    if filecheck(inputFilePath) != SUCCESS:
        return -1

    # get path of inputfilename

    # create output filename
    outputFilename = prefix + datetime.today().strftime('%Y.%m.%d.transactions.csv')

    # open output file
    outputFile = open(outputFilename, 'w', newline='')
    writer = csv.writer(outputFile, dialect= 'excel')

    # Write header row
    # header = ["account"] + ["date"] + ["description"] + ["expenseType"] 
    # header += ["amount"] + ["page"] + ["table"] + ["category"]
    header = ["amount"] + ["page"] + ["table"] + ["category"]
    writer.writerow(header) 

    # begin extraction

    return SUCCESS

if __name__ == "__main__":
    main()
