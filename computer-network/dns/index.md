# DNS
참고: https://xn--3e0bx5euxnjje69i70af08bea817g.xn--3e0b707e/jsp/resources/dns/dnsInfo.jsp
참고: https://docs.aws.amazon.com/ko_kr/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-domain-registration

##  개요
Domain Name System.

도메인에 부합하는 ip를 찾기 위해 최상위 도메인 zone부터 차례로 네임 서버를 조회하는 것이 바로 Recurvise Query.
`nslookup` 명령어로 어떤 도메인이 어떤 네임서버에 어떤 레코드를 가지고 있는지 확인 가능하다.

도메인 요청 참고: http://www.ktword.co.kr/test/view/view.php?m_temp1=2251&id=434

##  Domain Namespace


##  최상위 도메인 (TLD, Top Level Domain)
* gTLD: 일반 최상위 도메인(.com, .org 등)
* ccTLD: 국가코드 최상위 도메인(.kr, .jp 등)
* 최상위 도메인 이름 목록: https://data.iana.org/TLD/tlds-alpha-by-domain.txt

##  도메인 등록 과정
* 최종 사용자: end user
* 도메인 이름 등록 대행자: domain name registrar
* 도메인 이름 레지스트리: domain name registry
  * 중앙 레지스트리(central registry)라고도 불린다.
  * 목록: https://www.icann.org/resources/pages/listing-2012-02-25-en

최종 사용자가 어떤 도메인 이름을 사용하고 싶으면 도메인 이름 등록 대행자를 통해 도메인의 소유권을 등록해야 한다.
이때 해당 도메인 이름의 등록을 중개한 도메인 이름 등록 대행자는 지정 대행자(designated registrar)가 된다.
이후로는 지정 대행자만이 도메인 이름 레지스트리 데이터베이스에서 도메인 이름에 관한 정보를 수정 또는 삭제할 수 있다.
이때 최종 사용자는 지정 대행자를 도메인 이전(주로 '기관 이전'이라고 한다)을 통해 변경할 수 있다.

예를 들어 com 도메인을 지정 대행자가 등록할 때, 해당 도메인의 레지스트리인 VeriSign에 수수료를 납부하고 등록을 요청한다.

##  DNSSEC
후기: https://dev.dwer.kr/2020/03/bind9-dnssec.html
