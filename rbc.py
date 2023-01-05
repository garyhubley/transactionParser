
import sys
import csv

from datetime import datetime

def ConvertDateRbc(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime('%d/%m/%Y')

def rbc(accountName, filename):

    account = accountName

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    # Skip header row
    next(reader)

    for row in reader:
        date = ConvertDateRbc(row[2])
        description = row[4]
        expenseType = row[5]
        amount = row[6]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)
