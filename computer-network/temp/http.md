#   HTTP
HTTP stands for HyperText Transfer Protocol.

##  milestone verions
*   1991, HTTP/0.9 [doc](https://www.w3.org/Protocols/HTTP/AsImplemented.html)
*   1996, HTTP/1.0 [rfc1945](https://www.ietf.org/rfc/rfc1945.html)
*   1999, HTTP/1.1 [rfc2616](https://www.ietf.org/rfc/rfc2616.html)
*   2015, HTTP/2.0 [rfc7540](https://www.ietf.org/rfc/rfc7540.html) [Github](https://http2.github.io/)
*   2022, HTTP/3.0 [rfc9114](https://www.ietf.org/rfc/rfc2616.html)

MIME stands for Multipurpose Internet Mail Extensions.
MIME는 SMTP 등 이메일 프로토콜에서 사용할 목적으로 제안되었지만, 이후 HTTP에서도 채택되었다.

##  HTTP feature

### stateless
HTTP is  generic, stateless, protocol.

다만 HTTP에서 session cookie를 사용할 수 있다는 점에서 HTTP로도 stateful server를 구현하는 데에는 문제가 없다.
즉, HTTP가 stateful protocol이냐 아니냐는 논의의 실익이 없다.

##  HTTP Message
*   Request - Inbound, Downstream
*   Response - Outbound, Upstream

##  HTTP data exchange

##  HTTP Connection Models
[HTTP/1.x의 커넥션 관리 - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x)