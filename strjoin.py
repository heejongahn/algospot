##### Problem
# (Will be written)

##### Input
# (Will be written)

##### Output
# (Will be written)

n = int(input())

def cost(list):
    if len(list)==1:
        return 0
    else:
        list.sort()
        intermediate_cost = list.pop(0) + list.pop(0)
        list.append(intermediate_cost)
        return intermediate_cost + cost(list)

for case in range(n):
    input()
    nums = input().split(" ")
    nums = [int(num) for num in nums]

    print (cost(nums))
