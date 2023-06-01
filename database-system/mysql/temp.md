#   Mysql

##  꿀팁 및 기타
*   mysql STRAIGHT_JOIN
*   mysql community 버전에서는 스레드 풀을 지원하지 않는다.

##  아키텍처
* Mysql Engine
  * SQL Optimizer
* Storage Engine
  * Adaptive Hash Table (Only for InnoDB)
  * buffer(in memory)와 disk의 동기화
  * Transaction Isolation (Lock Level)
    * READ UNCOMMITED
    * READ COMMITED
    * REPEATABLE REAT
    * SERIALIZE
  * MVCC, Multi-Version Concurrent Control
    * Consistent Nonlocking Read: Lock을 사용하지 않고 일관된 데이터를 보장.
      * 여러 로우를 업데이트하는 중에 해당 로우를 조회한다면 어떤 로우는 갱신된 값이고 어떤 로우는 이전 값이기 때문에 일관성 문제가 발생할 수 있다.
      * Lock을 사용하면 이를 피할 수 있으나, 업데이트가 끝날 때까지 조회가 안 되기 때문에 성능 문제가 발생한다.
      * 따라서 성능 개선을 위해 Lock을 사용하지 않으면서도 일관된 읽기를 지원할 필요가 있다.
    * InnoDB는 Undo Log를 사용하여 이를 지원
    * 격리 수준에 따라 동작이 달라진다.
  * Deadlock Detection
  * Buffer pool
    * MySQL 5.7부터 Buffer pool의 크기를 설정할 수 있으며, 동적으로 확장도 가능하다. 다만 중요한 설정이므로 DB를 내리고 작업해야 한다.
    * 버퍼 풀의 크기가 커질수록 조회 성능만 증가한다.
    * Redo Log의 크기가 커야 조작 성능이 증가한다.

##  실습
* sql문 실행계획 출력: `EXPLAIN|DESCRIBE|DESC FORMAT=Table|JSON|TREE <SQL STATEMENT>;`
* 스레드 동작 확인: `SELECT thread_id, name, type, processlist_user, processlist_host FROM performance_schema.threads ORDER BY type, thread_id;`
* 설치된 Mysql 컴포넌트 조회: `SELECT * FROM mysql.component;`
* `SHOW ENGINES;`, `SHOW PLUGINS;`
* `SHOW GLOBAL VARIABLES LIKE 'innodb_adaptive_hash_index';`
* `SHOW ENGINE InnoDB STATUS`
