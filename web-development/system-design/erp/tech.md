# 설계

##  프론트엔드
* Deep Link
  * 웹과 모바일 일관성 강화
  * 모바일 내에서 컨텐츠 공유 시 웹 url 공유 가능
  * 또한 웹에서 앱으로 쉽게 전환하기 위한 기능

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
    * 상태관리도 이슈임.
  * 참고
    * https://toss.im/slash-23/session-detail/B1-3, https://www.youtube.com/watch?v=EuDOn7255gI
    * https://blog.toss.im/article/workflow-revolution, https://www.youtube.com/watch?v=5WBlhIl8KkY

* Funnel UI
  * 유저 플로우 상태 관리를 염두한 UI 설계
    * 이런 페이지들은 딥링크를 사용할 실익이 없지만, 다른 시스템과의 연동성(예: 리다이렉트 등)을 고려해야 한다.
  * Toss useFunnel 참고

* 기타
  * android: 인앱 업데이트

  ## 문서 관리
* 문제
  * 다양한 종류와 양식의 비즈니스 문서들을 RDBMS 테이블들의 마스터-디테일 사슬로 관리하기에는 유연성이 부족함.
  * XBRL은 스펙에 calculationlink가 있어서 검산기를 이용하면 수치 계산이 가능한데, 다른 표준들은 문서를 해석할 별도의 비즈니스 로직이 필요하다.
  * XBRL과 같은 XML 기반 문서들은 네임스페이스 기능을 통해 어트리뷰트 식별자의 충돌 방지를 넘어 문서 자체적으로 형식 검증까지 가능
  * 이러한 문서를 NoSQL에 저장할 때에는 그 확장성을 고려하여 동적 스키마(Dynamic Schema)를 정의해야 한다.

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



##  ~20240223

* 마케팅
* 프로덕트 (서비스)
* 시스템

##  마케팅과 프로덕트
* customer aquisition
  * 참고
    * https://acquiredentrepreneur.tistory.com/139
  * GTM(Go-To Market) Motion Flowchart
  * performance 마케팅
* customer retention
  * 참고
    * https://www.openads.co.kr/content/contentDetail?contsId=7575
  * CRM 마케팅
  * 단순히 고객 대상 프로모션뿐만 아니라, 활동이 미미한 유저들에게 끊임없이 서비스를 상기시키는 것도 포함.
    * 결국에는 기존 고객의 구매 전환 및 유지를 위함.

* PO 역할
* SRE(Site Reliability Enginner) vs DevOps
* CUJ(Critical User Journey) and SLO (Service Level Objective)
* SLI: Service Level Indicator
* SLA: Service Level Aggrement (보통 SaaS에서 주로 사용)

##  기능 목록 (Functionalities)
* Observability 관찰 가능성
  * monitor and analysis: not only real time
  * infrastructure and application: not only health check, but also business intensive
  * conclusion: 모니터링과 분석의 결합.
  * subfunctionalities: monitoring, log management, user journey tracking and analysis
    * 유저가 서비스 이용 중에 에러가 아니어도 운영진에 알람이 가게 할 수 있음.


프론트엔드 사용자 로그
백엔드 APIM

비즈니스 트랜잭션 추적
* APM: Application Performance Management
  * 모듈: apache prometheus vs sentry(유료) vs datadog(유료)
  * monitoring
  * log management (유료 서비스)
* BTM: Business Transaction Management
  * 프론트엔드 디버깅: Datadog Session Replay는 최강
    * 출처: https://steady-study.super.site/datadog-rum
  * 프론트엔드 트래킹: Amplitude
  * 모니터링: APM과 연동
  * 백엔드 트래킹: ??
  * 그래프 데이터베이스로 관리
  * https://brunch.co.kr/@jaechullee/2
    * Amplitude는 PO팀.
    * GA4는 마케팅팀.

* APM: Apache Prometheus vs Sentry
* BTM: Amplitude
* Marketing Analytics: GA4, ...


##  결론
Amplitude, Matomo, Sentry 등 대부분의 서비스들은 아래 기능들을 모두 지원한다.
따라서
* (에러) 모니터링: Apache Prometheus
* 분석
  * 시스템 레벨: Apache Prometheus
  * 서비스 레벨: GA4, 기타 마케팅 프레임워크

* Observability - more than monitoring
infrastructure monitoring or application performance monitoring
