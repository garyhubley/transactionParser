
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
        print('Incorrect number of args. Please provide account name and filename')
        return

    account = "triangle"
    filename = sys.argv[1]

    inputFile = open(filename)
    outputFile = open('new' + filename, 'w', newline='')

    reader = csv.reader(inputFile)
    writer = csv.writer(outputFile, dialect= 'excel')

    # Skip first 4 rows
    for i in range(4):
        next(reader)

#REF,TRANSACTION DATE,POSTED DATE,TYPE,DESCRIPTION,Category,AMOUNT
#75446132345010487543702,2022-12-09,2022-12-12,PURCHASE,#370 SPORT CHEK,Sport stores,2.59
    for row in reader:
        date = ConvertDate(row[1])
        description = row[4]
        amount = row[6]
        expenseType = row[5]

        newrow = [account] + [date] + [description] + [expenseType] + [amount]
        writer.writerow(newrow)

if __name__ == "__main__":
    main()
