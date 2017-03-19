import sys, os
import csv

csvfile = '286busLibTransposed_Paper.csv'
with open(csvfile, 'rU') as fin, open('TB_Raw.csv', 'rU') as fout:
    reader = csv.reader(fin)
    readerCheck = csv.reader(fout)
    
    next(reader)
    next(reader)
    goodlines = 0
    badlines = 0

    #writer.writerow(next(reader) + ['286', '286'])
    #writer.writerow(next(reader) + ['P (MW)', 'Q (MVAR)'])
    for row in reader:
    	readerCheck = csv.reader(fout)
    	for rowCheck in readerCheck:
    		if rowCheck == row:
    			goodlines += 1