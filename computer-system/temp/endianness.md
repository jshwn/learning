#   Endianness
참고할만한 출처
https://jhnyang.tistory.com/172
https://jhnyang.tistory.com/226

endiannes는 int와 float의 문제이다.

어떤 endianness를 채택하느지의 문제는 꽤 중요하다.

##  Hardware implications of endianness
출처: https://www.embedded.com/the-hardware-and-software-implications-of-endianness/

system bus와 transaction 개념
출처: https://heo-seongil.tistory.com/82

반도체 IP block: 지식 재산권이 되는 논리, 셀, 집적 회로 레이아웃 등등

bus: 시스템 내외부 모듈 사이에 데이터 전송을 위한 공유되는 통신 규약
bus의 사양(spec)은 일반적으로 다음의 계층으로 이루어진다.
*   트랜잭션 프로토콜
*   타이밍/신호 규격
*   전선의 묶음
*   전기적 규격
*   물리적/기계적 규격

transaction: Master(주로 CPU)가 Slave(주로 Memory)에 명령을 하고 Slave가 이에 응답하는 하나의 과정

bus width: 버스의 물리적 규격 - 32bit, 64bit, 128bit 등등
transaction width: transaction 1번 당 transferred된 size of data
CPU(또는 IP block)는 같은 bus에 대해서 다른 transaction size를 사용할 수 있다.