# Business Design

##  개요
* 이력 관리 (history)
* 운영/관리에 용이한 설계 (백오피스)
* 통계 조회 용이함.

##  설계
* service_task
* business_task

### 사용자 및 비즈니스 관계 분석
* 논의
  * 플랫폼이 아니더라도, 추후 플랫폼으로 성장할 가능성을 염두해야 한다.
  * 따라서 partner로 본사, 그리고 본사 직원들에게 admin이 아니라 partner employee 계정을 부여해야 한다.
* 분류
  * entity: user, partner
  * type: consumer, supplier, admin, system
  