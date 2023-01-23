import heapq
from cmath import inf
from sys import stdin

readVector=lambda: [*map(int,stdin.readline().rstrip().split(' '))]
readScalar=lambda: int(stdin.readline())

# initialization
V, E = readVector()
K = readScalar()
weights = [inf for _ in range(V+1)] # 가중치(또는 거리) 테이블의 모든 값들을 무한으로 초기화
weights[K] = 0 # 시작점의 가중치는 0으로 초기화

paths = [[] for _ in range(V+1)]
for _ in range(E):
    src, dst, weight = readVector()
    paths[src].append([weight, dst])

heap = []
heapq.heappush(heap, [0,K])


# Execution
def djikstra(heap, weights):
    while heap:
        src = heapq.heappop(heap)
        w0,u = src
        dsts = paths[u]
        if weights[u] < w0: continue
        for dst in dsts:
            w1, v = dst
            w2 = w0 + w1
            if w2 < weights[v]:
                weights[v] = w2
                heapq.heappush(heap, [w2, v])
    return weights

weights = djikstra(heap, weights)

# Format Output
for w in weights[1:]:
    if w == inf: print("INF")
    else: print(w)