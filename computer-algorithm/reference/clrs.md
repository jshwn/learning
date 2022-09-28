#   CLRS

##  2 Getting started

### insert sort
*   **loop invariant**
    *   Initialization: 초기 조건. 초기 상태가 타당해야 한다.
    *   Maintenance:유지 조건. 매 루프마다 상태가 타당해야 한다.
    *   Termination: 최종 상태가 타당해야 한다.

```swift
/*
    Swift가 예제의 의사코드와 가장 그 구문의 형태가 유사하다고 판단하여
    Swift5를 이용해서 예제를 구현함.
    CLRS에서는 initial index를 1로 취급하는 것을 준용하여
    seq[0]의 값은 구현에서는 존재하되, 알고리즘에서는 취급하지 않는 쓰레기 값이다.
*/
let A = [0, 5, 2, 4, 6, 1, 3]
func insert_sort(A:[Int]) -> [Int] {
    for j in 2...len(A){
        let key = A[j]
        let i = j-1
        while i>=0 && A[i] > key{
            A[i+1] = A[i]
            i = i-1
        }
        A[i+1] = key
    }
}
```
*   `insert_sort`의 루프 불변성 검토
    *   초기 조건: j=1, i=0의 경우 A\[0...j-1\]가 A\[0...0\]=\[5\]이다. 이 배열은 원소가 하나이므로 항상 정렬되어 있다. 따라서 초기 조건은 타당하다.
    *   유지 조건: j=1일 때 A\[0...0(=j-1)\]은 정렬되어 있다. `insert_sort`의 while문이 수행되면 A\[0...1\]은 정렬된다. 그리고 j=2일 때 A\[0...1((=j-1))\]이 정렬되어 있다. 수학적 귀납법에 의해 `insert_sort` 중 어떤 j에 대하여 A\[0...j-1\]은 항상 정렬되어 있다. 따라서 유지 조건은 타당하다.
    *   종료 조건: `insert_sort`의 for문은 j==A.length에서 종료된다. j=A.length에 대하여 A\[0...A.length-1\]이 정렬되어 있으므로 종료 조건은 타당하다.



### merge sort
```swift
func merge(A:List, p:Int, q:Int, r:Int){
    // A = [<trash value>...p....q...r]
    let n_1 = q - p + 1 // p...q까지의 크기
    let n_2 = r - q // r...q까지의 크기

    let L = [Int](repeating: 0, count: n_1)
    let R = [Int](repeating: 0, count: n_2)

    for i in 1...n_1 {
        L[i] = A[p+i-1]
    }
    for j in 1...n_2 {
        R[j] = A[q+j]
    }

    L[n_1+1] = inf
    R[n_2+1] = inf
    var i=1
    var j=1

    for k in p...r {
        if L[i] <= R[j] {
            A[k] = L[i]
            i += 1
        } else {
            A[k] = R[j]
            j += 1
        }
    }
}
```

##  3 Growth of Functions
*   $\Theta (g(n)) = \{ \exists \; c_1>0, c_2>0 \; \text{and} \; c_2>0, \; \text{such \ that} \}  $

$f(n)=\Theta(g(n))$ actually means $f(n) \in \Theta(g(n))$.

*   어떤 알고리즘의 비용 함수가 입력 크기 $n$에 대하여 $f(n)$이라고 하자.
*   어떤 $g(n)$에 대하여 임의의 상수 $c_1$, $c_2$를 상정하자.
*   $g(n)=n^2$, $O(g(n))$은 임의의 자연수 $c$
를 $n^2$에 곱했을 때 모든 $n$에 다하여 $cg(n)$의 값이 $f(n)$보다 크면 $f(n) \in O(n^2)$, 즉 $f(n) = O(n^2)$이다.

*   $O$-notation for asymptotic upper bound
*   $o$-notation for asymptotic bigger
*   $\Omega$-notation for asymptotic lower bound
*   $\omega$-notation for asymptotically smaller
*   $\Theta$-notation for asymptotic tight bound

<br/>

*   $O$-notation: **임의의** 상수 $c$에 대하여 $cg(n) > f(n)$
*   $o$-notation: **모든** 상수 $c$에 대하여 $cg(n) > f(n)$
*   $\Theta$-notation: 임의의 상수 $c$에 대하여 $cg(n) < f(n)$
*   $\Omega$-notation: 임의의 상수 $c$에 대하여 $cg(n) < f(n)$
*   $\omega$-notation: 모든 상수 $c$에 대하여 $cg(n) < f(n)$
*   Example
    *   $2n = o(n^2), \; 2n^2 \neq o(n^2), \; 2n^2 = O(n^2)$ 
    *   $ {1 \over 2}n  = \omega(n^2), \; {1 \over 2}n \neq \omega(n^2)$

### 정리
*   $O(g(n))$ - $f(n)$이 $g(n)$
*   $o(g(n))$
*   $\Omega(g(n))$ - best 
*   $\omega(g(n))$
*   $\Theta(g(n))$

### 수학적 표기법
$$
{a \mod b} = a - n \lfloor{ {a \over n} \rfloor}
$$

$$
\text{functional iteration}
\\[10px]
f^{(i)}(n) = 
\begin{cases}
n & \text{if} \quad i=0 \\
f(f^{(i-1)}(n)) & \text{if} \quad i>0
\end{cases}
$$

##  4 Divide-and-Conquer
*   **recursive case**: which the recursion can recurse
*   **base case**: where the recursion "bottoms out"(no longer recurses)


*   methods for solving recurrence
    *   substitution method
    *   recursion-tree method
    *   master method

### master method

$$
T(n) = a \ T \left( {n \over b} \right) + f(n)
\\[10px]
\text{where} \;
a \geq 1, \ b \geq 1,
\\[10px]
{n \over b} \;\ \text{means} \;\ \lfloor{ {n \over b} \rfloor} \; \text{or} \; \lceil{ {n \over b} \rceil}
$$

$a$는 number of subproblems in the recursion, $b$는 size of subproblem in the recursion

이때 $T(n)$의 점근적 표기는 다음과 같다.
1.  $f(n)=O\left(n^{\log_b a-\epsilon}\right), \exists \; \epsilon > 0 \Rightarrow T(n)=\Theta\left( n^{\log_b a} \right)$
2.  $f(n)=\Theta \left(n^{\log_b a}\right) \Rightarrow T(n)=\Theta\left( n^{\log_b a} \log _2  n \right)$
3.  아직 안 씀

증명은 4.6

### Strassen's algorithm for matrix multiplication
*   strassen's algorithm
    *   CLA, Carry Lookahead Adder와 비슷한 방식

##  Red-Black Trees

### properties
1.  color property: 모든 노드는 black 또는 red이다.
1.  root property: root 노드는 black이다.
2.  external property: 모든 leaf 노드는 black이다.
3.  internal property: red 노드의 자식은 black이다. (red 노드가 연속으로 나올 수 없다)
4.  depth property: 모든 leaf 노드에서 black depth는 같다. (leaf 노드에서 root 노드까지 경로에서 만나는 블랙 노드의 개수는 같다)
    *   CLRS에서는 black height, $\text{bh}(x)$ for node $x$

### T.nil (p309)
the sentinel T: nil is an object with the same attributes as an ordinary node in the tree. Its color attribute is BLACK, and its other attributes—p, left, right, and key—can take on arbitrary values

### operations
*   insert
*   delete
*   rotate
*   maximum
*   minimum


### Rotate
*   the way to keep properties
    *   recoloring
    *   restructuring(rotation)

*   left rotate
*   right rotate