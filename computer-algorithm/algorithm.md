#   About Algorithm
##  Definition of Aligorithm
알고리즘에 대한 공식적인 정의는 없다.
비공식 정의이지만 CLRS에서는 알고리즘을 다음과 같이 정의한다(CLRS:1.1).

    알고리즘은 값 또는 값들의 집합을 입력과 출력으로 가지는 잘 정의된 계산 절차이다.

여기서 "잘 정의된"이라는 개념은 그 뜻이 불분명하다.
이에 대해서는 다음 절에서 자세히 기술한다.

##  Expression of Algorithm
알고리즘은 크게 다음의 3가지 방식으로 표한할 수 있다.
1.  natural language
2.  programming language
3.  state diagram

자연어로 알고리즘을 표현할 경우, 절차나 상태에 대한 정보가 모호할 수 있다.

그래서 알고리즘의 내용을 명확하게 정의할 필요가 있다.
이때 명확한 정의는 형식적인 정의와 일맥상통한다.

따라서 앞서 나온 "잘 정의된"이라는 개념은 계산 절차가 형식적으로 정의되었다는 뜻이다.

이를 수학적으로 정의한 것이 바로 state machine이며, 이를 도식화한 것이 바로 state diagram이다.

##  Algorithm Characterization
도널드 크누스는 널리 받아들여지는, 알고리즘이 가져야 하는 5가지 속성을 제시하였다.

1.  Finiteness
2.  Definiteness
3.  Input
4.  Output
5.  Effectiveness

##  Performance of Algorithm
점근 표기법 Asymptotic Notation

비용