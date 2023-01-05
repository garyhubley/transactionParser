
import csv

from datetime import datetime

def ConvertDateTriangle(origDate):
    date = datetime.strptime(origDate, '%Y-%m-%d')
    return date.strftime('%d/%m/%Y')

def triangle(writer, accountName, filename):

    account = accountName

    inputFile = open(filename)

    reader = csv.reader(inputFile)

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

    return writer
