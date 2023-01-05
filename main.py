
import scotia
import rbc
import cibc
import triangle

import csv

from datetime import datetime

filenames = [
        [ 'Mutual cheq', 'mutual.csv' ],
        [ 'gary cheq', 'gary.csv' ],
        [ 'rbc visa', 'rbcVisa.csv' ],
        [ 'costco', 'costco.csv' ],
        [ 'triangle', 'triangle.csv' ],
        [ 'Chris cheq', 'chrisCheq.csv'],
        [ 'chris visa', 'chrisVisa.csv'] 
            ]

def main():
    outputFilename = datetime.today().strftime('%Y.%m.%d.transactions.csv')
    outputFile = open(outputFilename, 'w', newline='')
    writer = csv.writer(outputFile, dialect= 'excel')

    # Write header row
    header = ["account"] + ["date"] + ["description"] + ["expenseType"] + ["amount"]
    writer.writerow(header) 

    writer = scotia.scotia    (writer, filenames[0][0], filenames[0][1])
    writer = rbc.rbc          (writer, filenames[1][0], filenames[1][1])
    writer = rbc.rbc          (writer, filenames[2][0], filenames[2][1])
    writer = cibc.cibc        (writer, filenames[3][0], filenames[3][1])
    writer = triangle.triangle(writer, filenames[4][0], filenames[4][1])
    writer = scotia.scotia    (writer, filenames[5][0], filenames[5][1])
    writer = scotia.scotia    (writer, filenames[6][0], filenames[6][1]) 


if __name__ == "__main__":
    main()
