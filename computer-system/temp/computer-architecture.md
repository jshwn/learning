#   Computer Architecture

조건부 분기 구현: 제어의 조건부 전환(3.16.c) vs 데이터의 조건부 전송(3.17.c)

순차적 실행 vs 파이프라이닝 vs 슈퍼스칼라(무순서 실행)
IPC: Instructions Per Cycle

SMT 구현하는 방법: ILP, TLP

ILP: 명령어 수준 병렬화, Instruction Level Parallelization
ILP 구현 방법: 명령어 파이프라이닝, 슈퍼스칼라, 무순서 실행, 레지스터 재명명(renaming), 분기 예측, 예측 실행(speculative execution)

TLP: 스레드 수준 병렬화(Task Level Parallelization의 일종)

TMT(시간적 멀티스레딩, Temporal Multithreading) vs SMT(동시 멀티스레딩, Simultaneous Multithreading)

SMP(대칭형 다중 처리 Symmetric multiprocessing) vs AMP(Asymmetric multiprocessing)

Classic RISC pipeline
RISC vs CISC
폰 노이만 구조 vs 하버드 구조
플린 분류 Flynn's Taxonomy: SISD, SIMD, MISD, MIMD

벡터 프로세서 vs 스칼라 프로세서(이게 대부분)


#   컴퓨터 동작 계층
응용 프로그램: DB, Server, Compiler 등
운영체제: 프로세스 관리(스케줄링), 메모리 관리(페이징, 스와핑), 파일 시스템, 네트워크 등
컴퓨터 시스템: 프로세서(기초 내용, 파이프라이닝 등), 메모리(캐시 메모리, 메인 메모리, 디스크 메모리) 등


#   노트
칩, 칩셋, 주변장치
Chip, Chipset(Motherboad, M/B가 따르는 인터페이스), Peripheral

유닛 Unit은 논리적인 단위: CPU 안의 부품을 ALU, CU, MMU 등으로 부르는 것이  그 방증

micro processing unit, mpu
micro controlling unit, mcu

chip: 독립적으로 기능하는 집적 회로
die: 독립적으로 기능하지 않는 집적 회로(라고 하기에는 die가 waper에서 잘라낸 사각형이라는 의미여서 이렇게 정의하기는 힘들 듯)

===
마이크프로세서 이전에는 프로세서에 필요한 부품들을 일일이 기판에 납땜했다고 생각하면 편하다.
"칩"이라는 개념은 이러한 부품들을 모아 놓은, 물리적으로 구분되는 단위라고 보면 된다.
처음에는 칩에 CPU 기능만 넣고 칩과 시스템에 필요한 부품(GPU, RAM, HDD 등) 및 주변장치를 연결하여 사용하였다.
하지만 나중에는 기술이 발전하여 하나의 칩에 시스템 부품까지 포함하기도 한다(SoC).

1.  마이크로프로세서: ALU, CU, FPU, MMU, 레지스터, 캐시(L1, L2, L3) 등
2.  마이크로컨트롤러: 마이크로프로세서, RAM, SSD(HDD는 불가능), GPU, NPU 등

멀티 프로세서: 여러 개의 칩
멀티코어 프로세서: 1개의 칩

싱글 코어 -> 멀티 코어

일괄 처리: Batch processing
다중 프로그래밍: Multi-programming
다중 작업: Multi-tasking
다중 처리: Multi-processing

일괄 처리 -> 다중 프로그래밍 -> 다중 작업(협력 또는 선점) -> 다중 처리
다중 처리: 멀티코어 프로세싱 or 분산 컴퓨팅

전력 장벽(또는 4Ghz의 벽)

##  성능 측정
Clock frequency 클럭 주파수: 물리적 개념. Hz(clock cycles per second)로 측정.
Clock cycle 클러 주기: 물리적 개념. s 또는 ps로 측정
Instruction cycle: 논리적 개념

클럭 주기에 역수를 취하면 1 clock cycle 동안 걸린 시간을 의미한다.
latency: 어떤 명령(instruction일수도 있고 그 하위 단위일 수도 있음)이 시작해서 종료할 때 까지 걸리는 시간. latency 자체는 추상적 개념이지만 어떤 단위 명령에 대한 latency가 되면 물리적 개념이 됨.

최신 로직 설계에서는 회로 지연 시간을 피코-초(picosecond, 1ps=10^-12 second) 단위로 측정한다.
그리고 ips(초당 명령어 실행 횟수, instructions per second)는 회로 지연 시간의 역수에 시간 단위를 조정(10^12)한 값이 된다.

인스트럭션마다 걸리는 평균 클럭 사이클(CPI, Clock cycle per instruction).
파이프라인의 CPI는 최대 1

파이프라인을 사용하지 않는 CPU는 



#   정리

##  Concurrency and Parallelism
임의의 instruction A, B는 다음과 같이 실행될 수 있다.
*   software context, hardware context
*   sequential   serial    1:(A1), 2:(A2), 3:(A3), 4:(B1), 5:(B2), 6:(B3)
*   sequential,  parallel  1:(A1, A2), 2:(A3, B1), 3:(B2, B3)
*   concurrent,  seiral    1:(A1), 2:(B1), 3:(A2), 4:(B2), 5:(A3), 6:(B3)
*   concurrent,  parallel  1:(A1, B1), 2:(A2, B2), 3:(A3, B3)

##  여담: Synchronous and Blocking
Concurrency와 Parallelism의 개념은 마치 Synchronous와 Blocking의 개념과 유사하다.
즉, 각 개념 관계에 대하여 그 개념들은 서로 구분되지만 비슷해서 혼동하기 쉽다는 점에서 두 관계는 비슷하다.
*   Synchronous,  Blocking
*   Synchronous,  Non-blocking
*   ASynchronous, Blocking
*   ASynchronous, Non-blocking

##  Parallelism

##  Multithreading: hardware context
*   TMT는 가장 기본적인 명령어 파이프라이닝(하나의 사이클에서 그리고 하나의 파이프라인 stage에서 실행 가능한 스레드가 1개)
*   SMT는 슈퍼스칼라