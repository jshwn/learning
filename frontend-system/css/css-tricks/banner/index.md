# Banner
여기서 다루는 배넌 흔히 말하는 이미지 배경에 광고 카피 문장이 새겨진 광고 배너를 떠올리면 된다.

배너를 퍼블리싱하는 일은 생각보다 간단하면서도 어렵다.

만약 아무 제약 사항이 없다면 다음과 같이 부모 element에 background-image로 사진을 넣어주면 된다.

```html
<div class="banner">
  <span>Lorem ipsum</span>
</div>
```

```css
.banner {
  background-image: url('...');
}
```

##  Issue with background-image: url()
하지만 `background-image`을 사용하여 배경 이미지를 넣는 데에는 치명적인 제약이 뒤따른다.

바로 프론트엔드 프레임워크에서 최적화된 이미지의 url을 넣는 것이 매우 까다롭다는 점이다.

로컬 이미지의 캐싱된 파일 주소는 CSS-in-JS 프레임워크를 사용한다면, CSR과 SSR과 관계없이 import할 수는 있다.

하지만 캐싱과 이미지 최적화까지 같이 고려한다면 이야기가 달라진다.

대부분의 이미지 최적화는 다음 Next.js의 예시처럼 소스코드 단에서 특정 Image 컴포넌트를 사용해서 이루어진다.

```jsx
import Image from 'next/image'
import img from 'local image path'

<Image
  src={img.src}
  // ...
>
```

이론적으로야 컴포넌트에서 최적화된 이미지의 경로를 동적으로 찾아서 넣어주는 기능을 개발할 수도 있겠지만, 빠른 시간에 구현을 해야 하는 개발자 입장에서 플러그인을 새로 개발할 수는 없는 노릇이었다.

즉, react 생태계에서 이미지의 캐싱, 최적화, `background-image: url()`을 사용한 이미지 삽입을 모두 만족시키는 것은 이 글을 쓰는 시점에서는 불가능하다.

##  Layering absolute img
두 번쨰 방법은 고전적인 방법이다.
하지만 `position: absolute`에 대한 정확한 이해가 없으면 이를 응용하기가 어렵다.

이는 여러 이미지 레이어를 중첩시킬 수 있다는 점과 img 태그를 사용하여 semantic html을 준수한다는 점에서 `background-image`보다 나은 방법이라고 할 수 있다.

[참고](https://stackoverflow.com/questions/48173958/place-absolute-div-under-relative-div)