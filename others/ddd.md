#   DDD

*   trigger 정의
    *   actor
    *   command
    *   domain events
    *   external systems
    *   policy
*   Aggregate:  고유의 비즈니스 목적 수행을 위한 데이터 객체들의 집합
    *   RPO 규칙
        *   Root only
        *   Primary key 참조
        *   One to One

*   Bounded Context:  사용자, 프로세스, 정책/규정 등을 고유한 비즈니스 목적별로 그룹핑한 것

*   Context Map: Bounded Context간의 관계를 도식화 한 것

*   Repository
    *   ORM을 주로 사용

*   UseCase
    *   실무적으로는 db에 접근하는 로직(또는 시나리오)에 가까움.