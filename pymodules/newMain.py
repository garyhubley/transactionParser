#! /usr/bin/python3

from parser import Parser

import csv
import sys

from datetime import datetime

SUCCESS = 0
FAIL = -1

def usage():
    print("usage: ./main.py <csvDirectory>")

def initCsvWriter(filePath):
    outputFilename = filePath + datetime.today().strftime('%Y.%m.%d.transactions.csv')
    outputFile = open(outputFilename, 'w', newline='')
    csvWriter = csv.writer(outputFile, dialect= 'excel')

    # Write header row
    header = ["account"] + ["date"] + ["description"] + ["expenseType"] + ["amount"]
    csvWriter.writerow(header) 

    return csvWriter

def main():

    if len(sys.argv) != 2:
        usage()
        return FAIL

    prefix = sys.argv[1]

    parsers = [
        Parser('scotia',   'Mutual cheq', prefix + 'mutual.csv' ),
        Parser('rbc',      'gary cheq',   prefix + 'gary.csv' ),
        Parser('rbc',      'rbc visa',    prefix + 'rbcVisa.csv' ),
        Parser('cibc',     'costco',      prefix + 'costco.csv' ),
        Parser('triangle', 'triangle',    prefix + 'triangle.csv' ),
        Parser('cibc',     'Chris cheq',  prefix + 'chrisCheq.csv'),
        Parser('cibc',     'chris visa',  prefix + 'chrisVisa.csv') 
            ]

    csvWriter = initCsvWriter(prefix)

    for p in parsers:
        p.parse(csvWriter)

    return SUCCESS

if __name__ == "__main__":
    main()
