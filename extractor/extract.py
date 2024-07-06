#! /usr/bin/python3

import csv
import sys
import os

from datetime import datetime
from pathlib import Path

from totalTable import totals

SUCCESS = 0
FAIL = -1

def filecheck(path):
    ret = SUCCESS
    if not os.path.exists(path):
        print(f"{path} doesn't exist")
        ret = FAIL

    return ret

def usage():
    print("usage: ./extract.py <path to transaction csv>")

def addExpense( item, amount ):
    if( item[3] == "" ):
        item[3] = "="

    item[3] = item[3] + '+' + amount

def main():
    if len(sys.argv) != 2:
        usage()
        return -1

    inputFilePath = sys.argv[1]

    path = Path(inputFilePath)

    if filecheck(inputFilePath) != SUCCESS:
        return -1

    # get path of inputfilename

    # create output filename
    outputFilename = path.parent.absolute() / f'{path.stem}.extracted.csv'

    print(outputFilename)

    count = 0
    numMissed = 0
    # begin extraction
    with  open(inputFilePath, newline='') as inputFile:
        reader = csv.reader(inputFile, dialect= 'excel')
        # skip header row
        next(reader)

        for idx, row in enumerate(reader):
            #print(f' {idx}: couldn\'t find: >{row[5]}<, >{row[6]}<, >{row[7]}<')
            count += 1
            found = False
            # find entry in totalTable
            for t in totals:
                if( row[5] == t[0] and row[6] == t[1] and row[7] == t[2] ):
                    addExpense( t, row[4] )
                    found = True
                    #print(f'   found: {t[0]}, {t[1]}, {t[2]}: {t[3]}')
            if( found == False ): 
                numMissed += 1
                print("")
                print(row)
                print(f' {idx}: couldn\'t find: >{row[5]}<, >{row[6]}<, >{row[7]}<')

    # open output file
    with open(outputFilename, 'w', newline='') as outputFile:
        writer = csv.writer(outputFile, dialect= 'excel')
        header = ["amount"] + ["page"] + ["table"] + ["category"]
        writer.writerow(header) 
        for t in totals:
            writer.writerow( [ t[3] ] + [ t[0] ] + [ t[1] ] + [ t[2] ] )

    numFound = count - numMissed
    print(f'Found {numFound} of {count} entries')

    return (numMissed == 0)

if __name__ == "__main__":
    main()
