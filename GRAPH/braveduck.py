n = int(input())


def anotherUnion(anotherList, a, b):
    for e in anotherList:
        if a in e:
            set1 = e
        if b in e:
            set2 = e

    if set1 == set2:
        return anotherList

    newSet = set1.union(set2)
    anotherList.remove(set1)
    anotherList.remove(set2)
    anotherList.append(newSet)

    return anotherList

for i in range(n):
    max = pow(int(input()), 2)
    start = input().split(" ")
    end = input().split(" ")
    (start[0], start[1]) = (int(start[0]), int(start[1]))
    (end[0], end[1]) = (int(end[0]), int(end[1]))

    stoneNum = int(input())

    stoneList=[start, end]

    for j in range(stoneNum):
        stone = input().split(" ")
        stoneList.append([int(stone[0]), int(stone[1])])

    stoneNum += 2

    connectInfo = []
    for i in range(stoneNum):
        connectInfo.append({i})

    for i in range(stoneNum):
        for j in range(i+1, stoneNum):
            dist = (pow(stoneList[i][0] - stoneList[j][0], 2) +
            pow(stoneList[i][1] - stoneList[j][1], 2))

            if dist <= max:
                connectInfo = anotherUnion(connectInfo, i, j)

    avail = False
    for e in connectInfo:
        if 0 in e and 1 in e:
            avail = True

    if avail:
        print("YES")
    else:
        print("NO")
