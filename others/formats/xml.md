# XXML

##  타 표준과의 호환성
* 레거시 표준과의 호환이 아니면 쓸 이유가 없음
* XML과 JSON의 상호호환성을 만족하는 표준을 사용하는 것이 나음
  * XML이 JSON보다 훨씬 복잡하기 때문에, 보통 JSON에서 XML 데이터를 일관되게 표현하는 것이 핵심
  * BadgerFish, GData, JSON-LD 등이 있음
  * 단순 XML↔JSON 호환은 BadgerFish로 충분함.
  * XML↔JSON-LD 호환이 필요하다면 해당 데이터가 RDF 표준을 준수해야 함.
    * 거의 대부분의 레거시 표준들은 RDF 표준을 준수하지 않음

### 결론
* 각 XML 기반 표준들은 JSON 표현 양식이 있음
  * UBL: [UBL 2.3 JSON Alternative Representation Version 1.0](https://docs.oasis-open.org/ubl/UBL-2.3-JSON/v1.0/cn01/UBL-2.3-JSON-v1.0-cn01.html)
  * XBRL: [xbrl-json-CR-2021-07-07](https://www.xbrl.org/Specification/xbrl-json/CR-2021-07-07/xbrl-json-CR-2021-07-07.html)
* 하지만 이러한 json 표현 규정들은 가독성이 떨어진다.

##  참고
* YAML의 Anchor 기능은 JSON Pointer와 호환 가능
* GraphQL은 SDL(Schema Definition Language)라는 자체 언어 표준을 사용
  * JSON Schema와 호환은 가능
* JSON Schema를 full-support하는 NoSQL은 ArangoDB가 유일하며, 대부분의 검증은 어플리케이션 단에서 수행해야 함.
  * MongoDB의 스키마는 JSON Schema의 하위호환이며, JSON Schema로 검증하는 것 자체는 가능

##  번외: 마샬링(Marshalling) vs 직렬화(Serialization)
추후 정리 예정


##  지식
[출처](https://www.tcpschool.com/xml/xml_xslt_intro)

### XSL
1. XSLT : XSL Transformations를 의미하며, XML 문서를 다른 구조의 문서로 변환시키기 위한 언어입니다.
2. XPath : XML 문서의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어입니다.
3. XSL-FO : XML 데이터를 출력하기 위한 목적으로 설계된 언어입니다.
  * XSL-FO는 2012년에 발표된 2.0 버전을 마지막으로, 2013년부터는 더 이상의 업데이트를 진행하고 있지 않습니다. 따라서 현재는 CSS3로 대체하여 사용하고 있습니다.

### XSD
* DTD의 한계를 개선한 새로운 포맷