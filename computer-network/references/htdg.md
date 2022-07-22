#   HTTP 완벽 가이드

##  p31 URL 스킴

```
<scheme>://<username>:<password>@<host>:<port>/<path>;<parameter>?<query>#<fragment>
```

*   `<scheme>`: 사용하는 프로토콜(http, ftp, stmp 등)
*   `<host>`: 일반적으로 서버의 도메인 네임이 해당하지만, 본질적으로는 IP 주소이다.
*   `<port>`: 명시하지 않으면 HTTP 또는 HTTPS 기본 포트인 80 또는 443을 사용한다.
*   `<username>`이나 `<password>`는 FTP에서 사용한다.
*   `<path>`: unix file system의 file path와 같은 형식이다. 물론 glob pattern은 사용할 수 없다.
*   `<query>`
*   `<fragment>`

##  p50
*   [inbound/outbound](https://www.ietf.org/rfc/rfc2616.html#page-12)
*   [upstream/downstream](https://www.ietf.org/rfc/rfc2616.html#page-11)

##  pp90-98
소켓 API를 사용하면, TCP 종단(endpoint) 데이터 구조를 생성하고, 원격 서버의 TCP 종단에 그 종단 데이터 구조를 연결하여 데이터 스트림을 읽고 쓸 수 있다.

데이터가 작을수록 TCP 연결 시간이 전체 통신 시간에서 차지하는 비중이 커진다. 따라서 HTTP에서는 TCP 연결을 최소화하기 위해 TCP 커넥션을 유지하는 방법을 사용한다.
*   확인응답 지연
    *   확인응답 패킷은 크기가 작은 데이터들을 다른 패킷에 편승(piggyback)시키는 방법으로 요청 수를 줄인다.
*   TCP slow start
    *   처음 TCP Connection을 생성할 때는 전송 속도를 제한하다가 데이터 전송이 성공할 때마다 속도 제한을 점점 완화하는 방법.
    *   외부 링크: 혼잡 제어(Congestion Control)의 한 방법이다.
        *   [출처](https://evan-moon.github.io/2019/11/26/tcp-congestion-control/#slow-start)
*   네이글(Nagle) 알고리즘과 TCP_NODELAY
    *   여러 개의 TCP 데이터를 일정 크기를 넘을 때까지 모아서 전송하는 방법.
    *   네이글 알고리즘은 RFC896에 기술되어 있다.
    *   확인응답 지연과 같이 쓰게 되면 확인응답 패킷 전송이 매우 늦어지게 되는 부작용이 있다.
*   TIME_WAIT의 누적과 포트 고갈

##  p101  HTTP Connection 성능 향상 방법
1.  병렬(parallel) 커넥션
2.  지속(persistent) 커넥션
3.  파이프라인(pipelined) 커넥션
4.  다중(multiplexed) 커넥션

##  pp102-103 병렬 커넥션
병렬 커넥션이 순차 커넥션보다 항상 속도가 빠르지는 않다.

클라이언트의 네트워크 대역폭이 좁으면 데이터를 내려받는 속도 자체가 느려서 순차 커넥션보다 성능 상의 이점이 없다.
그리고 서버의 경우, 너무 많은 커넥션을 연결하게 되면 부하가 커져서 성능이 떨어진다.
그래서 브라우저 단에서 병렬 커넥션의 수를 제한하며 서버 역시 커넥션의 수에 제한을 둔다. 

##  pp104-113 지속 커넥션
사이트 지역성(site locality): 하나의 사이트에서 요청하는 자원들이 대부분 해당 사이트를 호스팅하는 서버에 있는 것.

사견: 튜닝된 커넥션(tuned connection)은 TCP tuning 주제.

지속 커넥션은 병렬 커넥션과 함께 사용될 때에 가장 효과적이다.

### HTTP/1.0+의 Keep-Alive 커넥션
p106: Keep-Alive 동작
*   HTTP 요청과 응답에 Connection:Keep-Alive 헤더를 추가
*   요청과 응답 헤더에 해당 헤더가 없으면 커넥션을 끊음

pp106-107: Keep-Alive 옵션
*   홉별 헤더 hop-by-hop header: 오직 1개의 전송 링크에만 적용되며, 다음 서버로 전달되면 안 되는헤더


pp108-112: Keep-Alive and dumb proxy 멍청한 프록시
Keep-Alive 헤더는 홉별 헤더인데, 클라이언트로부터 요청을 받은 프록시 서버가 멍청한 프록시여서 이를 이해하지 못하고 그대로 웹서버에 전달하면 웹 서버는 프락시가 커넥션을 유지하자고 요청하는 것으로 오인하게 된다.
웹 서버는 프락시 서버와의 커넥션을 끊지 않고 데이터를 프록시 서버에 반환한다. 프록시 서버는 클라이언트에게 데이터를 반환하면서 동시에 커넥션이 끊어지기를 기다린다.
프록시 서버가 클라이언트에게 데이터를 반환하면 클라이언트는 Keep-Alive 상태인 줄 알고 다음 요청을 보낸다.
하지만 프록시 서버는 같은 커넥션으로 또다른 요청이 오는 것을 예상하지 못하기 때문에 이 요청은 무시된다.
프록시 서버로부터 응답이 없으니 브라우저는 타임아웃이 나올 때까지 대기만 하게 된다.

### HTTP/1.1의 지속 커넥션
HTTP/1.1에서는 Connection:Keep-Alive 헤더를 사용하지 않는다.

HTTP/1.1에서는 지속 커넥션이 기본이다.
HTTP/1.1에서 커넥션을 끊으려면 Connection:close 헤더를 추가해야 한다.

##  파이프라인 커넥션
HTTP/1.1은 지속 커넥션을 통해서 요청을 파이프라이닝할 수 있다.
