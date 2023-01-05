
import csv

from datetime import datetime

def ConvertDateScotia(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime('%d/%m/%Y')

def scotia(writer, accountName, filename):

    account = accountName

    inputFile = open(filename)

    reader = csv.reader(inputFile)

    for row in reader:
        date = ConvertDateScotia(row[0])
        description = row[4]
        amount = str(-1 * float(row[1]))
        expenseType = row[3]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

    return writer

