#   TypeORM
실무에서 외래키를 사용하지 않는 이유: https://co1nam.tistory.com/44

##  Entity
*   Entity
    *   Embedded Entity (implements composite attribute)
    *   Entity Inheritance
        *   Join, 조인 전략
        *   Single Table Inheritance, 단일 테이블 전략
        *   Subtype Table (비추천)
    *   Tree Entity
    *   View Entity (View)

##  Relations
*   N+1 problem
    *   join을 통한 해결
    *   eager relation: relation 관계의 entity들을 모두 포함 (성능 이슈가 발생할 가능성이 있음)
    *   lazy relation: 참조되는 column에 접근할 때 데이터를 가져온다.

##  Entity Attribute Decorators
*   `@OneToOne`
*   `@OneToMany`

##  QueryBuilder
*   `where('{table}.{column} = :arg', {` arg `})`