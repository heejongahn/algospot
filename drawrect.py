##### Problem
# Given three coordinates of three vertexes of a rectangle, find the coordinate
# of the fourth one

##### Input
# First line, T, is number of test cases followed by T*3 lines, each 3 lines
# represents 1 rectangle. Each x and y coordinates are seperated by spaces

##### Output
# Print a line for each rectangle, x and y coordinates should be seperated by space


n = int(input())

for i in range(n):
    xList = []
    yList = []

    for j in range(3):
        line = input().strip('\n')
        line = line.split(" ")

        x = line[0]
        y = line[1]

        if x in xList:
            xList.remove(x)
        else:
            xList.append(x)

        if y in yList:
            yList.remove(y)
        else:
            yList.append(y)

    ansString = str(xList[0]) + " " + str(yList[0])
    print(ansString)
