
import sys
import csv

from datetime import datetime

def ConvertDateTriangle(origDate):
    date = datetime.strptime(origDate, '%Y-%m-%d')
    return date.strftime('%d/%m/%Y')

def triangle(accountName, filename):

    account = accountName

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    # Skip first 4 rows
    for i in range(4):
        next(reader)

    for row in reader:
        date = ConvertDateTriangle(row[1])
        description = row[4]
        amount = row[6]
        expenseType = row[5]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)
