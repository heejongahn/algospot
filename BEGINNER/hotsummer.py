n = int(input())

for i in range(n):
        limit = int(input())
        usage = input().split(" ")

        total = 0
        for num in usage:
                total += int(num)

        if total <= limit:
                print ('YES')
        else:
                print ('NO')


