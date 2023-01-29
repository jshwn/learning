#   동전

*   coin: coin의 value
*   count: 한 case에서 coin의 개수
*   case: 각 coin별 개수

$$
\text{coins}_{\ k} = \left[ \text{coin}_{\ 0}, \; \dots, \text{coin}_{\ k-1} \right]
\\[10px]
\text{case}^{\ n}_{\ k} = \left[ \text{count}_{\ 0}, \; \dots, \text{count}_{\ k-1} \right],
\\[10px]
n = \sum^{n-1}_{i=0} \ \text{count}_{\ i}
\\[10px]
\text{cases}^{\ n}_{\ k} = \{\ \text{all possible case}^{\ n}_{\ k} \ \},
\\[10px]
n \left( \text{cases}^{\ n}_{\ k} \right) = \ _{n}C _{ k}
\\[10px]
\text{value} = \text{coins}_{\ k} \times \left( \text{case}^{\ n}_{\ k} \right)^{\ T}
$$

*   보통 문제에서는 $\text{coins}_{\ k}$는 고정되어 있다.
*   문제 종류
    *   특정 $\text{value}$를 만족하는
        *   $\text{case}^{\ n}_{\ k}$의 개수
        *   최소 $n$을 가지는 $\text{case}^{\ n}_{\ k}$
        *   최대 $n$을 가지는 $\text{case}^{\ n}_{\ k}$

##  백준 9084 동전
*   주어진 $\text{coins}_{\ k}$에서 $X = \text{coins}_{\ k} \times \left( \text{case}^{\ n}_{\ k} \right)^{\ T}$ 를 만족하는 $n \left( \text{cases}^{\ n}_{\ k} \right)$

*   예시
    *   $\text{coins}_{\ 2} = \left\{1, \ 5 \right\}$
    *   $\text{cases}^{\ 1}_{\ 2} = \left\{ \left\{1, \ 0 \right\}, \;\ \left\{0, \ 1 \right\} \right\}$
    *   $\text{cases}_{\ 2} = \left\{ \left\{1, \ 0 \right\}, \;\ \left\{0, \ 1 \right\}, \;\ \left\{2, \ 0 \right\}, \;\ \cdots \right\}$
    *   $\text{values}= \left\{  1, \;\ 5, \;\ 2, \;\ \cdots \right\}$
    *   $n \left(  \text{cases}_{\ 2} \right) \text{where} \;\ \text{value}_{\ 2} = X(= 1,000)$

```py
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]
readScalar = lambda: int(stdin.readline().rstrip())

answers = []

T = readScalar() # Test Case
for _ in range(T):
    N = readScalar() # number of coins
    coins = readVector() # value per coin, 요소의 순서는 상관이 없음.
    M = readScalar() # price

    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    for coin in coins:
        for m in range(1, M+1):
            if m < coin: continue
            dp[m] += dp[m-coin]
    
    answers.append(str(dp[M]))

print("\n".join(answers))
```

##  백준 2293 동전 1
*   특정 value X를 만족하는 case의 개수
*   백준 9084 동전과 같은 문제

```py
from sys import stdin
readVector = lambda: [*map(int, stdin.readline().rstrip().split(' '))]
readScalar = lambda: int(stdin.readline().rstrip())

N, M = readVector()
coins = [readScalar() for _ in range(N)]

dp = [0 for _ in range(M+1)]
dp[0] = 1
for coin in coins:
    for m in range(coin, M+1):
        dp[m] += dp[m-coin]

print(dp[M])
```

##  백준 2091 동전
만족해야 하는 value X와 value별 coin의 개수가 주어진다.
이때 value X인 coin들의 조합 중에서 coin의 최대 개수를 구해야 한다.

```py
#   value X를 만족시키는 최대 개수
X, *maxCounts = map(int, input().split())
# X, maxCounts = 12, [5, 3, 1, 2]

coins = [1, 5, 10, 25] # 동전의 종류

dp = [[0,0,0,0,-1] for _ in range(X+1)]
dp[0] = [0 for _ in range(5)]

for curr in range(1, X+1):
    for i in range(4):
        coin = coins[i]
        maxCount = maxCounts[i]
        prev = curr - coin

        if prev < 0: continue
        if dp[prev][4] <= dp[curr][4]: continue
        if dp[prev][i] >= maxCount: continue
        
        dp[curr] = dp[prev][:]
        dp[curr][i] += 1
        dp[curr][4] += 1

print(*dp[X][:-1])
```

##  조합 계산
$$
\binom{n}{k} = \binom{n-1}{k-1} +\binom{n-1}{k}
\\[10px]
\binom{n}{0} = \binom{n}{n} = 1, \ \binom{n}{1} = n
$$

