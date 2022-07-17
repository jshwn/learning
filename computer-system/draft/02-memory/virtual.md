#   CODME, 5.7 가상 메모리

##  p488
메인 메모리가 보통 자기 디스크로 구현되는 2차 저장장치(secondary storage)를 위한 "캐시"로 동작할 수 있다. 이 기술을 가상 메모리(virtual memory)라고 부른다.

*   여러 프로그램들(또는 가상머신들)이 효과적이고 안전하게 메모리 공유
*   제한된 크기의 메인 메모리에서 프로그래밍해야 하는 제약을 극복

##  note
페이지 부재(Page fault)란 접근하려는 페이지가 메인 메모리에 없는 상태로, 이때는 디스크에 있는 페이지에 접근해야 한다. (사견: 마치 L1 캐시에 실패했을 때 L2 캐시에 접근하는 것과 같은 모양이다)

하지만 페이지 부재 처리를 위해 디스크에 접근하는 데에는 수백만 사이클이 소요된다.
이러한 실패 손실을 만회하기 위해 다음의 정책을 사용한다.

*   긴 접근시간을 보상할만큼 페이지의 크기가 충분히 커야한다.
*   페이지 부재 발생률을 줄이는 배치 구조와 배치 알고리즘을 사용해야 한다.
*   즉시 쓰기(write through) 대신 나중 쓰기(write back) 방식을 채택한다.

참고로 쓰기의 경우, 디스크 접근 시간이 수백만 사이클이기 때문에 즉시 쓰기 방식은 사실상 불가능하다. (참고로 접근 시간 떄문에 쓰기 버퍼 사용을 전제해도 마찬가지다.)

갱신 비트(dirty bit)를 사용할 경우, 어떤 페이지가 디스크로 page out(또는 swap out)될 때 갱신 비트가 1로 설정되어 있으며 디스크에 이를 쓰고, 갱신 비트가 0으로 설정되어 있으면 페이지의 내용이 변한 게 없으므로 그냥 없애서 성능 향상을 도모할 수 있다. (즉, 갱신 비트는 write back을 전제한다)

### p497 고난도
CS:APP pp788-790에서는 각 프로세스가 4MB의 페이지 테이블 크기를 가지는 문제를 다중 레벨 페이지 테이블 기법을 통해 해결할 수 있다고 기술한다.
반면 CODME에서는 이외에도 여러 방법을 소개한다.

##  TLB
하지만 페이지 테이블 역시 메인 메모리에 있기 때문에 가상 주소를 페이지 테이블에 접근하는 시간과 이를 실제 주소로 변환하여 다시 실제 주소에 접근하는 시간을 합쳐 총 2번 메인 메모리에 접근하게 된다.

그래서 페이지를 캐싱하는 특수한 캐시인 TLB(Table Lookup Buffer)를 사용한다.
단 페이지와 달리 태그로 가상 페이지 번호의 일부분을 사용하고, 블록 데이터로 실제 페이지 번호를 적재한다.

그런데 이런 구조에서 프로세스 문맥 전환이 자주 발생하게 되면 문맥을 전환할 때마다 TLB를 통쨰로 갈아야 한다는 비효율성이 발생한다.
이를 해결할 수 있는 방법으로 프로세스 식별자(process identifier)를 페이지 번호와 붙여서 TLB 태그로 사용한다. 이 방법을 사용하면 문맥 전환이 발생해도 TLB를 통째로 지울 필요가 없다.

##  캐시의 주소 방식( p505 고난도)
*   실제 주소 인덱싱과 실제 주소 태깅
*   가상 주소 인덱싱과 가상 주소 태깅
*   가상 주소 인덱싱과 실제 주소 태깅

이에 대해 CS:APP에서는 pp786-787에서 다음과 같이 기술한다:
대부분의 시스템은 물리 주소 지정을 선택한다. 물리주소를 사용하면, 다중 프로세스들이 캐시에서 블록을 갖는 것과 마찬가지로 가상페이지로부터 블록을 공유하는 것이 단순해진다. 게다가 캐시는 보호 이슈를 다룰 필요가 없는데, 접근 권한이 주소 번역 과정의 일부로 체크되기 때문이다.


##  LRU vs LFU
Least Recently Used

교체 페이지를 랜덤하게 고르는 방식도 있는데 그건 논외로 한다.

직접 사상 캐시에서는 교체 후보가 1개이므로 교체 알고리즘을 고려하지 않는다.
하지만 집합 연관 캐시라면 선정된 집합 내의 블록 중에서 하나를 선정해야 한다.

하지만 연관 정도 큰 집합 연관 캐시에서는 각 블록의 사용 정보를 추적하는 데에 비용이 많이 든다.
이런 경우에는 **LRU 근사 방식**을 사용한다.

LRU 근사 방식은 [clock algorithm](https://jeongmorecord.tistory.com/100)과 분할 비교(CODE p520에서 한 줄로 설명하고 넘어가는 내용에 이름을 붙인 것)이 있다.

가상 메모리는 페이지 폴트가 발생하면 디스크까지 접근해야 하므로 실패 비용이 매우 커서 실패율을 조금이라도 줄이는 것이 중요하다. 그래서 항상 LRU 근사 방식을 채택한다.

##  병렬성과 메모리 계층구조: 캐시 일관성 문제
캐시 일관성 문제 cache coherence problem

일관성(coherence)과 정합성(consistency)

이동(mitigation)과 복제(replication)

캐시 일관성 유지 프로토콜의 종류
출처: https://goodgid.github.io/Cache-Coherence/
*   스누핑(snooping) 프로토콜: 주소 버스를 항상 감시하여 캐시 접근 여부를 확인
*   디렉토리(directory) 프로토콜: 데이트 복사본 감시



#   Segmentation
*   출처: https://en.wikipedia.org/wiki/X86_memory_segmentation
*   출처: https://en.wikipedia.org/wiki/Memory_segmentation
*   참고: https://softwareji.tistory.com/73
(`/computer-system/temp/process-memory.md`의 내용을 보완)


[위키피디아](https://en.wikipedia.org/w/index.php?title=Memory_segmentation&oldid=1086015175)는 세그멘테이션(segmentation)을 "주소 공간을 일정 구간(세그먼트)으로 나누어 사용하는 메모리 관리 기술"로 정의한다.

워드가 16bit였을 때는 지원 가능한 최대 램크기는 64kB(=2^16=2^6*2^10)였다.
그런데 IBM에서 Intel 8086을 출시하면서 16bit 워드로 1MB 램에 접근할 수 있는 세그멘테이션 방식을 도입하였다.

Intel 8086은 1MB 램까지 지원했는데, 16bit 워드 크기로는 1MB=2^20B를 모두 커버할 수가 없었다.
그래서 Intel 8086은 상위 16bit는 세그먼트 베이스, 하위 4bit는 오프셋으로 사용하는 주소 지정 방식을 도입했다.

그래서 램이 1MB인 경우, 각 세그먼트는 16(=2^4)비트 크기의 오프셋을 가질 수 있다.


`lea`와 관련하여 `lds` for DS register, `les` for ES register ... 등의 이슈