# Enum

## Overview
타입스크립트의 열거형 타입은 `enum`과 `const enum`이 있습니다.
먼저 아래 예시 코드를 보시죠.

```ts
enum NUMBER_ENUM {
  ZERO,
  ONE,
}

enum STRING_ENUM {
  ZERO  = '0',
  ONE = '1',
}

const enum CONST_ENUM {
  ZERO,
  ONE,
}

console.log(NUMBER_ENUM.ZERO);
console.log(STRING_ENUM.ZERO);
console.log(CONST_ENUM.ZERO);
```

위 타입스크립트 코드의 컴파일 결과는 아래와 같습니다.
```js
"use strict";

var NUMBER_ENUM;
(function (NUMBER_ENUM) {
    NUMBER_ENUM[NUMBER_ENUM["ZERO"] = 0] = "ZERO";
    NUMBER_ENUM[NUMBER_ENUM["ONE"] = 1] = "ONE";
})(NUMBER_ENUM || (NUMBER_ENUM = {}));

var STRING_ENUM;
(function (STRING_ENUM) {
    STRING_ENUM["ZERO"] = "0";
    STRING_ENUM["ONE"] = "1";
})(STRING_ENUM || (STRING_ENUM = {}));

console.log(NUMBER_ENUM.ZERO);
console.log(STRING_ENUM.ZERO);
console.log(0 /* CONST_ENUM.ZERO */);
```

`enum`은 내부적으로 javascript obejct로 변환되는 반면, `const enum`은 참조되는 부분들에 모두 리터럴한 값들로 들어갑니다.

## Issues with `const enum`

### `isolatedModules` 플래그
이 설정을 활성화하면 tsc는 `const enum`로 선언된 enum도 `enum`과 동일한 방식으로 컴파일합니다.

아래의 예제 소스를 컴파일한다고 가정해봅시다.
```js
// module.ts
export const enum CONST_ENUM {
  ZERO,
  ONE,
}

// main.ts
import { CONST_ENUM } from "./module";

console.log(CONST_ENUM.ZERO);
```

#### `isolatedModules=false`의 경우 컴파일 결과

`isolatedModules` 플래그를 활성화했을 때의 컴파일 결과는 아래와 같습니다.

```js
// module.js
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });

// main.js
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
console.log(1 /* CONST_ENUM.ONE */);
```

#### `isolatedModules=true`의 경우 컴파일 결과

`isolatedModules` 플래그를 활성화하지 않았을 때의 컴파일 결과는 아래와 같습니다.

```js
// modue.js
Object.defineProperty(exports, "__esModule", { value: true });
exports.CONST_ENUM = void 0;
var CONST_ENUM;
(function (CONST_ENUM) {
    CONST_ENUM[CONST_ENUM["ZERO"] = 0] = "ZERO";
    CONST_ENUM[CONST_ENUM["ONE"] = 1] = "ONE";
})(CONST_ENUM = exports.CONST_ENUM || (exports.CONST_ENUM = {}));

// main.js
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const module_1 = require("./module");
console.log(module_1.CONST_ENUM.ONE);
```

### `--preserveConstEnums`
`isolatedModules` 플래그를 활성화하면 `preserveConstEnums` 플래그도 활성화됩니다.

이 플래그를 활성화하면 tsc는 `const enum`로 선언된 enum도 `enum`과 동일한 방식으로 컴파일합니다.
이때 `isolatedModules` 플래그를 활성화했을 때 `preserveConstEnums` 플래그를 비활성화할 수 없습니다.

위와 동일한 예제 소스를 `isolatedModules=false`이면서 `preserveConstEnums=true`로 컴파일하면 다음과 같은 결과가 나옵니다.

```js
// modue.js
Object.defineProperty(exports, "__esModule", { value: true });
exports.CONST_ENUM = void 0;
var CONST_ENUM;
(function (CONST_ENUM) {
    CONST_ENUM[CONST_ENUM["ZERO"] = 0] = "ZERO";
    CONST_ENUM[CONST_ENUM["ONE"] = 1] = "ONE";
})(CONST_ENUM = exports.CONST_ENUM || (exports.CONST_ENUM = {}));

// main.js
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
console.log(1 /* CONST_ENUM.ONE */);
```

### 소결
`isolatedModules` 플래그는 파일 단위로 트랜스파일을 진행할 때 필요한 옵션입니다.
babel과 tsc를 같이 사용할 때 필요한 옵션이라고 알고 있는데 이에 대해서는 자세한 조사가 필요할 것 같습니다.

하지만 `const enum`은 `preserveConstEnums` 플래그와 무관하게 후술할 enum iteration을 지원하지 않습니다.
구현 자체는 가능할 지 모르지만

## Enum Iteration
enum의 멤버 타입이 숫자라면, `for ... in ...`으로 순회할 때 enum의 멤버 변수명까지 순회하게 됩니다.
이는 tsc가 어떻게 `enum`을 컴파일하는지 보면 알 수 있습니다.

```ts
export enum NUMBER_ENUM {
  ZERO,
  ONE,
}

for (const value in NUMBER_ENUM) {
  console.log(value);
}
/* output
0
1
ZERO
ONE
 */
```

## Union Type, Constant Object
라인 블로그에 따르면 enum을 사용하는 대신에 다음과 같은 방안을 제시한다.

```ts
const NUMBER_ENUM = {
  zero: 0,
  one: 1,
} as const;

type NUMBER_ENUM = typeof NUMBER_ENUM[keyof typeof NUMBER_ENUM];
```

##  결론
typescript에서 enum이 불완전하게 지원되는 것이 아쉽다.

굳이 enum에서 성능 향상을 도모하기 보다는 좀 더 가독성 좋고 편리하게 사용할 수 있는 방법으로 사용하는 것이 졸을 것이다.

### Reference
1. [Wikipedia, Enumerated Type](https://en.wikipedia.org/wiki/Enumerated_type)
2. [Line Engineering Blog](https://engineering.linecorp.com/ko/blog/typescript-enum-tree-shaking)
3. [Typescript Handbook](https://www.typescriptlang.org/docs/handbook/enums)
4. [Typescript Doc](https://www.typescriptlang.org/tsconfig#preserveConstEnums)
