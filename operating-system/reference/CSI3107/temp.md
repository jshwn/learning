#   20221123

Javascript를 처음 배울 때 synchronous/asynchronous, blocking/non-blocking을 공부한 적이 있다.

이때는 blocking이 그저 코드가 작업을 모두 수행할 때까지 기다리는 것, non-blocking은 그렇지 않는 것 정도로 이해하고 있었다.

하지만 이 수업에서 blocking은 context switch를 의미했다. 예를 들어 blocking lock이란 lock을 사용하는 프로세스가 당장 lock을 획득할 수 없다면 일단 재우고 lock을 획득할 때까지 해당 프로세스를 깨우지 않는 것이다.


#   20211224
OSTEP stands for Operating System: Three Easy Pieces

Virtualization, Concurrency, Persistency (+ Security)

vdso: virtual dynamic shared object

*   In a single processor
    *   Instruction Level Parallelism
    *   Data Level Parallelism
*   Task Level Parallelism
*   Distributed Computing


컨테이너 오케스트레이션 (Container Orchestration)

LXC, LXD

`chroot`, `namespace`, `cgroups`, `capabilities`, `union mount`

process 1, kernel threads.

##  process
batch system
concurrent system
interactive system
parallel system


강학상 개념, 이론상 개념
설계상 개념, 구현상 개념

*   linux task
    *   lifecycle
        *   creation
            *   `execve`
            *   `clone`, `fork` system call은 모두 `kernel_clone` 기반: https://elixir.bootlin.com/linux/v5.15/source/kernel/fork.c#L2543
                *   cloning flag: https://elixir.bootlin.com/linux/v5.15/source/include/uapi/linux/sched.h
            *   `posix_spwan`
        *   context switch
        *   exit
        +   states
    *   metadata
        *   about identification: `pid`, `tgid`
        *   for concurrency: `thread group`