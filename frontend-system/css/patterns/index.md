# CSS Patterns

##  Layout
* [Sticky Footer](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Sticky_footers)
  * 본문 내용이 없어도 푸터가 맨 하단에 붙어 있게 하는 패턴
  * 기존에 `grid-template-rows: auto 1fr auto;`를 이용한 방법은 본문과 푸터 사이에 화소 단위 간격이 발생하고 있음.
    * 향후 이미지 자료 첨부 예정
  * `flex`를 이용한 방법도 동일한 현상이 간헐적으로 발생하는 것을 확인함.
    * `flex`를 이용하는 방법은 크게 두 가지임.
      1. [`flex-shrink`와 `flex-grow`를 사용하는 방법.](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Sticky_footers#alternate_method)
      2. footer에 `margin-top: auto`를 주기.
    * `flex`를 샤용하는 경우에는 위의 두 방법 모두 `flex-direction: column`도 같이 사용하는데, 이때는 viewport의 width에 따른 word break가 발생하지 않음.
      * 따라서 사용을 지양해야 함.
    
  * 다만 화면 비율에 따라 이 현상이 재현되지 않는 경우도 있어서 cssom의 계산량이 많을 때 기기 환경에 따라 렌더링 버그가 나타나는 것으로 추측함.
  * `position: absolute`를 이용한 방법으로 footer를 본문과 약간 중첩시켜서 간격이 벌어질 가능성을 원천 차단할 수 있음.
    * 하지만 footer의 height이 content에 의존적일 경우(fit-content), footer의 계산된 height을 완충 div에 반영해주어야 한다.
  
  * 썩 내키는 방법은 아니지만, 2가지 방법을 생각했고 그 중 후자를 선택함.
    1. layout에 main과 footer와 동일한 배경색을 적용하고, 각 layout component들에 background-color를 다시 정의하는 방법
      * 암묵적으로 css cascading을 사용하는 게 아니라, 직접 모든 element에 background-color를 명시하는 방법
      * css preprocessor 같이 별도의 css 파일 컴파일러를 만드는 게 아니라면 매우 번거로운 작업이 될 뿐더러, 투입 대비 효용 측면에서 컴파일러 개발은 비효율적임.
      * 단, 성능 측면에서는 향후 확장성을 고려하더라도 큰 영향은 없을 것으로 추측되나, 가급적이면 css property를 추가하지 않는 게 더 나음.
    2.  main과 footer 사이에 absolute element를 덧대기
      * 임시방편이기는 하지만 `grid-template-rows: auto 1fr auto;` 방법을 유지하려면 이 방법밖에 없음.
  
  * 참고: https://css-tricks.com/couple-takes-sticky-footer/

* [Flexible column layout](https://experience.sap.com/fiori-design-web/flexible-column-layout)