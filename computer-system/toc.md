#   Table of Contents

##  기초
*   Computer Instructions
*   Computer Operations (CS:APP)
*   Computer Circuits (CODME)

##  프로세서
*   Single Cycle Processor
*   Multi  Cycle Processor
*   Pipelining

##  메모리







아래는 예전 목차

---

##  Part I. Processor

### Overview
*   폰 노이만 아키텍처 vs Harvard 아키텍처
*   Instruction Cycle
    *   단순 순서도가 아니라 회로 동작이 어느 정도 반영된 도안
*   명령어 기본
    *   명령어 형식
    *   피연산자 접근 방식 = 주소 지정 방식
*   성능 측정 지표

### Bitwise Operations
logical shift, arithmetic shift, and, or, not, xor 등
Boolean Algebra 해당함.
*   algorithm: bitmasking

### Integer Arithmetic in Computer System
부호 없는 정수
부호 절대치, 1의 보수, 2의 보수
정수 산술: 덧셈, 곱셈, 나눗셈

### Float Arithmetic in Computer System
IEE754
AVX, SSE 등

### Control
*   분기 branch
    *   무조건 분기: jump(goto)
    *   조건부 분기: 순환 loop, switch/case
*   프로시저 Procedure
    *   security issue: buffer overflow exlpoit
*   algorithm: 재귀 vs 순환


### Parallelism for Processor
Concurrency vs Parallelism
명령어 수준 병렬성: ILP
스레드 수준 병렬성; TLP - SMT vs TMT

파이프라이닝, 슈퍼파이프라이닝, 슈퍼스칼라, 분기 예측, 레지스터 재명명

SMP (vs AMP) vs MPP
UMA vs NUMA

GPU

### Interrupt and Exception
*   ISR: Interrupt Service Routine
*   IVT: INterrupt Vector Table

### Compilation and Execution
어떻게 코드가 명령어의 열이 되는가?
컴파일 단계
어플리케이션 코드의 symbol 처리: symbol table
정적 링크와 동적 링크
api와 abi

### Virtualization
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