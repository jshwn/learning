# Frontend System

##  Overview
프론트엔드란 무엇인가?

프론트엔드는 사용자와 상호작용하는 시스템이라고 정의할 수 있다.

그런데 기술적으로 우리는 웹 프론트엔드와 모바일 프론트엔드를 구분한다.

직무 관점에서는 웹 프론트엔드 개발자와 iOS,안드로이드 개발자로 구분한다.

하지만 전략관점에서 프론트엔드는 결국 웹, 모바일, 필요하다면 다른 디바이스 시스템도 다루어야 한다.

그 이유는 통합된 고객 경험 제공도 있지만, 그보다 근본적으로는 어떤 디바이스에도 대응을 할 수 있어야 하기 때문이다.

### 통일된 경험

예를 들어 고객이 앱에서 어떤 포스트를 누군가에게 공유하고 싶다고 하자. 

그런데 공유받는 사람에게 그 앱이 저장되어 있지 않다고 하자.

만약 모바일 앱만 개발했다면 공유받는 사람에게 이 포스트를 띄울 방법이 없다.

마케팅 전략 관점에서 공유가 불가능하다는 것은 대단히 크리티컬한 이슈다.

1차 고객을 모바일 앱 사용자로 한정할 수는 있겠지만, 2차 고객까지 그렇게 한정된다면 답이 없다.

### 기술적인 이슈
대부분의 개발 강의들은 웹과 모바일의 통합 대응을 전제하지 않기 때문에 기본적인 

모바일 앱 안에 

* 개발 방식
  * 모바일 웹
    * 기존 PC 웹을 모바일에 최적화된 화면으로 운영
  * 웹앱
    * 모바일 웹과 기술적으로는 동일(독립된 웹브라우저에서 실행)
    * 모바일 웹과 달리 네이티브 앱과 같은 사용성 제공이 목표
    * 단 웹에서 동작하기 때문에 네이티브 기능이 제한됨
  * 네이티브앱
  * 하이브리드앱
    * 네이티브 웹뷰
      * 주요 컨텐츠 페이지 제공은 웹뷰로 하며, 메뉴바나 카메라 촬영 등은 네이티브 앱으로 구현
      * 웹뷰 브라우저와 네이티브 앱 간의 명령 전송을 위해 브릿지를 사용
    * PWA
      * iOS 지원이 제한된다.


### 결론
브랜딩을 위해서는 웹이든 모바일이든 통일된 경험을 제공할 수 있어야 한다.

브랜딩 전략에는 단순히 디자인 시스템을 통해서 디자인 일관성을 관리하는 것도 포함되지만,

고객의 서비스 가치 여정에 중에 장애물을 없애는 것도 중요하다.

##  Reference
* 링크 관련
  * [딥링크 실전에서 잘 사용하는 방법 by 토스페이먼츠](https://blog.tossbusiness.com/articles/dev-10)
  * [모바일 앱 딥링크 완전 정복 가이드](https://www.adjust.com/ko/blog/dive-into-deeplinking/)
* 모바일 공유 관련
  * [Web Share API 사용하기](https://ui.toast.com/weekly-pick/ko_20190618)
  * [Navigator.share](https://developer.mozilla.org/ko/docs/Web/API/Navigator/share)