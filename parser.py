
import csv
import os

from datetime import datetime

class Parser:
    __outputDateFormat = '%Y/%m/%d'

    __dateFormats = {
            'cibc':'%Y-%m-%d',
            'rbc':'%m/%d/%Y',
            'triangle':'%Y-%m-%d',
            'scotia':'%m/%d/%Y' 
            }

    def __init__(self, bank, account, accountFilename):
        self.bank = bank
        self.accountName = account
        self.accountFilename = accountFilename
        if self.__filecheck() != 0:
            print('Invalid initialization')

    def __convertDate(self, origDate):
        date = datetime.strptime(origDate, self.__dateFormats[self.bank])
        return date.strftime(self.__outputDateFormat)

    def __filecheck(self):
        path = self.accountFilename
        if not os.path.exists(path):
            print(f"{path} doesn't exist")
            return -1

        return 0

    def __initCsvReader(self):
        inputFile = open(self.accountFilename)
        return csv.reader(inputFile)

    def __cibcParser(self, csvWriter):

        expenseType = ''

        csvReader = self.__initCsvReader()
        
        for row in csvReader:
            date = self.__convertDate(row[0])
            description = row[1]
            if row[2] != '':
                amount = row[2]
            else:
                amount = '-' + row[3]

            newrow = [self.accountName] + [date] + [description] + [expenseType] + [amount]
            csvWriter.writerow(newrow)

        return csvWriter

    def __rbcParser(self, csvWriter):

        csvReader = self.__initCsvReader()

        # Skip header row
        next(csvReader)

        for row in csvReader:
            date = self.__convertDate(row[2])
            description = row[4]
            expenseType = row[5]
            amount = row[6]

            newrow = [self.accountName] + [date] + [description] + [expenseType] + [amount]
            csvWriter.writerow(newrow)

        return csvWriter


    def __scotiaParser(self, csvWriter):

        csvReader = self.__initCsvReader()

        for row in csvReader:
            date = self.__convertDate(row[0])
            description = row[4]
            amount = str(-1 * float(row[1]))
            expenseType = row[3]

            newrow = [self.accountName] + [date] + [description] + [expenseType] + [amount]
            csvWriter.writerow(newrow)

        return csvWriter

    def __triangleParser(self, csvWriter):

        csvReader = self.__initCsvReader()

        # Skip first 4 rows
        for i in range(4):
            next(csvReader)

        for row in csvReader:
            date = self.__convertDate(row[1])
            description = row[4]
            amount = row[6]
            expenseType = row[5]

            newrow = [self.accountName] + [date] + [description] + [expenseType] + [amount]
            csvWriter.writerow(newrow)

        return csvWriter

    def parse(self, writer):
        print(f"Parsing {self.accountFilename} ({self.accountName}, {self.bank})")

        if self.bank == 'cibc':
            self.__cibcParser(writer)
        elif self.bank == 'rbc':
            self.__rbcParser(writer)
        elif self.bank == 'triangle':
            self.__triangleParser(writer)
        elif self.bank == 'scotia':
            self.__scotiaParser(writer)
        else:
            print("bank not recognized")

        return
