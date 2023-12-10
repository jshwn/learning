# Spring Security

##  인증 Authentication
* HTTP 인증 종류. [HTTP Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication)
  * Basic (Base64 인코딩 기반)
    * 무조건 ssl/tls가 보장되는 연결 환경에서만 사용해야 한다.
  * Bearer (OAuth 2.0에 사용)
    * 사용자가 해석할 수 없도록 충분히 복잡하게 만들 수 있어야 한다.
  * Digest
  * HOBA
  * ...

### 세션 인증
Basic Authentication과 Session Authentication을 혼동하면 안 된다.

전자는 클라이언트가 서버에 인증 정보를 안전하게 전달하는 일종의 약속이고,
후자는 서버가 인증 정보를 관리하는 방법이다.

* Spring Session vs HttpSession (from Servlet API, Tomcat) vs Spring Security Session

[Mysql을 Spring Session Storage로 사용하는 방법](https://junhyunny.github.io/information/spring-boot/spring-session/)

[참고](https://stackoverflow.com/questions/27437159/difference-of-spring-session-management-and-spring-security-session)

### JWT and Spring Security OAuth
* 참고: JWT vs Opaque
  * JWT와 Opaque는 편의성과 보안성의 trade off 관계라고 할 수 있다.
  * JWT는 내부적으로 유저 정보를 저장할 수 있어서 해독 시 정보 침해 가능성이 존재한다.

JWT: Json Web Token. JWT Standard를 따르는 토큰 양식이다.


OAuth 모델

```
Figure 2: Refreshing an Expired Access Token

+--------+                                           +---------------+
|        |--(1)------- Authorization Grant --------->|               |
|        |                                           |               |
|        |<-(2)----------- Access Token -------------|               |
|        |               & Refresh Token             |               |
|        |                                           |               |
|        |                            +----------+   |               |
|        |--(3)---- Access Token ---->|          |   |               |
|        |                            |          |   |               |
|        |<-(4)- Protected Resource --| Resource |   | Authorization |
| Client |                            |  Server  |   |     Server    |
|        |--(5)---- Access Token ---->|          |   |               |
|        |                            |          |   |               |
|        |<-(6)- Invalid Token Error -|          |   |               |
|        |                            +----------+   |               |
|        |                                           |               |
|        |--(7)----------- Refresh Token ----------->|               |
|        |                                           |               |
|        |<-(8)----------- Access Token -------------|               |
+--------+           & Optional Refresh Token        +---------------+
```

[OAuth의 과거, 현재, 미래](https://junuuu.tistory.com/703)
[Spring 기반 OAuth 2.1 Authorization Server 개발 찍먹해보기](https://tech.kakaopay.com/post/spring-oauth2-authorization-server-practice/)
[강의](https://www.inflearn.com/course/%EC%8B%A4%EC%8A%B5-oauth-%EB%B3%B4%EC%95%88-%ED%95%B4%ED%82%B9)