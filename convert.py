##### Problem
# Conversion between the metric and English measurement systems is relatively
# simple. Often, it involves either multiplying or dividing by a constant.
# You must write a program that converts between the following units:

# 1.000 kilogram    ->  2.2046 pounds
# 0.4536 kilograms  ->  1.0000 pound
# 1.000 liter       ->  0.2642 gallons
# 3.7854 liters     ->  1.000 gallon


##### Input
# The first line of input contains a single integer N, (1 ≤ N ≤ 1000) which is
# the number of datasets that follow.
# Each dataset consists of a single line of input containing a floating point
# (double precision) number, a space and the unit specification for the
# measurement to be converted. The unit specification is one of kg, lb, l, or g
# referring to kilograms, pounds, liters and gallons respectively.

##### Output
# For each dataset, you should generate one line of output with the following
# values: The dataset number as a decimal integer (start counting at one),
# a space, and the appropriately converted value rounded to 4 decimal places,
# a space and the unit specification for the converted value.

n = int(input())
convert1 = {'kg': 2.2046, 'lb': 0.4536, 'l': 0.2642, 'g': 3.7854}
convert2 = {'kg': 'lb', 'lb': 'kg', 'l': 'g', 'g': 'l'}

srcList = []
for i in range(n):
    srcList.append(input())

count = 1
for src in srcList:
    before = src.split(" ")

    quantity = float(before[0])
    standard = before[1]

    print('%d %0.4f %s' % (count, quantity*convert1[standard],
        convert2[standard]))
    count += 1
