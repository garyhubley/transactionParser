
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

    if len(sys.argv) != 3:
        print('Incorrect number of args. Please provide account name and filename')
        return

    account = sys.argv[1]
    filename = sys.argv[2]

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    for row in reader:
        date = ConvertDate(row[0])
        description = row[4]
        amount = str(-1 * float(row[1]))
        expenseType = row[3]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

if __name__ == "__main__":
    main()
