#   20221123

Javascript를 처음 배울 때 synchronous/asynchronous, blocking/non-blocking을 공부한 적이 있다.

이때는 blocking이 그저 코드가 작업을 모두 수행할 때까지 기다리는 것, non-blocking은 그렇지 않는 것 정도로 이해하고 있었다.

하지만 이 수업에서 blocking은 context switch를 의미했다. 예를 들어 blocking lock이란 lock을 사용하는 프로세스가 당장 lock을 획득할 수 없다면 일단 재우고 lock을 획득할 때까지 해당 프로세스를 꺠우지 않는 것이다.