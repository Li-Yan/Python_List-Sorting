#!/usr/bin/python

import sys
from listOp import Refine, IsNumber, Separate, Rearrange
from quicksort import QuickSort, QuickSort_Optimized

#read input
input_path = sys.argv[1]
f = open(input_path, 'r');
ss = f.readline().strip().split(' ')
f.close()

'''
initilization
w_or_n: It is a word or a number in stringList 
word: only word list
number: only number list
'''
w_or_n = list()
word = list()
number = list()

#separate word and number in advance, sort both lists, rearrange them
Separate(ss, w_or_n, word, number)
QuickSort(word, 0, len(word) - 1)
QuickSort(number, 0, len(number) - 1)
outList = Rearrange(w_or_n, word, number)

#Output
output_path = sys.argv[2]
f = open(output_path, 'w');
for i in range(0,  len(outList) - 1):
	f.write('{0} '.format(outList[i]))
f.write('{0}\n'.format(outList[len(outList) - 1]))
f.close()