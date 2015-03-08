##### Problem
# I don't want to translate the whole thing. Just read the code and you'll get
# it.

##### Input
# First line indicates the number of test cases.
# From second line, there are strings that you should encrypt.

##### Output
# Print each encrypted strings, one per a line.

n = int(input())
strings = []

for i in range(n):
    strings.append(input())

for string in strings:
    newString = ''
    length = (len(string)//2)

    if length==0:
        print (string)
        continue

    for i in range(length):
        newString += string[2*i]

    if len(string)%2 != 0:
        newString += string[len(string)-1]

    for i in range(length):
        newString += string[2*i+1]


    print (newString)
