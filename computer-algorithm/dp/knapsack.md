#   knapsack
*   무게와 가치가 주어진 각 요소들에 대하여 제한된 무게로 최대의 가치를 도출하는 문제
*   선형계획법 문제
*   각 물품은 1개씩만 선택 가능

##  백준 12865, 평범한 배낭
*   무게 a와 가치 b에 대하여
    *   무게 a에 최대값 제한이 존재할 때
    *   가치 b의 최대값

```py
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]

N, K = readVector()
items = [readVector() for _ in range(N)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(N):
    a, b = items[i]
    for k in range(1,K+1):
        if k < a:
            dp[i+1][k] = dp[i][k]
            #  dp[i+1][k] = max(dp[i][k], dp[i+1][k])
        else:
            dp[i+1][k] = max(dp[i][k], b + dp[i][k-a])

print(dp[N][K])
```

##  백준 7579, 앱
*   메모리 a와 비용 b에 대하여
    *   메모리 a에 최솟값 제한이 존재할 때
    *   비용 b의 최솟값
```py
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]

N, M = readVector() # N, M = 5, 60
A = readVector() # B = [30, 10, 20, 35, 40]
B = readVector() # C = [3, 0, 3, 5, 4]

ASUM = sum(A)

dp = [[0 for _ in range(ASUM+1)] for _ in range(N+1)]
for i in range(N):
    a, b = A[i], B[i]
    for j in range(ASUM+1):
        b_ij = dp[i][j]

        if j-b >= 0:
            dp[i][j] = max(b_ij, dp[i-1][j-b]+a)
        dp[i][j] = max(b_ij, dp[i-1][j])

for i in range(ASUM+1):
    a = dp[N][i]
    if a < M: continue
    print(i)
    break
```

##  백준 12920, 평범한 배낭 2
*   무게 a와 만족도 b와 개수 c에 대하여
    *   메모리 a에 최대값 제한과 요소별 개수 제한이 존재할 때
    *   만족감 b의 최댓값

### 기존 방법 응용
*   dp 테이블 구성
    *   종: 물품들의 종류, 무게
    *   열: 만족감 (가능한 최대 만족감, 즉 만족감까지)
    *   값: 선택 횟수, 누적 무게
*   이때 임의의 만족도 $n_1$에서 최소 만족감을 가지는 요소들의 분포가 임의의 만족도 $n_2$에서도 최소임을 장담할 수 있는가?

```py
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]

N, M = readVector()
items = [readVector() for _ in range(N)]

X= sum(map(lambda x: x[1]*x[2], items))

dp = [[0 for _ in range(N+1)]for _ in range(X+1)]

for curr in range(X+1):
    for i in range(N):
        v, c, k = items[i]
        prev = curr - c

        if prev < 0: continue
        if dp[prev][i] >= k: continue

        w = dp[prev][N] + v 
        if dp[prev][N] + v > M: continue
        if dp[prev][N] > 0 and w >= dp[curr][N]: continue

        if prev > 0 and dp[prev][N] == 0: continue

        dp[curr] = dp[prev][:]
        dp[curr][N] += v
        dp[curr][i] += 1

answer = 0
for x in range(X+1):
    if dp[x][N]:
        answer = x
print(answer)
```

### 조건 축소
*   각 요소별 개수를 쪼개서 요소를 나누는 방법
    *   예를 들어 무게 a와 만족도 b인 요소의 개수가 7개라면, 이는 $(a, b)$, $(2a, 2b)$, $(4a, 4b)$인 요소가 1개씩 존재하여 이들을 선택하는 것과 같다.
    *   이는 $(a,b)$인 요소가 7개 존재하는 것과도 같은데, 이는 요소 자체의 개수가 너무 많아서 2의 지수배로 요소의 개수를 나눈 것보다 효율성이 떨어진다.
```py
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]

N, M = readVector()
items = []
for _ in range(N):
    v,c,k = readVector()
    i = 1
    while k > 0:
        x = min(i,k)
        items.append([v*x, c*x])
        k -= x
        i *= 2

N = len(items)

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    a, b = items[i]
    for k in range(1,M+1):
        if k < a:
            dp[i+1][k] = dp[i][k]
        else:
            dp[i+1][k] = max(dp[i][k], b + dp[i][k-a])

print(dp[N][M])
```

### 조건 축소 최적화
```py
# https://www.acmicpc.net/source/54555369
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]

N, M = readVector()
dp = [0 for _ in range(M+1)]

for i in range(N):
    v, c, k = readVector()
    
    if v > M: continue
    
    count = 1
    while k > 0:
        if k < count:
            count = k
            
        for j in range(M, v*count-1, -1):
            dp[j] = max(dp[j], dp[j-v*count]+c*count)
        k -= count
        count *= 2

print(dp[M])
```