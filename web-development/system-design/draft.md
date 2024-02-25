# System Design

##  프론트엔드
* Server Driven DST
  * Server Driven: 서버에서 요청 별로 화면 디자인 정의를 내려줌.
    * 권한에 따른 버튼이나 메뉴 표시 제어 가능
    * 이용자별 화면 A/B 테스트가 매우 용이해짐
  * DST: Design Syntax Tree
    * 플랫폼 간 UI/UX 일관성 극대화 가능
    * 디자이너-프론트엔드 개발자 간 의사소통 비용 절감
  * 고려사항
    * Server Driven DST를 사용한다면, A/B 테스트를 위해 React Native나 Flutter를 사용할 필요가 없다.
    * 다만 데이터를 prefetch하지 않는 이상, 페이지 이동 시 성능 문제가 발생할 수 있다.
    * 기존보다 서버 트래픽 비용이 증가한다.
      * 초기에는 전통적인 방식으로 개발하되, Server Driven으로 마이그레이션할 수 있도록 미리 대비할 필요
    * DST에 어느 정도까지 자율성을 부여할 지는 고민해봐야 한다.
      * 너무 많은 자율성(스타일링까지)을 부여하면 네트워크 지연 부담과 일관성 문제가 부각됨.
      * 너무 적은 자율성(데이터만)을 부여하면 A/B 테스트를 하는 것이 어려워짐.
  * 참고
    * https://toss.im/slash-23/session-detail/B1-3, https://www.youtube.com/watch?v=EuDOn7255gI
    * https://blog.toss.im/article/workflow-revolution, https://www.youtube.com/watch?v=5WBlhIl8KkY

* Funnel UI
  * 유저 플로우 상태 관리를 염두한 UI 설계
    * 이런 페이지들은 딥링크를 사용할 실익이 없지만, 다른 시스템과의 연동성(예: 리다이렉트 등)을 고려해야 한다.
  * Toss useFunnel 참고

##  서비스 통합
* Integration
  * MCI: Multi Channel Interface, 내부 연계(채널계 <-> 계정계)
  * FEP: Front End Processor, 외부 연계(계정계 <->외부)
  * EAI: Enterprise Architecture Integration, 외부 연계(계정계 <-> ERP)
* 참고
  * https://velog.io/@linked2ev/%EA%B8%88%EC%9C%B5IT-MCI-EAI-ESB

##  DevOps, SRE
* Scalability Functionality
  * Load Balancing
  * Service Discovery: Spring Cloud - Eureka Server
  * Docker Compose, k8s, podman, ...
  * 개념
    * SPOF: Single Point Of Failure

* Observability Functionality
  * 참고
    * https://medium.com/@dudwls96/opentelemetry-grafana-loki-tempo-prometheus%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-spring-boot-observability-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0-f977df45bb70
  * OpenTelemetry API (Java Dependent)
    * Spring Boot Actuator가 기본으로 지원(https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.observability.opentelemetry)
  * Trace
    * collector: Automatic instrumentation (with Java)
    * datasource: Grafana Tempo
  * Metric
    * collector: Micrometer (JVM dependent)
    * datasource: Prometheus(+ Thanos) vs OpenSearch (vs Graphite는 죽음)
  * Log
    * collector: Logstash vs Automatic instrumentation (with Java)
    * datasource: Elasticsearch vs Loki vs OpenSearch
  * Visualization: Grafana
  * ELK vs PLG는 옛말?
  * 프론트엔드 성능 측정 및 분석: lighthouse user flow API

* 기타
  * SPOF: Single Point Of Failure
  * Auditing
    * JPA Data Envers: 이력 테이블까지 관리
    * 비즈니스 이력

##  보안
* 보안 자동화
* 업무 보안을 위한 Zero Trust
  * IAM: Identity Access Management
    * SSO: SSL, SAML 등
    * RBAC & ABAC
    * Policy
    * Security
  * SASE: Secure Access Service Edge
  * ZTNA: Zero Trust Network Access
    * VPN과 달리 어플리케이션 서비스 단위로 관리
  * UEM: Unified Endpoint Management
    * Device Management
    * Asset Management
    * Application Management
  * EPP: Endpoint Protection Platform




# ~20240205

IT 서비스는 항상 운영, 예측 가능성, 확장 가능성 염두하고 설계해야 한다.

시스템은 Entity, State, Action(또는 Operation)으로 구성된다.

* 시스템 디자인 설계 목표
  * 운영: 운영이 편해야 한다.
  * 예측 가능성
    * 다양한 의미로 해석 가능한데, 여기서는 **"비즈니스 수준에서"** 시스템이 예측한 대로 동작하여 오류가 없는 것을 말한다.
    * 즉, 시스템에 정의된 Action들은 모두 닫혀 있어야 한다(closed)
  * 통계: 운영과 비슷한 맥락인데, 통계 자료를 산출하기 편해야 한다.

##  설계 구상
### Entity
* 구조
  * 종류: tree 관계(Composition), 집합 관계, 순서 관계, 연관 관계
  * type (엔티티 분류)

### State
* 연산

### Action
* 하나의 비즈니스 로직(예: 결재 승인, 회원 탈퇴 등)에 대하여 생각해볼 수 있는 지점
  * bulk action (집단 실행)
    * 관리자가 어떠한 사유로 수십 명의 회원을 탈퇴시키는 경우, 단체로 회원을 탈퇴시킬 수 있는 기능이 없다면 일일이 회원탈퇴 버튼을 눌러야 할 것이다.
    * 따라서 복수의 비즈니스 로직 실행을 한 번에 할 수 있어야 한다.
  * concurrent action (동시 실행)
    * 물리적으로 동시 실행이 아니라 비즈니스 수준에서 동시로 기록할 필요가 있는 경우
    * 예를 들어 두 행의 정보를 서로 교차 변경시키는 경우, UPDATE를 각각에 대하여 2번 해야 하지만 변경 시점이 같도록 할 필요가 있으면 동시 실행으로 처리할 필요가 있다.
    * 대표적인 예시가 바로 **연초의 대규모 조직 개편과 인사 발령**이다.
  * idempotent action (멱등 실행)
    * 연산을 여러번 실행해도 상태가 같은 것
    * 참고: https://developer.mozilla.org/ko/docs/Glossary/Idempotent
  * invertible action (역 실행)
    * 임의의 action a의 실행으로 변경된 entity의 status를 a 실행 이전으로 돌리는 것
    * a(s) = a * s = s'이라면, invertible action은 a^(-1)(s') = s' * a^(-1) = s
    * invertible action이 로그까지 날리는지는 정하기에 따라 다르다(git log를 생각하면 쉽다).
      * 최악의 경우에는 상태 변경 순서까지 revert 또는 수정해야 할 수 있다.
      * 예를 들어 결재 순서가 모종의 이유로 잘못된 경우, 그리고 다른 시스템이 그 결재 순서에 의존하고 있는 경우에는 결재 순서를 수정하여 의존 시스템에 동기화시켜야 할 필요가 있을 수 있다.
      * 이런 경우에는 상태 자체를 entity화 시킬 필요가 있으며, 수정해서
    * **결론**
      * 비즈니스 로직에서 상태의 순서가 중요할 경우에는, 상태들의 순서 구조 그 자체를 연산의 대상으로 할 필요가 있다.
      * 비정상적인 데이터 비일관성 이슈에 대비하여

##  백오피스 시스템 공통 도메인
* 유저
  * 가입(생성), 탈퇴(삭제 or soft delete)
* 조직
  * 놀랍게도, 필요에 따라 포함관계뿐만 아니라 연관관계도 가능해야 한다.
  * 결국 하나의 표에 띄우려면, 같은 entity여야 한다. (아니면 union해야 하니까)
  * 연관 관계인 조직이 있는 경우에도 비정규화를 할 수 있는지는 의문
* 역할 vs 권한 (or both)
* 결재
* 결재와 권한의 경우, 보통 조직 안에서만 가능해야 하지만 **협업**하는 경우에는 서로의 데이터를 확인하기 위해서는 결재자 지정 대상이나 권한을 공유할 필요가 있다.
  * 이 경우에는 프로젝트, task force 등의 일종의 연관관계 조직을 만들어서 매핑할 수 있을 것이다.
  * **아예 복수의 조직 자체가 하나로 합쳐지거나, 갈라지는 것도 생각해볼 수 있다.**
