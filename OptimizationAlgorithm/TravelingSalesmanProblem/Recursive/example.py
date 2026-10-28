from BruteForce import brute_force

D=[
[-1, 3, 6, 7],
[ 5,-1, 2, 3],
[ 6, 4,-1, 2],
[ 3, 7, 5,-1]
]

S = brute_force(D,0)

print(S.tsp())

# 开始回溯
M = S.array
lists = list(range(len(S.X)))
start = S.start_node

while len(lists) > 0:
    lists.pop(lists.index(start))
    m = S.transfer(lists)
    next_node = S.array[start][m]
    print(start,"--->" ,next_node)
    start = next_node
