#   draft

##  용어 및 개념 정리
*   Clock cycle: 클럭 주기. 클럭이 하나 발생하기까지 걸리는 시간.
*   Clock frequency: 클럭 주파수. 일정 기간 동안 발생한 클럭 횟수. 기본적으로 Hz(clock cycles per second)로 측정한다.

*   Processor = Processing Unit = Central Processing Unit
*   Instruction: Processor를 직접 동작시키는 명령어.
*   Instruction Cycle: Processor가 명령어를 수행하는 세부 단계들(steps or stages)

*   Functional Unit: Execution Stage에서 실제로 instruction을 execute하는 unit
    *   Exampels: ALU, AGU, FPU, MMU, LSU, TLB, BPU(분기 예측 유닛) etc
*   Execution Unit: Instruction Cycle을 수행하는 단위. Fetcher, IDU(명령어 해독 유닛), functional unit, register, cache memory 등을 포함한다.
    *   CSAPP에서는 Execution Unit이 Instruction Cycle에서 Execution Stage를 담당하는 것처럼 여겨지나, Wikipedia에서는 Instruction Cycle 전체를 수행하는 것으로 정의한다.


*   IPC: Instructions Per Clock cycle
*   CPI: Clock cycles Per Instruction
*   CPE: Clock cycles Per Element, 응용프로그램에서 벡터 데이터의 요소 하나를 계산하는 데에 걸리는 평균 클럭 주기


### Concurrency and Parallelism
임의의 instruction A, B는 다음의 순서로 실행될 수 있다.
*   software context, hardware context
*   sequential   serial    1:(A1), 2:(A2), 3:(A3), 4:(B1), 5:(B2), 6:(B3)
*   sequential,  parallel  1:(A1, A2), 2:(A3, B1), 3:(B2, B3)
*   concurrent,  seiral    1:(A1), 2:(B1), 3:(A2), 4:(B2), 5:(A3), 6:(B3)
*   concurrent,  parallel  1:(A1, B1), 2:(A2, B2), 3:(A3, B3)


##  분류
Bit level Parallelism은 일단 고려하지 않음.
core도 지금은 고려할 수 없음.

latency per stage in instruction cycle는 어떤 명령을 처리하느냐에 따라 상이할 수 있지만 보통은 논의의 편의를 위해서 1 clock cycle로 고정되어 있다고 가정한다.

그리고 아래를 보면 알겠지만 instruction pipelining과 superscalar는 구분되는 개념이다. 그리고 superscalar는 무순서 실행과도 구분된다.

*   single   sequential EU
    *   subscalar processor
    *   CPI = summation of clock cycles per stage in instruction cycle
*   single   pipelined  EU
    *   scalar processor
    *   CPI =  latency of stage which has the longest clock cycles
    *   CPI = 1 if all latencies of stages are 1 clock cyle
*   multiple sequential EU
    *   superscalar
    *   CPI = number of EU / number of stages in instruction cycle
*   multiple pipelined  EU
    *   superscalar
    *   It is hard to calculate CPI for specific instruction but mostly CPI is under 1



*   out-of-order execution
*   register Renaming
*   speculative execution
*   brach prediction


*   VLIW
*   EPIC
*   Multithreading
    *   TMT: 여러 스레드에서 명령을 받아서 실행. Concurrency 개념
    *   SMT: Superscalar가 전제되어야 한다.  Parallelism 개념
*   Multi-core