
# Transaction Parser

Converts bank CSV downloads to match my existing columns

columns: 
0 Account Name
1 Date (dd/mm/yyyy)
2 Description
3 Type
4 Amount


## Create transactions w/ data validation
1. Download all transactions
1. run combine.py
1. open transactions csv file
1. create new sheet
1. open validationCategories.csv
1. paste values into new sheet
1. press alt+f11 to open vbe
1. right click > import
1. find Module1.bas
1. close vbe
1. press alt+f8 to view macros
1. run named ranges macro
1. verify ranges populated in formulas > name manager
1. run add validation macro

## extract amounts
1. run extract.py
