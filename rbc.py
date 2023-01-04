
import csv

from datetime import datetime

def ConvertDate(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime('%d/%m/%Y')

def main():

    inputFile = open('rbc.csv')
    outputFile = open('newrbc.csv', 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    # Skip header row
    next(reader)

    for row in reader:
        account = row[0]
        date = ConvertDate(row[2])
        description = row[4]
        expenseType = row[5]
        amount = row[6]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

if __name__ == "__main__":
    main()
