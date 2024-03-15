# Spring Java 개발

##  고려사항

### 일반
* openapi (swagger)
* logger
* security (csrf, xss, jwt, session 등)
  * 인증은 별도
* mysql jpa
  * crud
* deploy
* batch

### 심화
* 대용량, MSA
  * parallel transaction
  * timeout configuration

* 모니터링
  * Spring Boot Actuator, Prometheus, Grafana, Thanos

### 의존성
* Spring 기본
  * Logger (slf4j)
  * Filter, Interceptor
  * Testing
* Lombok
* Validation
* Spring Boot Debvtools
* Docker Compose Support
* Spring Web
* Spring Security
* Spring Boot Actuator
