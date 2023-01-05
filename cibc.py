
import sys
import csv

from datetime import datetime

def ConvertDate(origDate):
    date = datetime.strptime(origDate, '%Y-%m-%d')
    return date.strftime('%d/%m/%Y')

def main():

    #print(f"Arguments count: {len(sys.argv)}")
    #for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")

    if len(sys.argv) != 2:
        print('Incorrect number of args. Please provide filename')
        return

    account = 'Costco card'
    expenseType = ''
    filename = sys.argv[1]

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

# 2023-01-04,PAYMENT THANK YOU/PAIEMEN T MERCI,,417.76,5223********6713
    for row in reader:
        date = ConvertDate(row[0])
        description = row[1]
        if row[2] != '':
            amount = row[2]
        else:
            amount = '-' + row[3]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

if __name__ == "__main__":
    main()
