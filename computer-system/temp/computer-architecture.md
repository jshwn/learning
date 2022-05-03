#   Computer Architecture

조건부 분기 구현: 제어의 조건부 전환(3.16.c) vs 데이터의 조건부 전송(3.17.c)

순차적 실행 vs 파이프라이닝 vs 슈퍼스칼라(무순서 실행)

ILP: 명령어 수준 병렬화, Instruction Level Parallelization
TLP: 스레드 수준 병렬화(Task Level Parallelization의 일종)

TMT(시분할 멀티스레딩, Temporal Multithreading) vs SMT(동시 멀티스레딩, Simultaneous Multithreading)

SMP(대칭형 다중 처리 Symmetric multiprocessing) vs AMP(Asymmetric multiprocessing)

Classic RISC pipeline
RISC vs CISC
폰 노이만 구조 vs 하버드 구조
플린 분류 Flynn's Taxonomy: SISD, SIMD, MISD, MIMD

벡터 프로세서 vs 스칼라 프로세서(이게 대부분)


#   컴퓨터 동작 계층
응용 프로그램: DB, Server, Compiler 등
운영체제: 프로세스 관리(스케줄링), 메모리 관리(패이징, 스와핑), 파일 시스템, 네트워크 등
컴퓨터 시스템: 프로세서(기초 내용, 파이프라이닝 등), 메모리(캐시 메모리, 메인 메모리, 디스크 메모리) 등