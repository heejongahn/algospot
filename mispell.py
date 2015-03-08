##### Problem
# Misspelling is an art form that students seem to excel at. Write a program
# that removes the nth character from an input string.

##### Input
# The first line of input contains a single integer N, (1 ≤ N ≤ 1000) which is
# the number of datasets that follow.
# Each dataset consists of a single line of input containing M, a space, and a
# single word made up of uppercase letters only. M will be less than or equal to
# the length of the word. The length of the word is guaranteed to be less than or
# equal to 80.

##### Output
# For each dataset, you should generate one line of output with the following
# values: The dataset number as a decimal integer (start counting at one),
# a space, and the misspelled word. The misspelled word is the input word
# with the indicated character deleted.

n = int(input())

wordList = []
for i in range(n):
    wordList.append(input())

count = 1
for word in wordList:
    pair = word.split(' ')
    pair[1] = list(pair[1])
    pair[1].pop(int(pair[0])-1)
    print ("%d %s" % (count, ''.join(pair[1])))
    count+=1
