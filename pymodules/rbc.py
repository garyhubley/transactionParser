
import csv

from datetime import datetime

outputDateFormat = '%Y/%m/%d'

def ConvertDateRbc(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime(outputDateFormat)

def rbc(writer, accountName, filename):

    print(f"Starting {accountName} - {filename}")
    account = accountName

    inputFile = open(filename)

    reader = csv.reader(inputFile)

    # Skip header row
    next(reader)

    for row in reader:
        date = ConvertDateRbc(row[2])
        description = row[4]
        expenseType = row[5]
        amount = str(float(row[6]) * -1)

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

    return writer
