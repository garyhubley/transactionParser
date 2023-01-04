
import sys
import csv

from datetime import datetime

def ConvertDate(origDate):
    date = datetime.strptime(origDate, '%m/%d/%Y')
    return date.strftime('%d/%m/%Y')

def main():

    #print(f"Arguments count: {len(sys.argv)}")
    #for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")

    if len(sys.argv) != 2:
        print('Incorrect number of args. Please provide filename')
        return

    filename = sys.argv[1]

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

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
