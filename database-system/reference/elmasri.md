#   Chpater 3
*   ER model: Entity-Relation Model

*   데이터베이스 설게 과정
    1.  요구사항 수집 및 분석
    2.  개념적 설계(conceptual design), 개념 스키마
    3.  데이터베이스 구현

##  3.1 엔티티 타입, 엔티티 집합, 애트리뷰트, 키

### 3.3.1 entity and attribute
*   simple attribute vs composite attribute
    *   simple attribute: 더 이상 나눌 수 없는 attribute
    *   composite attribute: 더 작은 attribute로 나눌 수 있는 attribute
*   single valued attribute vs multivalued attribute
*   stored vs derived
*   null values
*   complex attribute

### 3.3.2 entity type, entity set, key, value set
*   entity type: 동일한 attribute들을 갖는 entity들의 set
*   entity set: 동일한 entity type의 entity들의 set

entity type과 entity set은 서로 결부되는 개념

*   key: entity set에서 각 entity마다 서로 다른 값을 가지는 attribute

p64
키 제약 조건은 두 개 이상의 엔티티가 동시에 키 애트리뷰트에 대해 동일한 값을 가질 수 없음을 의미한다. 이 제약 조건은 특정 엔티티 집합에서만 만족되는 성질이 아니라 특정 시점에 엔티티 타입의 어떠한 엔티티 집합에 대해서도 만족되어야 하는 제약 조건이다.

*   domain: value set of attribute

##  3.4 관계, 관계 타입, 역할, 구조적 제약 조건
relationship: ER 모델에서의 엔티티 집합 간의 (수학적) 관계

여기서 관계(또는 관계 타입)는 entity set들의 수학적 관계(relation)라고 생각하면 된다.

그리고 관계의 각 원소들을 관계 인스턴스(relationship instance)들이라고 한다.

*   role name: 관계에서 entity가 가지는 이름
    *   예를 들어 상사-부하 관계의 경우, 실질적인 엔티티들은 모두 EMPLOYEE 엔티티 집합에 포함되지만 상사-부하 관계에서는 서로 이름을 달리 해야 한다.

구조적 제약 조건
*   카디날리티 비율
    *   이진 관계의 경우, 1:1, 1:N, N:1, M:N이 가능하다. 
    *   이 중 1:1이 가장 강한 제약이다.
*   참여 제약
    *   최소 카디날리티 조건: 엔티티가 참여할 수 있는 관계 인스턴스의 최소 수를 제약
    *   전체 참여(존재 종속성): 모든 entity가 적어도 하나의 관계 인스턴스에 참여할 것을 강제
    *   부분 참여: 전체 참여가 아닌 경우

관계 타입의 애트리뷰트

##  3.5 약한 엔티티 타입
키 애트리뷰트가 없는 엔티티 타입을 약한 엔티티 타입,
키 애트리뷰트가 있는 엔티티 타입을 정규 엔티티 타입 또는 강한 엔티티 타입이라고 한다.

식별 엔티티 타입 또는 소유 엔티티 타입와 식별 관계(identifying relationship).

p75: 약한 엔티티는 소유 엔티티 없이는 식별될 수 없기 때문에, 약한 엔티티 타입은 식별 관계에 대해 항상 전체 참여 제약 조건(존재 종속성)을 가진다. (그러나 그 역은 성립하지 않음)

#   Chapter 4
8장에서 Relation Model과 ER Model의 관련성을 다룸.

데이터베이스 이론에서 relationship이 엔티티와 엔티티 사이의(또는 엔티티 집합 간) 관계를 말한다면, relation은 엔티티 집합(테이블)을 의미한다.

**p107: 키는 슈퍼키이지만, 슈퍼키는 키가 아닐 수 있다.**
사견: 슈퍼키는 애트리뷰트의 튜플도 될 수 있다. 예를 들어 회원정보 relation의 id 열(애트리뷰트)은 키이면서 슈퍼키이다. 하지만 id와 name으로 조합된 튜플은 키가 될 수 없지만 슈퍼키가 된다. 이때 키는 특정 애트리튜브에 대해서만 가능하다.

### 4.2.4
*   엔티티 무결성 제약 조건: 어떠한 기본키 값도 널 값이 될 수 없다
*   참조 무결성 제약 조건
    *   외래키



#   Chapter 5
*   관계 데이터 모델의 용어와 SQL의 용어 대응
    *   relation    : table
    *   tuple       : row
    *   attribute   : column