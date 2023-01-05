
import csv

from datetime import datetime

def ConvertDateScotia(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime('%d/%m/%Y')

def scotia(accountName, filename):

    account = accountName

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    for row in reader:
        date = ConvertDateScotia(row[0])
        description = row[4]
        amount = str(-1 * float(row[1]))
        expenseType = row[3]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

