##### Problem
# Given a circuit of many computers, you want to send a message from a starting
# computor to another. Unfortunately, these cables are not so descent thus noise
# get amplified as it goes through cables. Find a minimum-noise route.


##### Input
# First line : number of test cases
# Firts line of each test case : number of computers and number of cables
# Rest lines of each test case : info about noise amplication
# Starting point is always computer 0, destination is always computer N-1

##### Output
# Value of noise amplication 소수점 아래 10자리까지

def extract_min(remaining, dist):
    min = remaining[0]

    for e in remaining:
        if dist[e] <= dist[min]:
            min = e

    return min

n = int(input())

for case in range(n):
    # Graph Initialization
    graph = {}
    (n_v, n_e) = input().split(" ")
    (n_v, n_e) = (int(n_v), int(n_e))

    # Graph Construction
    for i in range(n_v):
        graph[i] = []

    for i in range(n_e):
        e = input().split(" ")
        e = [int(e[0]), int(e[1]), float(e[2])]

        graph[e[0]].append((e[1], e[2]))
        graph[e[1]].append((e[0], e[2]))

    # Dijkstra Initialization
    remaining = list(range(n_v))

    dist = [9999] * n_v
    dist[0] = 1

    # Dijkstra
    while remaining:
        target = extract_min(remaining, dist)
        remaining.remove(target)

        edges = graph[target]
        for edge in edges:
            next = edge[0]
            amp = edge[1]

            dist[next] = min(dist[next], dist[target] * amp)


    print("%0.10f" % dist[n_v-1])
