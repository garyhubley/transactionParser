
import sys
import csv

from datetime import datetime

def ConvertDateCibc(origDate):
    date = datetime.strptime(origDate, '%Y-%m-%d')
    return date.strftime('%d/%m/%Y')

def cibc(accountName, filename):

    account = accountName
    expenseType = ''

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    for row in reader:
        date = ConvertDateCibc(row[0])
        description = row[1]
        if row[2] != '':
            amount = row[2]
        else:
            amount = '-' + row[3]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)
