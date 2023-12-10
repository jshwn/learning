# JPA Configuration

## Use mysql-connector-j from spring boot>=2.7.1
[출처1](https://luvstudy.tistory.com/221)
[출처2](https://stackoverflow.com/a/76351449)

##  @Transactional Propagation
* `@Transactional(propagation = Propagation.REQUIRED)`
  * default level
  * 부모 트랜잭션 내에서 실행하며, 부모 트랜잭션이 없을 경우 새로운 트랜잭션 생성

* `@Transactional(propagation = Propagation.NESTED)`
  * DB가 SAVEPOINT 기능을 지원해야 사용이 가능(Oracle)하다.

##  Reference
[트랜잭션 전파레벨](https://n1tjrgns.tistory.com/266)
[Transaction Propagation :: Spring Framework](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-propagation.html)

