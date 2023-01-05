
import scotia
import rbc
import cibc
import triangle

import sys

filenames = [
        [ 'Mutual cheq', 'mutual.csv' ],
        [ 'gary cheq', 'gary.csv' ],
        [ 'rbc visa', 'rbcVisa.csv' ],
        [ 'costco', 'costco.csv' ],
        [ 'triangle', 'triangle.csv' ],
        [ 'Chris cheq', 'chrisCheq.csv'],
        [ 'chris visa', 'chrisVisa.csv'] 
            ]

def main():
    scotia.scotia    (filenames[0][0], filenames[0][1])
    rbc.rbc          (filenames[1][0], filenames[1][1])
    rbc.rbc          (filenames[2][0], filenames[2][1])
    cibc.cibc        (filenames[3][0], filenames[3][1])
    triangle.triangle(filenames[4][0], filenames[4][1])
    scotia.scotia    (filenames[5][0], filenames[5][1])
    scotia.scotia    (filenames[6][0], filenames[6][1]) 


if __name__ == "__main__":
    main()
