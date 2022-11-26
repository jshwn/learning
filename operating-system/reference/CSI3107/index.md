#   시스템프로그래밍

##  Linux Task

### Process vs Thread
이론적인 차원에서 Process Model과 Thread Model은 Process Context(stack, registers 등)와 Process Image(code, data)의 결합 유무로 구분할 수 있다.

Process는 context와 image가 모두 결합된 인스턴스이고, Thread는 context만 존재하고 스레드가 동작해야할 로직들은 process image에서 가져오는 인스턴스라고 볼 수 있다.

스레드를 사용하는 이유는 자원 공유와 병렬성에 이점이 있기 때문이다. 프로세스 간 자원 공유는 꽤 어려운 문제인데 스레드들은 같은 프로세스 메모리 공간에서 별도의 overhead 없이 자원을 공유할 수 있다. 그리고 프로세스는 (적어도 개념적으로는) 병렬화가 불가능하다. 하나의 인스턴스가 하나의 로직만을 동작시키기 때문이다. 하지만 프로세스에서 여러 개의 스레드를 만들면 같은 로직을 동시에 실행시킬 수가 있다.

### task_struct
리눅스는 process와 thread 모두 task로 취급한다. 각각에 해당하는 PCB와 TCB가 있지 않고 모두 `struct task_strcut`으로 구현된다. 다만 

### User Mode & Kernel Mode
kernel mode로 진입할 때 user mode에서의 context(cpu register 등)을 저장할 필요가 있다. 

### Identifying current task
현재 user process에서 커널 모드로 진입한 다음 커널 스택 아래에 저장되어 있는 `thread_info`를 참조한다.


### Context Switch
