#   kernel.org
*   https://www.kernel.org/doc/html/latest/core-api/index.html
*   https://www.kernel.org/doc/html/latest/
*   https://www.kernel.org/doc/html/latest/kernel-hacking/index.html

compendium of best practice: 모범 사례의 개요
낡은 것, 구식 등: cruft, jargon 등

tasklet and softirq vs workqueue: https://selfish-developer.com/entry/tasklet과-workqueue-12-차이점

#   코드로 알아보는 ARM 리눅스 커널
*   커널 버전: 4.6 (p xx)
    *   교재에서 제시한 소스코드 [출처](https://github.com/torvalds/linux/tree/4.6)는 2022년 7월 19일 기준 404를 반환한다.
    *   https://elixir.bootlin.com/linux/v4.6/source

##  ARMv8
ARMv8은 64bit 아키텍처이지만, 실행 상태(execution state)라는 개념을 통해 AArch64(64bit 실행 상태)와 AArch32(32bit 실행 상태)를 사용한다. 64bit와 32bit 모두 지원

### ARMv8의 익셉션 모델


##  부트로딩
리눅스 커널 v4.6의 arch/arm64에서 head.S는 `/arch/arm64/boot/`가 아니라 `/arch/arm64/kernel/`에 있다.

소스코드 [출처](https://elixir.bootlin.com/linux/v4.6/source/arch/arm64/kernel/head.S)

*   L212: stext 프로시저 시작 위치
*   L213: preserve_boot_args, 부트 파라미터 저장
*   L214: el2_setup, EL2 설정
*   L217: set_cpu_boot_mode_flag, CPU 부트 모드 저장
*   L218: __create_page_tables, 페이지 테이블 생성


리눅스 커널 v4.6 이후에는 KASLR이 도입되었다. KASLR은 Kernel 메모리 공간에서의 ASLR 기법을 일컫는다.
KASLR을 통해 커널도 PIE 바이너리를 생성할 수 있게 되었다.


#   리눅스 커널과 객체 지향 패턴
출처: https://lwn.net/Articles/444910/
출처: https://lwn.net/Articles/446317/
출처: https://matheustavares.gitlab.io/assets/oop_git_and_kernel.pdf


Method dispatch와 Data inheritance(inheritance by composition)

linux kernel 코드에서는 private inheritance를 superclass가 subclass를 멤버로 포함하는 방식으로 구현한다면, public inheritance를 subclass가 superclass를 멤버로 포함하는 방식으로 구현한다.

private superclass에서 subclass에 접근하려면 private superclass의 포인터에 대해 `ALIGN` 함수로 구한 offset을 더한 주소값으로 접근해야 한다.
반대로 public superclass에서 subclass에 접근하려면 public superclass의 포인터를 인자로 하여 `container_of` 함수로 구한 주소값을 통해 접근해야 한다.

`container_of`는 커널 자료구조에서도 사용되는 함수이다.

koject과 gobject에 반영된 객체지향 개념

##  kobject
출처: https://www.kernel.org/doc/html/latest/core-api/kobject.html

어떤 구조체가 kobject를 내제(embed)하고 있는 것은, 객체지향 관점에서 보면 [어떤 구조체가 kobject를 상속받는 것으로 해석할 수 있다.](https://www.kernel.org/doc/html/latest/core-api/kobject.html#embedding-kobjects)



#   김동현, 2020. 디버깅을 통해 배우는 리눅스 커널의 구조와 원리 1
*   커널 버전: 4.19 (p27)
*   라즈비안 버전: 2019-07-10-raspbian-buster-full

*   `task_struct` 구조체: 태스크 기술자(task descriptor)
    *   `thread_info` 구조체: 프로세스 스레드 정보

`task_struct`는 아키텍처 독립적이라면, `thread_info`는 아키텍처 종속적(또는 의존적)이다.
`thread_info`는 컨텍스트 스위칭에 따른 직전 cpu 상태(레지스터값 등)를 저장하는데, 아키텍처에 따라 레지스터의 개수, 이름, 크기 등이 상이하기 때문에 `thread_info`의 소스코드는 아키텍처 종속적이다.

*   `init_task` 전역 변수

##  getpid
`getpid`는 현재 프로세스(current process)의 tgid(thread group id)를 반환한다.

*   [pid_t getpid(void)](https://elixir.bootlin.com/linux/v4.19/source/kernel/sys.c#L880)
*   `sys_getpid` 핸들러는 SYSCALL_DEFINE0 매크로를 통해 생성되며, `unistd.h`의 `getpid`를 호출하면 `sys_getpid(current)` 핸들러가 호출된다.
*   [static inline pid_t task_tgrid_vnr(struct task_struct *tsk)](https://elixir.bootlin.com/linux/v4.19/source/include/linux/sched.h#L1292)
*   [pid_t __task_pid_nr_ns(struct task_struct *task, enum pid_type type, struct pid_namespace *ns)](https://elixir.bootlin.com/linux/v4.19/source/kernel/pid.c#L420)
*   [struct pid_namespace *task_active_pid_ns(struct task_struct *tsk)](https://elixir.bootlin.com/linux/v4.19/source/kernel/pid.c#L436)
    *   [static inline struct pid *task_pid(struct task_struct *task)](https://elixir.bootlin.com/linux/v4.19/source/include/linux/sched.h#L1212)
    *   `task_pid` 함수에서 `task->thread_pid`를 반환한다.
    *   [static inline struct pid_namespace *ns_of_pid(struct pid *pid)](https://elixir.bootlin.com/linux/v4.19/source/include/linux/pid.h#L128)
    *   `ns_of_pid` 함수에서 `pid->numbers[pid->level].ns`를 반환한다.
*   [pid_t pid_nr_ns(struct pid *pid, struct pid_namespace *ns)](https://elixir.bootlin.com/linux/v4.19/source/kernel/pid.c#L400)
*   `pid_nr_ns`에서 `&pid->numbers[ns->level]`를 반환.

##  ps
`ps -ely`
`ps -ejH`
`ps axjf`

##  _do_fork()
pp138-139
리눅스 커널에서는 프로세서 생성 속도 개선을 위해 리소스를 새로 할당하지 않고 부모 프로세스를 복제하여 부모 프로세스에 할당되어 있는 리소스를 물려주는 방식을 채택하였다.

출처: https://elixir.bootlin.com/linux/v4.19/source/kernel/fork.c#L2129

```cpp
/*
 *  Ok, this is the main fork-routine.
 *
 * It copies the process, and if successful kick-starts
 * it and waits for it to finish using the VM if required.
 */
long _do_fork(unsigned long clone_flags,
	      unsigned long stack_start,
	      unsigned long stack_size,
	      int __user *parent_tidptr,
	      int __user *child_tidptr,
	      unsigned long tls)
```

*   [clone_flgas](https://elixir.bootlin.com/linux/v4.19/source/include/uapi/linux/sched.h#L5)
*   `stack_start`: 유저 영역에서 스레드 생성 시 복사하려는 스택의 주소.
*   `parent_tidptr`: 부모 스레드 그룹을 관리하는 핸들러
*   `child_tidptr`: 부모 스레드 그룹을 관리하는 핸들러

`_do_fork`는 `copy_process`로 프로세스를 만든 후, `wake_up_new_task` 함수를 호출하여 프로세스를 `wake_up_new_task`를 깨운다(run queue에 해당 프로세스를 삽입한다. 즉 스케줄링 대상에 올린다는 뜻이다).

`copy_process`: pp187-189
`wake_up_new_task`: pp189-190

### copy_process()
출처: https://elixir.bootlin.com/linux/v4.19/source/kernel/fork.c#L1628
*   [dup_task_struct](https://elixir.bootlin.com/linux/v4.19/source/kernel/fork.c#L1707): task_struct 구조체와 프로세스가 실행될 스택 공간을 할당
*   [L1839-L1841](https://elixir.bootlin.com/linux/v4.19/source/kernel/fork.c#L1839): task_struct의 스케줄링 관련 정보 초기화
*   [L1849-L1888](https://elixir.bootlin.com/linux/v4.19/source/kernel/fork.c#L1854): 부모 프로세스의 프로세스 정보를 생성할 프로세스에 복사

### wake_up_new_task
출처: https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/core.c#L2394
*   [p->state = TASK_RUNNING](https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/core.c#L2400): 프로세스 상태를 `TASK_RUNNING`으로 변경
*   [L2411](https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/core.c#L2411): thread_info 구조체의 cpu 필드에 현재 실행 중인 [cpu 번호 저장](https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/sched.h#L1339)
*   [L2413-L2417](https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/core.c#L2413): 

### 프로세스 생성: user process fork
*   `fork`
*   `sys_clone`
*   `_do_fork`

### 프로세스 생성: kernel process fork
*   커널 스레드 생성 요청
*   `kthread_create`
*   `kthread_create_on_node`
*   `__kthread_create_on_node`
*   kthread에서 커널 프로세스 생성
*   `kthreadd`
*   `create_kthread`
*   `kernel_kthread`
*   `_do_fork`


##  do_exit()
출처: https://elixir.bootlin.com/linux/v4.19/source/kernel/exit.c#L765


```cpp
void __noreturn do_exit(long code)
```

`__noreturn` 지시자는 실행 후 자신을 호출한 함수로 되돌아가지 않는다고 컴파일러에게 지시한다.
```cpp
// https://elixir.bootlin.com/linux/v4.19/source/include/linux/compiler_types.h#L209
#define __noreturn		__attribute__((noreturn))
```

*   [do_task_dead](https://elixir.bootlin.com/linux/v4.19/source/kernel/exit.c#L924)
*   [schedule](https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/core.c#L3482)


### do_task_dead
*   출처: https://elixir.bootlin.com/linux/v4.19/source/kernel/sched/core.c#L3482

### 프로세스 종료: user process exit
*   `exit`
*   `sys_exit_group`
*   `do_group_exit`
*   `do_exit`

### 프로세스 생성: kernel process fork
*   `slow_work_pending`
*   `do_work_pending`
*   `do_signal`
*   `do_group_exit`
*   `do_exit`

##  task_struct

##  current 매크로
`task_struct`와 관련된 함수에서는 `current`를 마치 전역변수처럼 접근한다.
즉 함수 내부에서 `current`를 선언하지 않고도 `current` 변수에 접근할 수 있는 것이다.

`current_thread_info()->task`

실행 중인 프로세스 스택의 주소를 이용해 최상단 주소에 접근하여 `thread_info` 구조체의 `task` 필드의 주소를 반환하는 코드.


##  인터럽트
irq stands for interrupt request

인터럽트 컨텍스트에서 스케줄링을 하면, 안 그래도 인터럽트 핸들러가 인터럽트를 빨리 처리해야 하는데 휴면 상태에 돌입하면 시스템이 오동작할 수 있다(pp314-315).

커널에서 인터럽트를 처리하는 과정에 대한 간략한 기술:

1.  인터럽트 벡터(`__irq_svc`)를 실행하여 실행 중인 프로세스의 레지스터 세트를 프로세스 스택에 저장
2.  커널의 IRQ 서브시스템에서 관련 함수를 호출하다가 `__handle_irq_event_precpu()` 함수에서 인터럽트 디스크립터를 읽어서 인터럽트 핸들러 함수(ISR, Interrupt Service Routine이라고도 함)를 호출
3.  인터럽트 핸들러 함수가 이후에 해야할 일을 수행.

### 인터럽트 벡터
*   인터럽트 벡터의 종류
    *   `__irq_svc`: 커널 모드
    *   `__irq_usr`: 유저 모드

### 인터럽트 등록


### 인터럽트 디스크립터
`irq_desc` 구조체

인터럽트 종류별 발생 횟수는 `cat /proc/interrupts` 명령어로 확인 가능

## 인터럽트 후반부 처리
pp384-385 참고
*   IRQ 스레드
*   Soft IRQ: 각 Soft IRQ 서비스에 제한 시간(`MAX_SOFTIRQ_TIME`)이나 최대 재시작 횟수(`MAX_SOFTIRQ_RESTART`)를 설정하여 Soft IRQ 컨텍스트에서의 처리가 느려지면 `ksoftirqd` 스레드를 깨워 나머지를 처리하도록 하고 Soft IRQ 서비스는 종료.
*   tasklet: Soft IRQ를 디바이스 드라이버 레벨에서 쓸 수 있는 인터페이스
*   Work Qeuue

IRQ 스레드는 인터럽트 후반부 처리 로직에서 자체적으로 실행 시간이 길어질 때 조치하지 않는 이상 실행 시간이 길어져도 이를 제어할 방법이 없다. 또한 IRQ 스레드는 실시간 프로세스로 구동되므로 다른 일반 프로세스들이 선점을 할 수 없는데, 이때 인터럽트 후반부 처리 시간이 길어지면 다른 프로세스들이 모두 대기하게 되며 이는 시스템 전체 속도가 느려지게 되는 결과를 초래한다.

반면 Soft IRQ는 인터럽트 후반부 처리 시간이 길어지면 이를 `ksoftirqd` 커널 스레드에 넘긴다. `ksoftirqd`는 IRQ 스레드와 하는 역할이 같다. (사견: 교재에서는 `ksoftirqd`가 실시간 프로세스인지 여부가 나와있지 않는데 일반 프로세스라면 결과 반환 지연은 워크큐와 비슷할 것으로 추정한다.)

워크큐는 일반 프로세스로 프로세스 우선순위가 높지 않아 처리 시간은 긴데 결과를 빨리 반환할 필요가 없을 때 쓰면 좋을 것이다.

결국 인터럽트 빈도와 처리 시간은 반비례 관계가 되어야 한다. 인터럽트 빈도도 높고 처리 시간도 길면 결국 처리 결과 반환 시간을 포기해야 한다.

`atomic`: 커널에서는 스케줄링 하면 안 되는 컨텍스트 또는 선점 스케줄링이 되지 않는 실행 단위(어셈블리 명령어).

##  IRQ 스레드(threaded IRQ)
IRQ 스레드: 인터럽트 처리 전용 프로세스.
라즈비안에서는 IRQ 스레드가 1개이지만, 다른 리눅스 배포판에서는 IRQ가 2개 이상일 수 있다.

### IRQ 스레드 생성
IRQ 스레드는 부팅 과정에서 생성된 다음, 이후에 인터럽트 핸들러에서 IRQ 스레드를 깨우는 방식으로 IRQ 스레드가 동작한다.

*   `request_thread_irq`
    *   [prototype in header](https://elixir.bootlin.com/linux/v4.19/source/include/linux/interrupt.h#L139)
        *   `unsigned int irq`: 인터럽트 번호
        *   `irq_handler_t handler`: 인터럽트 핸들러의 주소
        *   `irq_handler_t thread_fn`: IRQ 스레드 처리 함수의 주소
        *   `unsigned long flags`: 인터럽트 핸들링 플래그
        *   `const char *name`: 인터럽트(를 발생시킨 디바이스) 이름
        *   `void *dev`: A cookie passed back to the handler function
    *   [function in source](https://elixir.bootlin.com/linux/v4.19/source/kernel/irq/manage.c#L1794)
        *   L1833-L1849: 인터럽트 디스크립터 설정. 인터럽트 디스크립터의 필드 중 `action` 구조체에서 IRQ 스레드 관련 정보를 저장.
        *   L1849: `__setup_irq` 함수로 IRQ 스레드 생성
*   `__setup_irq`
    *   [function in source](https://elixir.bootlin.com/linux/v4.19/source/kernel/irq/manage.c#L1181)
    *   L1233-L1242: `new->thread_fn`에 IRQ 스레드 처리 함수가 등록되었는지 그리고 nested의 값이 1(인터럽트 중에 난입한 인터럽트인지)인지 확인.
    *   L1234: `setup_irq_thread` 함수 실행
*   `setup_irq_thread`
    *   [function in source](https://elixir.bootlin.com/linux/v4.19/source/kernel/irq/manage.c#L1125)
    *   L1132-L1139: `kthread_create`로 커널 스레드 생성

리눅스 커널에서는 IRQ 스레드 처리 함수와 IRQ 스레드 핸들러 함수를 모두 IRQ 스레드 핸들로로 취급하지만, 이들의 역할은 서로 다르다.
스레드로 생성되는 `irq_thread`는 IRQ 스레드 핸들러이고, 이 IRQ 스레드 핸들러가 지정된 함수를 실행할 때 그 함수를 IRQ 스레드 처리 함수라고 부른다.

### IRQ 스레드 실행
p413


##  Soft IRQ
Soft IRQ 서비스는 Soft IRQ를 실행하는 단위이다.

### Soft IRQ 서비스 핸들러 등록
### Soft IRQ 서비스 요청
### Soft IRQ 서비스 처리
*   `__do_softirq()`

### ksoftirqd 스레드

##  기타
*   [RCU](https://www.kernel.org/doc/html/latest/RCU/whatisRCU.html)
*   [profs vs sysfs](https://unix.stackexchange.com/a/86614)