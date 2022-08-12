#   Chapter 1

##  1.1 운영체제가 할 일
(Silberschatz:1.1) 또는 (Silberschatz:pp4-5)

*   사용자 관점: 운영체제를 사용의 용이성을 목적으로 설계
*   시스템 관점: 운영체제를 자원을 효율적이고 공정하게 할당하는 목적과 프로그램 및 기타 입출력 장치를 제어하기 위한 목적으로 설계

##  1.5 자원 관리

### 1.5.1 프로세스 관리, p29
하나의 프로그램은 디스크에 저장된 파일의 내용과 같인 수동적(passive) 개체이지만, 프로세스는 다음에 수행할 명령을 지정하는 프로그램 카운터를 가진 능동적(active) 개체이다.

##  2.7 운영체제 설계 및 구현
### 2.7.1 설계 목표 Design Goals
설계목표는 사용자 관점과 시스템 관점

### 2.7.2 기법과 정책 Mechanism and Policy
p88
한 가지 중요한 원칙은 기법으로부터 정책을 분리하는 것이다.
기법은 어떤 일을 **어떻게** 할 것인가를 결정하는 것이고, 정책은 **무엇**을 할 것인가를 결정하는 것이다.

p89
마이크로 커널 기반 운영체제는 프리미티브 빌딩 블록의 기본 집합을 구현함으로써 기법과 정책의 분리를 극단적으로 추구한다.
이 블록들은 정책으로부터 거의 자유로우며, 더 고급의 기법과 정책들이 사용자 프로그램 자체를 통해 첨가될 수 있도록 한다.
(중략)
반면 Microsoft는 Windows 운영체제를 실행하는 모든 장치에서 전체적인 모양과 느낌을 통일하기 위해 기법과 정책이 밀접해지도록 인코딩 하였다.

### 2.7.3 구현 Implementation

##  2.8 운영체제 구조
*   모놀리식 구조  Monolithic Structure
*   계층적 접근 Layered Approach
*   마이크로커널 MicroKernels
*   모듈 Moudles
*   하이브리드 시스템 Hybrid Systems

### 2.8.3. 마이크로커널
p94
이 방법은 모든 중요치 않은 구성요소를 커널로부터 제거하고, 그들을 별도의 주소 공간에 존재하는 사용자 수준 프로그램으로 구현하여 운영체제를 구성하는 방법이다.
(중략)
마이크로커널 접근법의 한 가지 장점은 운영체제의 확장이 쉽다는 것이다. 모든 새로운 서비스는 사용자 공간에 추가되며, 따라서 커널을 변경할 필요가 없다.

pp94-95
마이크로커널은 서비스 대부분이 커널이 아니라 사용자 프로세스로 수행되기 때문에 또한 더욱 높은 보안성과 신뢰성을 제공한다. 만일 한 서비스가 잘못되더라도, 운영체제의 다른 부분은 아무런 영향을 받지 않는다.

p95
안타깝게도 마이크로 커널은 가중된 시스템 기능 오버헤드 때문에 성능이 나빠진다. 두 개 사용자 수준 서비스가 통신해야 하는 경우, 별도의 주소 공간에 서비스가 존재하기 때문에 메세지가 복사되어야 한다. 또한 운영체제는 메시지를 교환하기 위해 한 프로세스에서 다음 프로세스로 전환해야 할 수도 있다.

### 2.8.4 모듈
p95
적재가능 커널 모듈(LKM, Loabable Kernel Moudles) 접근법에서 커널은 핵심적인 구성요소의 집합을 가지고 있고 부팅 때 또는 실행 중에 부가적인 서비스들을 모듈을 통하여 링크할 수 있다.

사견: 계층 구조와 마이크로 커널의 장점만 취하고 단점을 보완하는 방식.

### p98
Darwin은 Mach 트랩과 BSD 시스켐 콜을 사용하는 커널이다.

##  2.10 운영체제 디버깅

### 2.10.4 BCC
BCC stands for BPF Compiler Collection

p109
BCC는 eBPF(extended Berkeley Packet Filter) 도구에 대한 프론트엔드 인터페이스이다.

#   Chapter 3

p119
활성화 레코드(activation record)

p126
스와핑

p135
연쇄적 종료(cascading termination)

## 3.4 프로세스 간 통신
p137
시스템에서 실행 중인 다른 프로세스들과 데이터를 공유하지 않는 프로세스는 독립적이다.
시스템에서 실행 중인 다른 프로세스들에 영향을 주거나 받는 프로세스는 협력적이다.

*   프로세스 간 협력을 허용하는 이유는 다음과 같다.
    *   정보 공유(information sharing)
    *   계산 가속화(computation speedup)
    *   모듈성(modularity)

사견: 정보 공유를 제외하면 프로세스 간 협력(또는 통신)은 계산 가속화와 모듈성을 보조하는 수단이지 그 이유나 목적은 아니라고 생각한다.

노트:
*   IPC 기법들
    *   공유 메모리
    *   메세지 전달
        *   직접 통신 vs 간접 통신
        *   동기식 통신 vs 비동기식 통신
        *   자동 또는 명시적 버퍼링

##  3.6 메시지 전달 시스템에서의 프로세스 간 통신

p145
메시지 전달은 봉쇄형(blocking)이거나 비봉쇄형(nonblocking) 방식으로 전달된다.
이 두 방식은 동기식, 비동기식이라고도 알려져 있다.

*   봉쇄형 보내기: 송신하는 프로세스는 메시지가 수신 프로세스 또는 메일박스에 의해 수신될 때까지 봉쇄된다.
*   비봉쇄형 보내기: 송신하는 프로세스는 메시지가 메세지를 보내고 작업을 재시작한다.
*   봉쇄형 받기: 메시지가 이용 가능할 때까지 수신 프로세스가 봉쇄된다.
*   비봉쇄형 받기: 송신하는 프로세스가 유효한 메시지 또는 널(null)을 받는다.

`send()`와 `receive()`가 모두 봉쇄형일 때, 우리는 송신자와 수신자 간에 랑데부(rendezvous)를 하게 된다.

##  3.7 IPC 시스템의 사례
*   POSIX 공유 메모리
*   Mach 메세지 전달
*   Windows ALPC, advanced local procedure call facility
*   pipe

##  3.8 클라이언트 서버 환경에서의 통신
*   socket
*   rpc, remote procedure call

p162
1024 미만의 모든 포트는 well-known 포트로 간주되며 표준 서비스를 구현하는 데 사용된다.


#   Chapter 4

##  4.3 다중 스레드 모델
*   다대일 모델
*   일대일 모델
*   다대다 모델

사견:
다대일 모델에서 유저 스레드 하나가 시스템 콜을 하거나 인터럽트를 일으키면 해당 프로세스(또는 스레드)의 모든 유저 스레드가 블로킹되며, 멀티 코어 시스템에는 유저 스레드를 할당할 수 없다.

##  4.4 스레드 라이브러리
*   POSIX pthrad
*   Windows thread
*   Java thread

##  4.5 암시적 스레딩 Implicit Threading
암묵적 스레딩: 스레딩 생성과 관리 책임을 개발자로부터 컴파일러와 런타임 라이브러리에게 넘겨주는 전략.

사견: 마치 메모리 관리를 Garbage Collector가 해주는 것과 유사하다.

*   thread pool
*   fork-join model
*   OpenMP
*   GCD, Grand Central Dispatch (for Apple)
*   Intel TBB, Thread Building Blocks

##  4.6 스레드와 관련된 문제들 Threading Issues

### 4.6.3 스레드 취소
p208
취소되어야할 스레드를 목적 스레드라고 한다.

*   비동기식 취소(asynchronous cancellation): 한 스레드가 즉시 목적 스레드를 강제 종료시킨다.
*   지연 취소(deferred cancellation): 목적 스레드가 주기적으로 자신이 강제 종료되어야 할지를 점검한다. 이 경우 목적 스레드가 질서정연하게 강제 종료될 수 있는 기회가 만들어진다.

### 4.6.5 스케줄러 액티베이션
(이건 원문을 봐야 이해할 수 있을 듯)

p210
다대다 또는 두 수준 모델을 구현하는 많은 시스템은 사용자와 커널 스레드 사이에 중간 자료구조를 둔다. 이 자료구조는 통산 경량 프로세스 또는 LWP(Light Weight Process)라고 불린다.

p211
커널은 어플리케이션에 가상 처리기(LWP) 집합을 제공하고, 어플리케이션은 유저 스레드를 가상 처리기에 스케줄한다. 커널은 어플리케이션에 대해 특정 이벤트를 알려줘야 하는데, 이 프로시저를 upcall이라고 한다. upcall은 스레드 라이브러리의 upcall에 의해 처리되고, upcall 처리기는 가상 처리기에서 실행되어야 한다.

#   Chapter 5

##  5.3 스케줄링 알고리즘
*   FCFS, First Come First Served Scheduling
*   SJF, Shortest Job First Scheduling
*   RR, Round Robin Scheduling
*   Priority Scheduling
*   Multilevel Queue Scheduling
*   Multilevel Feedback Queue Scheduling

호위 효과(convoy effect)

##  5.5 다중 프로세서 스케줄링
*   AMP: common-ready queue
*   SMP: per-core run queues

### 5.5.3 부하 균등화 Load Balancing
*   push 이주: 바쁜 프로세서가 쉬고 있는 프로세서에 프로세스를 보내는 것
*   pull 이주: 쉬고 있는 프로세서가 바쁜 프로세서를 기다리는 프로세스를 가져와서 실행

##  5.6 실시간 CPU 스케줄링 Real-Time CPU Scheduling
*   지연시간 최소화 Minimizing Latency
    *   전체 지연 시간 = 인터럽트 지연시간 + 디스패치 지연 시간
*   Priority Based Scheduling
*   Rate Monotonic Scheduling
*   EDF, Earliest-Dealing-First Scheduling
*   Proportionate Share Scheduling

##  5.8 알고리즘의 평가
*   결정론적 모델링
*   큐잉 모델
*   시뮬레이션


#   Chapter 6
*   Critical Section Problem
*   Peterson's Solution

*   hardware support for synchronization
    *   memory barrier
        *   강한 순서:
        *   약한 순서: 
    *   hardware instruction for swap
    *   atomic variable
*   mutex: spin lock and semaphore

##  pp286-287

1.  상호 배제가 제대로 지켜진다는 사실. Mutual exclusion is preserved.
    *   어떤 프로세스가 자기의 임계구역에서 실행된다면, 다른 프로세스들은 그들 자신의 임계구역에서 실행될 수 없다.
2.  진행에 대한 요구 조건을 만족한다는 사실. The progress requirement is satisfied.
    *   자기의 임계구역에서 실행되는 프로세스가 없고 그들 자신의 임계구역으로 진입하려는 프로세스들이 있다면, 나머지 구역에서 실행 중이지 않은 프로세스들만 다음에 누가 그 임계구역으로 진입할 수 있는지를 결정하는 데 참여할 수 있으므로, 이 선택은 무한정 연기될 수 없다.
3.  대기 시간이 한없이 길어지지 않는다는 사실. Bounded-waiting requirement is met.
    *   프로세스가 자기의 임계구역에 진입하려는 요청을 한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 그들 자신의 임계구역에 진입하도록 허용되는 횟수에 한계가 있어야 한다.


##  p290
Peterson의 해결안은 최신 컴퓨터 아키텍처에서 작동한다고 보장되지 않는다. 주된 이유는 시스템 성능을 향상하기 위해 프로세서 및 / 또는 컴파일러가 종속성이 없는 읽기 및 쓰기 작업을 재정렬할 수 있기 때문이다.

##  6.5 Mutex Locks
p299
일반적인 규칙은 라기이 유지되는 기간이 문맥 교환을 두 번 하는 시간보다 짧은 경우 스핀락을 사용하는 것이다. (부연: 스레드를 대기 상태로 옮기기 위한 문맥 교환과 락이 사용 가능해질 때 대기 중인 스레드를 복원하기 위한 문맥 교환 총 두 번)

(중략)

스핀락은 프로세스가 락을 기다려야 하고 문맥 교환에 상당한 시간이 소요될 때 문맥 교환이 필요하지 않다는 장점이 있다. 멀티 코어 시스템의 특정 상황에서는 실제로 락이 필요할 때 스핀락이 선호된다.

##  6.6 Semaphore
세마포 S는 정수 변수인데 초기화를 제외하면 표준 원자적 연산 wait과 signal로만 접근할 수 있다. 즉 한 스레드가 세마포 값을 변경할 때, 다른 어떤 스레드도 동시에 동일한 세마포 값을 변경할 수 없다.

즉 세마포 S는 자원의 점유 상태를 나타내는 변수이다.

*   counting semaphore
*   binary semaphore

p300: 이진 세마포는 mutex lock과 유사하게 동작한다.

##  사견
mutex에서는 acquire와 release, semaphore에서는 wait과 signal을 구현하는 방법에는 busy waiting과 process sleep이 있다. 전자는 스핀락(spinlock)이라고 하는데, p299에 관련 내용이 있다.

##  6.7 Monitors
p304
프로그래머가 세마포를 잘못 사용하면 다양한 유형의 오류가 너무나도 쉽게 발생할 수 있다. 이러한 오류를 처리하기 위한 한 가지 전략은 간단한 동기화 도구를 통합하여 고급 언어 구조물을 제공하는 것이다. 이 절에서는 근본적인 고급 언어 구조물 중 하나인, 모니터(monitors) 형을 설명한다.

##  6.8 Liveness
p311: 무기한 대기하는 프로세스는 "라이브니스 실패"의 한 예이다.

*   데드 락
*   우선순위 역전


#   Chapter 7
##  7.1
*   The Bounded-Buffer Problem
*   The Readers-Writers Problem
*   The Dining-Philosophers Problem

### 7.1.2 The Readers-Writers Problem
reader들의 작업은 데이터에 영향을 미치지 않지만, writer의 작업은 데이터에 영향을 미친다.
따라서 writer와 reader가 데이터에 동시에 접근하면 reader는 잘못된 데이터를 읽을 수 있다.
따라서 writer가 쓰기 작업을 하는 동안에 공유 데이터(베이스)에 대해 배타적 접근 권한을 가지게 할 필요가 있다.
이 문제를 reader-writers 문제라고 한다.

여기에는 reader에게 우선권을 주는 방법과 writer에게 우선권을 주는 방법이 있다.
전자는 writer가 후자는 reader가 기아 상태에 빠질 수 있다.


#   Chapter 8
##  8.2.1 Livelock
데드락은 두 개 이상의 스레드가 서로 진행되는 것을 방해하지만, 라이브락은 스레드가 실패한 행동을 계속 시도할 때 발생한다.

예를 들어 이미 락이 걸린 변수에 대해서 다시 락을 걸 수 없는데, 락을 걸 수 없는 경우에 다시 락을 거는 작업을 실행하는 코드의 경우 무한 루프에 빠지게 된다(라이브니스 장애).

이는 두 개 이상의 스레드에서 발생할 수도 있지만, 스레드가 1개인 경우에도 가능하다.

##  8.3 교착 상태 특성 Deadlock Characterization
*   필요조건
    1.  상호 배제: mutual exclusion
    2.  점유하며 대기: hold-and-wait - 최소 1개 자원을 점유하며 다른 자원을 요구하는 경우
    3.  비선점: no premmption
    4.  순환 대기: circular wait

##  8.4 교착 상태 처리 방법
교착 상태 처리 기법은 크게 예방(prevention)과 회피(avoidance) 기법으로 구분할 수 있다.

##  8.5 교착 상태 예방

##  8.6 교착 상태 회피
### 8.6.3 은행원 알고리즘 Banker's Algorithm


#   Chapter 9
### 9.2.3 단편화 Fragementation
*   외부 단편화: 전체 메모리 공간은 충분한데 가용 공간이 작게 쪼개어져 있어 공간을 할당할 수 없는 경우
*   내부 단편화: 할당된 공간이 요청된 공간보다 큰 경우 - 보통 공간을 할당할 때 할당 단위의 정수배만큼 할당하기 때문에 발생하는 문제. 남는 공간은 이미 할당되었기 때문에 남는 공간만큼의 메모리 할당 요청이 들어와도 해당 메모리 공간 전체가 할당 해제되기 전까지는 절대 할당할 수 없다.


#   Chapter 10
##  10.4 페이지 교체
요구 페이징 기법을 사용하면 프로세싱 정도를 높일 수 있다.
예를 들어 모든 프로세스가 10개 페이지 중 5개 페이지만 사용한다면, 사용하지 않는 5개 페이지는 디스크(보조 저장장치)에 할당할 수 있다. 따라서 메모리 제약 상 할당 가능한 프로세스 개수의 2배를 생성하여 스케줄링 할 수 있다.
즉, CPU 활용률과 처리율(throughput)을 높일 수 있다.

문제는 그렇게 프로세스를 엄청나게 많이 생성해서 스케줄링하고 있는데, 갑자기 프로세스들이 나머지 5개 페이지를 요구하게 되는 경우에 발생한다(메모리 과할당 over-allocating).
메인 메모리가 페이지로 가득찼는데도 프로세스들에서는 페이지를 요구하게 된다.

이때가 바로 페이지 교체가 필요한 시점이다.

(하지만 프로세스 자체가 매우 많은 경우에는 프로세스가 교체될 때마다 페이지 교체를 요청하게 되므로 오히려 효율성이 떨어진다. 이렇게 메모리 공간 대비 프로세스가 너무 많아 페이지 교체 요청이 과도한 경우를 스레싱이라고 한다)

### 페이지 교체 알고리즘
*   FIFO
*   OPT
*   LRU
    *   counter을 이용한 구현
    *   stack을 이용한 구현
*   LRU 근사
    *   부가적 참조 비트 알고리즘
    *   2차 기회 알고리즘
*   LFU
*   MFU
*   페이지 버퍼링 알고리즘


#   Chapter 11
NVM: Non-volatile Memory Device 비휘발성 메모리 장치

##  11.2 디스크 스케줄링
HDD에서는 디스크 접근 시간 때문에 아래의 방식들을 사용하지만, NVM에서는 모든 메모리 위치의 접근 시간이 동일하므로 FCFS 또는 NOOP(in linux)를 사용한다.

*   FCFS: First Come First Serve
*   SCAN
*   CSCAN
*   deadline scheduler in linnux
*   CFQ: Completely Fair Queuing

##  11.5 저장장치 관리
*   파티션: 물리적인 디스크 분할 방식
*   볼륨: 논리적인 디스크 분할 방식

##  11.8 RAID
Redundant Array of Inexpensive/Independent Disk

과거에 RAID은 소수의 비싼 디스크들을 다수의 값싼 디스크들로 대체하는 방법으로 사용되었지만, 현재는 경제적 이유보다는 높은 신뢰성과 높은 데이터 전송률 때문에 사용된다.
그래서 RAID의 'Inexpensive'도 최근에는 'independent'를 나타내는 것으로 본다.


#   Chapter 12

##  12.2 입출력 하드웨어
*   I/O-mapped I/O: 입출력과 메모리를 분리. 별도의 입출력 명령이 필요하다.
*   Memory-mapped I/O
    *   메모리 접근 명령을 통해 입출력 연산을 구현할 수 있다.

DMA Controller: Direct Memory Access Controller

*   인터럽트 처리기
    *   FLIH: 1차 인터럽트 처리 - 문맥 교환, 상태 저장 및 처리 작업을 큐에 삽입 등
    *   SLIH: 1차 인터럽트 처리 - 스케줄된(큐에 삽입된) 처리 작업을 수행

##  12.6 STREAMS
스트림