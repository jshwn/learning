#   kernel.org
*   https://www.kernel.org/doc/html/latest/core-api/index.html
*   https://www.kernel.org/doc/html/latest/
*   https://www.kernel.org/doc/html/latest/kernel-hacking/index.html

compendium of best practice: 모범 사례의 개요
낡은 것, 구식 등: cruft, jargon 등

tasklet and softirq vs workqueue: https://selfish-developer.com/entry/tasklet과-workqueue-12-차이점



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

*   `handle_level_irq()`
*   `handle_irq_event()`
*   `__handle_irq_event_percpu()`
*   `dwc_otg_common_irq()`

인터럽트 컨텍스트에서 스케줄링을 하면, 안 그래도 인터럽트 핸들러가 인터럽트를 빨리 처리해야 하는데 휴면 상태에 돌입하면 시스템이 오동작할 수 있다(pp314-315).

### 인터럽트 벡터
*   `__irq_svc`: 커널 모드
*   `__irq_usr`: 유저 모드

### 인터럽트 디스크립터
`irq_desc` 구조체

인터럽트 종류별 발생 횟수는 `cat /proc/interrupts` 명령어로 확인 가능

## 인터럽트 후반부 처리
*   IRQ 스레드
*   Soft IRQ
*   tasklet: Soft IRQ를 디바이스 드라이버 레벨에서 쓸 수 있는 인터페이스
*   Work Qeuue

`atomic`: 커널에서는 스케줄링 하면 안 되는 컨텍스트 또는 선점 스케줄링이 되지 않는 실행 단위(어셈블리 명령어).

##  기타
*   [RCU](https://www.kernel.org/doc/html/latest/RCU/whatisRCU.html)
*   [profs vs sysfs](https://unix.stackexchange.com/a/86614)