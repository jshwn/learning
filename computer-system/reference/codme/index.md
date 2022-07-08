#   Chapter 1 컴퓨터 추상화 및 관련 기술

##  1.6 성능
명령어당 클럭 사이클 수 CPI, clock cycles per instruction

CPU 시간 = 명령어 개수 x CPI x 클럭 주기
CPU 시간 = 명령어 개수 x CPI / 클럭 속도

##  1.9 실례: Intel Core i7 벤치마킹

SPEC CPU 벤치마크

##  1.11 오류 및 함정
암달의 법칙 - 수확 체감의 법칙과 비슷한 개념

##  Chapter 2 명령어: 컴퓨터 언어
본서에서 사용할 명령어 집합은 MIPS를 선택했는데, MIPS는 1980년대 이후에 설계돈 명령어 집합들을 대표할만한 것 중 하나이다.


### p141
MIPS에서는 경쟁 관계(race) 문제를 해결하기 위해 load linked/store conditional 매커니즘을 사용한다. 이는 경쟁 관계에 있는 메모리를 읽는 명령어를 `ll`(load linked)와 `sc`(store conditional)로 분리해서 실행하는 것이다.

만약 load linked 명령어에 의해 명시된 메모리 주소의 내용이 같은 주소에 대한 store conditional 명령어가 실행되기 전에 바뀐다면 store conditional 명령은 실패하게 된다. store conditional 명령어는 1.레지스터 값을 메모리에 저장하는 일과 2.성공하면 레지스터 값을 1 아니면 0으로 바꾸는 일을 동시에 수행한다.

(아래는 교재 p141의 예제)

```
again:
(0) addi $t0, $zero, 1
(1) ll   $t1, 0($s1)
(2) sc   $t0, 0($s1)
(3) beq  $t0, $zero, again
(4) add  $s4, $zero, $t1
```

(아래는 스스로 작성한 해설)

만약 s1 레지스터의 값이 100이면, 

(1) MEM\[100\]의 값을 t1으로 적재   \
    ( (1)과 (2) 사이에 다른 프로세스나 프로세서에서 MEM\[100\]의 값을 수정했을 수 있음 ) \
(2) MEM\[100\]의 값과 t1 레지스터의 값을 비교하여   \
    1. 두 값이 같으면 t0 레지스터에 1을 적재    \
    2. 두 값이 틀리면 t0 레지스터에 0을 적재    \
(3) $t0==0이면 위 과정을 다시 반복  \
(4) (1)에서 적재한 $t1을 다른 레지스터에 복사

load linked/store conditional 매커니즘의 또 다른 장점은 atomic compare and swap 또는 atomic fecth-and-increment 같은 다른 동기화 프리미티브를 만드는 데 사용할 수 있다는 점이다. 이러한 프리미티브들은 여러 가지 병렬 프로그래밍 모델에서 사용되며, 이러한 모델에서는 load linked/store conditional 매커니즘 사이에 명령어가 추가로 필요한 경우가 있다.
이때 load link 명령어와 store conditional 명령어 사이에 다른 명령어를 넣을 때 주의해야 한다.


#   Chapter 3 컴퓨터 연산

##  덧셈과 뺄셈

### p207
예외 Exception: 인터럽트라고 하는 컴퓨터도 많이 있다. 프로그램 수행을 방해하는 계획되지 않은 사건. 예를 들면 오버플로우가 탐지에 사용된다.

인터럽트 Interrupt: 프로세서 외부에서 발생하는 예외 (어떤 아키텍처에서는 모든 예외를 인터럽트라고 하기도 한다)

MIPS에는 EPC(exception program counter)라고 불리는 레지스터가 있어서 인터럽트가 걸린 명령어의 주소를 기억하는 데 사용된다. mfc0(move from system control) 명령어는 EPC를 범용 레지스터에 복사하여 MIPS 소프트웨어가 예외 처리 코드를 수행한 후에 점프 레지스터 명령어를 통해 인터럽트가 걸린 명령어로 되돌아갈 수 있게 해준다.

### p208
모듈로 산술 연산 vs 포화(saturation) 산술 연산

모듈로 산술 연산은 값이 지원 범위를 넘어가면 랩어라운드 처리를 해버리지만 포화 산술 연산은 가장 큰 양수나 음수를 결과값으로 한다. 포화 연산은 미디어 연산에서 주로 사용된다. 예를 들어 라디오의 볼륨 손잡이를 계속 돌릴 떄 한동안 소리가 커지다가 갑자기 조용해지면 이상할 것이다. 표준 명령어 집합의 멀티미디어 확장은 포화 산술 연산을 제공하는 경우가 많다.

#   Chapter 4 프로세서

##  논리 설계 관례

### pp286-287
클러킹 방법론
*   에지 구동 클러킹(edge sensitive)
*   레벨 구동 클러킹(level sensitive)

에지 구동 방법론은 경쟁 관계를 발생시키지 안흥면서 같은 클럭 사이클에 상태 소자를 읽고 쓸 수 있게 해준다.

### p310
멀티사이클 구현 관련
https://talkingaboutme.tistory.com/entry/Study-Multi-Cycle-Implementation



#   Chapter 6 병렬 프로세서

##  p580
*   경성 스케일링(strong scaling): 문제의 크기를 고정시킨 상태에서 얻어지는 속도 개선
*   연성 스케일링(weak scaling): 프로세서 수에 비례하여 문제 크기를 증가시키는 경우의 속도 개선