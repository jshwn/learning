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


```py
#   백준 2091, 동전
#   value X를 만족시키는 최대 개수
X, *maxCounts = map(int, input().split())

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


