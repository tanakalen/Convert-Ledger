#! /usr/bin/env python3

'''
  convertLedger
  	by Len
  
  input: csv file to convert
  output: Ledger to stdout
'''

# Copyright (C) 2011 by Len Tanaka 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import csv, sys, re

def getFile(filename):
	'''Gets items from csv file exported from excel msdos csv'''
	asset = r".*(Checking|Saving)"
	with open(filename, newline='', encoding='cp1250') as f:
		try:
			reader = csv.reader(f)
			for row in reader:
				date = row[0]
				year = row[1]
				month = row[2]
				day = row[3]
				company = row[4]
				amount = row[5]
				type = row[6]
				account = row[7]
				print(year + '/' + month + '/' + day + '\t' + company)
				print('\t' + 'Expenses:' + type + '\t$' + amount)
				if account == 'Cash':
					print('\tExpenses:' + account)
				elif (len(re.findall(asset, account))>0):
					print('\tAssets:' + account)
				else:
					print('\tLiabilities:' + account)
				print()
		except csv.Error as e:
			sys.exit('file {}, line{}: {}'.format(filename, reader.line_num, e))

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		sys.exit()
	else:
		file = sys.argv[1]
		getFile(file)

		