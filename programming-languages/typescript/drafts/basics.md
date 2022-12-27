#   Basics
*   reference: https://www.typescriptlang.org/docs/handbook/intro.html

##  Strictness tsconfig option
*   `compilerOptions/noImplicitAny`
*   `compilerOptions/strictNullCheck`
*   `compilerOptions/strictPropertyInitialization`

##  temp
*   generic programming, generic variable or wild card.
*   `{key} ?: {value}` syntax for optional property
*   `?.` optional chaining
*   `!.` Non-null Assertion Operator

*   union type `|`
*   intersection type `&`
*   literal type: literal value를 type으로 지정.
*   `never` type

*   `as` for type assertion (and also type conversion)
    *   정석적인 방법으로는 해결이 어려울 때, 다음과 같이 쓸 수 있음.
        *   `const a = (expr as any) as T;`
*   `type` for type alias
*   `void`
*   `unknown`: any랑 비슷하지만, unknown로 지정된 값은 참조될 수 없다.


##  interface vs type
reference: https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases
```ts
//  for interface
interface Animal {
  name: string
}

interface Bear extends Animal {
  honey: boolean
}

const bear = getBear() 
bear.name
bear.honey

//  for type
type Animal = {
  name: string
}

type Bear = Animal & { 
  honey: boolean 
}

const bear = getBear();
bear.name;
bear.honey;
```

##  narrowing
*   type narrowing (type guard)
    *   In TypeScript, checking against the value returned by `typeof` is a type guard.
*   `in` operator narrowing (property or element narrowing)
*   truthiness narrowing
*   equality narrowing
*   discriminated union 방법


##  function types
*   `void`
*   `object`
*   `unknown`
*   `never`

##  Object types
*   optional properties `?:`
*   readonly properties `readonly`
*   intersection types `&`
*   `Array`, `ReadonlyArray`, `Tuple`


##  Type manipulation
*   `keyof` type operator

##  Classes
*   `get`/`set` accessor (keyword)
*   member visibility
    *   `public`: allow access for all
    *   `prtotected`: allow access for subclass
    *   `privated`: allow access for only itself
        *   `Cross-instance private access`: typescript는 가능
            *   다른 인스턴스여도 같은 클래스끼리는 private member에 접근 가능
        *   When compiling to ES2021 or less, TypeScript will use WeakMaps in place of `#` for private class members.
    *   `static`

*   `this` issue

##  type compatiability
issue related with type variance(타입가변성)

structural (sub)typing vs Subtype polymorphism (or Nominal typing)

structural typing은 인정되는 범위의 측면에서 subtype polymorphism보다 관대한 방식이다. **member들의 type이 같으면 같은 type으로 취급하는 것.** 물론 sound한 typing system은 아니지만, javascript에서 anonymous object(function expression, object literal)를 자주 사용하는 관행을 뒷받침한다.

Function Parameter Bivariance 이슈가 있었지만, `compilerOptions/strictFunctionTypes`를 통해 해결되었다.

##  others
*   `unique symbol`
*   `satisfies` operator (>=4.9)
...