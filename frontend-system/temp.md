#   Frontend Stack

##  Architecture
independent and framework agnostic

needs discuss about DDD, Dependency Injection

*   monorepo
    *   main package
    *   script package
    *   design system package
        *   ui components
        *   static data
    *   utility packages (libraries)

*   framework agnostic
    *   very hard for configuration dependency
    *   dependency injection
        *   older issues
            *   class inheritance vs dynamical allocation
        *   `signal feature` of `preact`
            *   `@preact/signals-react` for react integration
        *   `inversify`

### 설계에 대한 고민
React의 View Update 로직에서 Model로 class를 사용하는 것은 거의 안티 패턴에 가깝다. 하지만 시스템이 복잡해질수록 명세와 구현의 구분이 더욱 필요해지며 인터랙션이 복잡해질수록 반응형 프로그래밍은 더더욱 필요해진다. 전자는 OOP 중에서도 DI와 관련되어 있다.

DI와 reactive programming을 모두 만족하는 frontend framework로는 Angular 2를 꼽을 수 있다. 아직 제대로 알아보지는 않았지만 의존성 주입이 상속받은 클래스에 대해서도 적용되는지는 미지수이다(아마 될 것으로 예상한다). 그리고 reactive programming은 rxjs을 차용하여 구현하였다.

Svelte는 fully reactive하지만, DI가 제대로 되는지는 모르겠다. 비록 class와 interface를 사용하지 않더라도 개념적인 의미에 interface를 선언하고 이를 만족하는 구현체와 그 구현체를 interface를 의존하는 객체에 연결하는 configuration이 있어야 하는데, 예제 코드에는 그런 게 없고 단지 이를 매개하는 wrapper function만 있었다.

어찌되었든 간에 문제는 Angular와 Svelte 모두 개발자 풀이 적다는 것이다. 유지보수 관점, 즉 서비스 지속성 관점에서 Angular와 Svelte를 사용하는 것은 좋은 판단이 아니다.

React의 가장 큰 단점은 model과 view가 강하게 결합되어 있다는 것이다. 대부분의 웹 UI 라이브러리가 가지는 문제이긴 하지만 React는 특히 심하다. 적어도 Function Component가 "Functional Component"을 의도했다면 View Component는 stateless할 필요가 있다. 하지만 state는 반드시 Component 안에서 초기화되고 사용되어야 한다. 구문적으로 인스턴스의 속성값을 바꾸지 않고 데이터를 새로 갱신한다고 해서 Component가 stateless해지는 것이 아니다. 결국 Function Component는 Class Component의 문법적 변주에 불과하다.

React가 rerendering을 줄이기 위해 이런 설계를 채택했다고 변호할 수 있지만, jsx처럼 자체 문법을 사용하는 svelte가 fully reactive를 구현했다는 점에서 부정적인 평가를 피할 수 없다. 단지 React는 Svelte, SwiftUI, Jetpack Compose처럼 MVVM 패턴을 native syntax로 설계하기에는 너무 오래되었고 대중화되었을 뿐이다.

(여담으로 React의 Class Component가 View layer에서 진정으로 OOP를 달성하고자 했다면 적어도 Component를 직접 import하지 않고 Component Interface Type들을 import해서 DI를 할 것이다. 하지만 동적 타이핑을 지원하는 javascript에서는 DI를 하는 것보다 `Button` Component의 내용 자체를 바꿔버리는 게 훨씬 직관적이기 때문에 그렇게 할 필요가 없었을 것이다.)

그럼에도 React로 DI와 fully reactive를 달성하려면 `inversify`와 `preact signal`을 사용할 필요가 있다.

preact의 `signal()` api는 vue의 `ref()` api와 달리 deep comparision을 지원하지 않는다. 그 말인 즉 object를 인자로 받을 경우 `signal()`은 object의 속성 변화를 감지하지 못하지만 `ref()`는 감지한다는 것이다.

어쨌든 View와 Model을 분리해야 하는 이유는 시스템 가독성도 있지만 Model의 Data를 서버와 동기화할 때 필요하다. Model이 View에 강하게 연결되면 동기화 로직이 중복된다.

Client Server 구도에서 Server에 MVC 패턴을 적용하는데, 이를 다르게 볼 필요가 있다.
```
Client <-> Server <-> DB
User <-> Frontend <-> Backend <-> DB
```

Controller를 Component 별로 구분하고(user input이 component 단위로 이루어지기 때문이다), Service와 Repository(Backend 연동)를 적용할 수 있다고 볼 수 있다.
이때 Component는 View와 Controller로 구분. Controller가 Service를 호출하면 Service가 store를 업데이트 및 server와 동기화한다.


### 예시
Table, Column, Cell 예시를 들어보자. interaction을 구현하려면 Cell의 위치가 계속 바뀌어야 한다. 이 과정에서 rendering이 중복될 수 있다. View Layer에서는 바로 이 부분을 해결해야 한다. 즉 Table, Column, Cell 관련 Data의 구조대로 Component 구조에 반영해서는 안 된다.

예를 들어 한 Column에 있는 Cell을 다른 Column으로 옮기는 경우, 일반적인 View 구조에서는 두 Column을 전부 rendering해야 하지만, Cell Component를 2개씩 짝을 지어 놓을 경우에는 훨씬 적게 rendering할 수 있다. 물론 이 정도 구현은 오버엔지니어링이지만, 때론 필요할 수도 있다.

중요한 건 Model이 변할 때 View가 바뀔 수는 있어도 View가 변할 때 Model이 변해서는 안 된다. 하지만 이것인 인터랙션 설계에서는 힘든 경우가 많다. drag & drop 인터랙션 중에 임시로 cell의 위치가 바뀔 때 실제 model을 안 바꾸기는 상당히 힘들다. 이를 위해서는 pesudo model 같은 것이 필요하다.


### 현재의 결론
React를 선택하되 그 설계는 View와 Model, Service(비즈니스 로직)를 명확하게 분리한다.

fully reactive는 Service가 DDD를 따르는 경우에 필요하다. 즉 어떤 Domain 인스턴스의 필드 데이터가 변경되었을 때 이를 구독하는 View나 다른 Domain 인스턴스들이 업데이트되어야 한다.

하지만 fully reactive를 지원하지 않는다면 FLUX로 비즈니스 로직을 제어하되, FLUX 로직의 프론트엔드를 Service로 감쌀 필요가 있다.

Component: Controller(Dispatcher, Reducer), View, ViewModel(View에 종속적인 Model), Model. Model 변경 시에는 ViewModel도 변경해야 하지만 ViewModel 변경 시에는 별도의 Model update가 없는 이상 Model을 변경해서는 안 된다. ViewModel은 양방향 바인딩이다. React의 Component는 View와 ViewModel이 하나의 단위에 결합된 형태.

controller는 stateless해야 하며, model은 global해야 한다. 대신 controller만이 model에 접근할 수 있어야 한다.

##  Stack in 2018
*   javascript
*   node.js
*   npm
*   babel
*   webpack
*   react
*   CSS in JS(runtime)
*   redux or recoil

##  Stack in 2022
*   typescript
*   node.js (or bun.js later)
*   yarn berry
*   swc
*   vite (or parcel)
*   react (or svelte?)
*   CSS in JS(compile time or zero-time)
*   jotai or zustand

##  다른 고민
빌드 도구 또는 어플리케이션 라이브러리 선택을 위한 벤치마킹 인터페이스

중요한 것은 빌드 대상이 되는 소스 프로젝트를 최대한 바꾸지 않아야 한다는 것이다.

##  References
*   [차세대 빌드 도구 비교. 최호철, 2022.01.27](https://ui.toast.com/weekly-pick/ko_20220127)