#   Virtual Memory

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