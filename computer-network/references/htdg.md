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
    *   확인응답 패킷은 크기가 작아서 다른 패킷에 편승(piggyback)시키는 방법으로 요청 수를 줄인다.
*   TCP slow start
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
