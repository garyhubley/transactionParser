
import csv

from datetime import datetime

def ConvertDateRbc(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime('%d/%m/%Y')

def rbc(writer, accountName, filename):

    account = accountName

    inputFile = open(filename)

    reader = csv.reader(inputFile)

    # Skip header row
    next(reader)

    for row in reader:
        date = ConvertDateRbc(row[2])
        description = row[4]
        expenseType = row[5]
        amount = row[6]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

    return writer
