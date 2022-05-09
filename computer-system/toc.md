#   Table of Contents

여담: 컴퓨터 시스템의 컴포터넌트 및 개념 간 연관성(또는 의존성)이 매우 강해서 순서대로 설명하는 걸 포기해야할 것 같다.

단원별 내용 구성:
RISC vs CISC 차이점: MIPS(or ARM) vs Intel x86
application programming level
instruction architecture level
hardware implementation level
(+) security issue(ex: Intel CPU gate)

단원별 내용 구성 세부 계획:
application programming level은 주로 C 명세나 코드 작성 레벨 또는 컴파일러 단계에서의 효율성 개선이 해당함.
----명령어 명세----
명령어 구현
*   일반적인 하드웨어 구현
*   주어진 아키텍처 맥락에서 효율성 개선(또는 극대화) 구현
추상적인(또는 수학적인) 접근은 Boolean Algebra, Integer Arithmetic까지일 듯

##  Part I. Processor

##  Overview
*   명령어 기본
    *   명령어 형식
    *   피연산자 접근 방식 = 주소 지정 방식
*   Instruction Cycle
    *   단순 순서도가 아니라 회로 동작이 어느 정도 반영된 도안

##  Bitwise Operations
logical shift, arithmetic shift, and, or, not, xor 등
Boolean Algebra 해당함.

##  Integer Arithmetic in Computer System
부호 없는 정수
부호 절대치, 1의 보수, 2의 보수
정수 산술

덧셈 빠르게 하는 법: 올림수 예견(carry lookahead)

##  Float Arithmetic in Computer System
IEE754
AVX, SSE 등

##  Control
*   분기 branch
    *   조건부 분기: 순환 loop, switch/case
    *   무조건 분기
*   프로시저 Procedure

##  Compilation and Execution
어떻게 코드가 명령어의 열이 되는가?
컴파일 단계
어플리케이션 코드의 symbol 처리: symbol table
정적 링크와 동적 링크
api와 abi


##  Parallelism for Processor
Concurrency vs Parallelism
명령어 수준 병렬성: ILP
스레드 수준 병렬성; TLP - SMT vs TMT

파이프라이닝, 슈퍼파이프라이닝, 슈퍼스칼라, 분기 예측, 레지스터 재명명

SMP (vs AMP) vs MPP
UMA vs NUMA

GPU

##  Virtualization
linux cgroup
hyper-v

##  Part II. Memory

### Memory Hierarchy
레지스터, 캐시, 메인 메모리, 보조 메모리

### Virtualization on Memory
가상 메모리, 스왑
Hardware Segmentation(Intel), Hardware Paging
Software Segmentation and Paging (on kernel) - 간략히

### Parallelism on Memory
Partioning과 RAID도 사실 가상화(자원 가상화)에 포함되는 개념이긴 하다.