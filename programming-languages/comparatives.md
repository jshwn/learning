#   Comparative Features in Major Programming Languages

##  언어 목록
*   python
*   javascript(typescript)
*   swift
*   kotlin
*   java
*   dart

##  Typing

### Dynamic Typing
dynamic typing이란 타입 검사를 컴파일 타임이 아니라 런타임에 수행하는 것을 말한다.
즉 변수에 숫자를 할당했다가 문자를 할당해도 각 시점마다 자료형에 맞는 연산만 수행된다면 문제가 없다.

javascript에서는 변수 선언을 제약하는 기능을 제공한다.
```javascript
a = 1;      // Declare as global varialbe
var a = 1;  // redeclarable and reallocatable; var hoisting issue

// let, cont keyword >= ES6
let a = 1;  // unredeclarable but reallocatable
const a = 1;// unredeclarable, unreallocatable but modifiable of properties for object data types
```

전역 변수와 var 변수는 다음과 같은 차이가 있다.
```javascript
console.log(a)  // undefined
var a="Hello"
```
```javascript
console.log(a)  // ReferenceError
a="Hello"
```

python은 변수를 재선언 및 재할당하는 데에 아무 제약이 없다.
```python
from typing import Final # (>=3.8)
a=1
# or
a:int = 1 # type hint (>=3.5)
a:Final[int] = 2 # 에디터에서 경고만 출력할 뿐 정상 실행된다.
```

### Static Typing
c와 c++은 설명을 생략한다.
```cpp
int a = 1;
```

java에서 `final`은 상수 선언 역할도 하지만 클래스나 메서드 앞에 오면 하위 자녀가 해당 클래스나 메서드를 상속 또는 오버라이드하지 못하도록 막는 기능도 한다.
```java
public Int a
public final Int b;
```

swift5에서는 변수 선언 시에 타입 명시를 생략할 수 있을 뿐, 다른 타입을 재할당할 수 없다.
```swift
var a = 1;  // unredeclarable but reallocatable
let b = 1;  // unredeclarable, unreallocatable but modifiable of properties for collection types
```

kotlin에서는 `val`과 `const`가 있다. `val`은 runtime에 상수를 할당하고 `const val`은 compile time에 상수를 할당한다.
```kotlin
var a: Int = 1; // var stands for variable
val b: Int = 2; // val stands for valuable
```

dart의 상수 키워드에는 `final`과 `const`가 있다. `final`은 런타임에 상수 할당을 체크하고 `const`는 컴파일 타임에 상수 할당을 체크한다.
두 상수 키워드 모두 사용할 때 변수 선언과 변수 초기화(값 할당)가 동시에 이루어져야 한다.
컴파일 타임에 정확한 값을 알 수 있으면 `const`를, 그러지 않으면 `final`을 사용해야 한다.
```dart
final Datetime now = new DateTime.now();    // 가능
const Datetime now = new DateTime.now();    // 불가능
```

dart에서는 `late`라는 키워드(>=2.12)도 있는데 

##  SubTyping

### Type Variance
*   Covariance 공변성
*   Convariance 반공변성
*   Invariance 무공변성
*   Bivariance 양공변성

##  Type Conversion
형변환에는 묵시적(implicit) 형변환과 명시적(explicit) 형변환이 있다. 이때 명시적 형변환은 보통 type casting이라고 한다. 묵시적 형변환은 수학 연산 중 정수와 부동소수점수 사이의 연산을 가능하게 하기 위해 이루어진다. 이 단락에서는 이러한 형변환을 제외한 모든 형변환 이슈를 다룬다.

java 역시 c/c++과 같이 primitive data types에 대해서는 type casting이 가능하다.

### C/C++, Java
c/c++에서 타입 캐스팅은 자료형의 포인터에 대해서 자주 이루어진다.
```c
int a = 100;
double b = (double) a;
```

### Dart & Swift
dart와 swift5 모두 `as`를 명시적인 형변환 키워드로 사용한다.
dart와 swift5 모두 업캐스팅(upcasting)은 묵시적으로 이루어진다.

swfit5는 여기에 더해 `as?`와 `as!` 키워드도 사용한다.
만약 다운캐스팅에 실패하면 `as?`는 `nil`을 반환하며, `as!`는 에러를 발생시킨다.

### Java Autoboxing & Unboxing
Java에는 특별하게 원시 자료형과 그 자료형에 해당하는 wrapper 클래스 간의 암묵적인 형변환이 존재한다.


### Type Casting for OOP
대부분의 언어에서는 클래스를 자료형으로 취급한다. 즉 자료형을 구현하기 하기 위한 기능으로 클래스를 사용한다는 것이다.
모든 언어가 클래스로 자료형을 구현하지는 않는다. javascript는 여전히 Prototype으로 자료형을 구현한다.

이는 OOP의 리스코프 치환 원칙 (LSP, Liskov Substitution Principle)과 연관된 이슈이다.

##  Statements

### conditional expressions

### loop expressions
*   `for(index = startValue; #termination condition#; increment expression)`
*   `for element in collection`
    *   python, swift, javascript
*   `while (#condition#) {}`
*   `do {} while (#condition#) {}`


##  Expressions

### others
*   삼항연산자 Tenary Operator
    *   `True if expr else False` for python
    *   `expr ? true : false ` for others

*    바다코끼리 연산자 Walrus Operator `:=` (>=Python 3.8)
    *   표현식과 동시에 변수 선언
    *   반드시 괄호로 묶어야 한다.
```python
x = 1, 2  # x에 (1, 2)를 대입
(x := 1, 2)  # x에 1을 대입
```

*   comprehension in python
    1.  LC, List Comprehension
    2.  SC, Set  Comprehension
    3.  DC, Dict Comprehension
    4.  GE, Generator Expression

+   python의 unpacking은 javascript의 spread syntax와 destructuring 기능을 모두 수행할 수 있다.

*   javascript spread syntax (>=ES5)
```javascript
arr1 = [1,2,3]
arr2 = [...arr1, 4, 5] // [1,2,3,4,5]

dict1 = {b: 2, c: 3}
dict2 = {a:1, ...dict1, d:4}
```

*   javascript destructuring (>=ES6)
```javascript
const [a, b, c] = [1,2,3]
// or
const {a, b, c} = {a: 1, b:2, c:3}
```

*   packing, unpacking in python
    *   가변 길이 컬렉션
    *   packing은 주로 함수의 가변 인자를 구현하지만, unpacking은 다양한 곳에 응용될 수 있다.
```python
def func(arg1, arg2, *args, **kwargs):
    arg3, arg4 = args   # (0, 1)
    arg5, arg6 = kwargs # {'arg5': 0, 'arg6': 1}

func(-1, -1, 0, 1, arg5=0, arg6=1)

a, b = [0, 1]
#   a=0, b=1
```

###  Optional Chaining and Nullish Coalescing
동적 타이핑 언어에서는 그 자체로 Optional type을 지원한다고 볼 수 있다.

javascript는 null coalescing operator 등장 전에도 파이썬처럼 OR 연산자로 null coalesing과 비슷한 기능을 사용할 수 있었다.
```javascript
a?.b    // optional chaining (>=ES2020)
a || b  // returns b when right value is falsy value
a ?? b  // nullish coalescing (>=ES2020)
        // returns b when right value is undefined or false
```

파이썬은 OR 연산자를 통한 nullish coalescing은 지원하지만 optional chaining을 지원하지 않는다.
파이썬 역시 javascript와 마찬가지로 OR 연산자를 통한 coalescing은 falsy value에 대해서 동작한다.
```python
a = None or  1   # 1
b = False or 1   # 1
c = 0     or 1   # 1
```

Java에서는 Nullish Coalescing을 아직도 지원하지 않는다. 그래서 Nullish Coalescing 기능을 Stream API 등을 이용하여 구현해야 한다. 물론 Optional Chaining도 literal syntax로 지원하지 않는다.
```java
//  Java Optional (>=Java 8)
//  NullPointerException를 줄이기 위해 도입된 기능
Optional<T> optional = Optional.empty();
optional.isPresent();   // false

Optional<T> optional = Optional.ofNullable(a);
T data = optional.ofElse("something for fallback"); // Nullish Coalescing
```

kotlin에서는 Optional type을 `nullable type`, optional chaining을 safe call이라고 부르며, nullish coalescing 연산자 `?:`를 elvis 연산자라고 한다.
```kotlin
val x = a?.b;
val x = null ?: "value";
```

swift에서는 optional type, optional chaining, nil coalescing을 모두 지원하지만 OR 연산자를 통한 coalescing은 지원하지 않는다.
```swift
//  Swift
var a:int? = nil; // Optional Type
a?.b    //  Optional Chaining
a = nil ?? 1      // Nil Coalescing
print( nil || a)  // Error!
```

sql에는 coalesce 함수가 존재한다.
```sql
--Nullish Coalescing in SQL
COALESCE(expr1, expr2, ...);
```

### String Formatting and String Interpolation
*   javascript
    1.  String.format()
    2.  template literal
```javascript
const name = "Tom";
const age = 20;

stmt = "{0} is {1} years old".format(name, year);
stmt = "{name} is {age} years old".format(name=name, age=age);
stmt = `${name} is ${age} years old`;
```

*   python
    1.  %-formatting
    2.  Str.format()
    3.  f-string

```python
name="Tom"
age=20

stmt = "%s is %d years old" % (name, age) 
stmt = "{0} is {1} years old".format(name, age)
f'{name} is {age} years old'
```

*   java
    1.  MessageFormat class (%-string)
    2.  StringBuilder class
    3.  formatted() (>=Java 15)

```java
String name = "Tom";
Int age = 20;

String stmt = String.format("%2$s is %1$d years old", age, name);
String stmt = new StringBuilder(name).append(" is ").append(age).append(" years old").toString();
String stmt = "%s is $d years old".formatted(name, age)
```

*   swift
    1.  Format specifier
    2.  String Interpolation

```swift
let name = "Tom";
let age  = 20;

// // 에러
// let stmt = String(format: "%s is %d years old", name, age )
let stmt = "\(name) is \(age) years old"
```



##  Functional Programming
*   기본 개요
    *   유명 함수
    *   익명 함수
    *   람다 함수
    *   Function as first class citizen

### Java
*   람다

*   함수형 인터페이스 Functional Interface (>=Java 8)
    *   Predicate, Consumer, Supplier, `Function<T, R>`, Comparator, Runnable, Callable 등
    *   java.util.function의 인터페이스: `IntFunction<R>`, `BinaryOperator<T>`
```java
@FunctionalInterface
interface CustomInterface<T> {
    // abstract method 오직 하나
    T myCall();

    // default method는 존재해도 상관없음
    default void printDefault() {
        System.out.println("Hello Default");
    }

    // static method는 존재해도 상관없음
    static void printStatic() {
        System.out.println("Hello Static");
    }
}

CustomInterface lambda = () -> "customer";
System.out.println(lambda.myCall()); // customer
```

*   Stream (외부적으로는 function pipelining, 내부적으로는 currying)
    +   Java 7 Fork/Join Model for thread implementation



##  Object Orient Programming


### dart
*   dart 생성자
    *   생성자, generative constructor
    *   기본 생성자
    *   유명 생성자
    *   리다이렉팅 생성자
    *   상수 생성자
    *   팩토리 생성자
    *   initializing formal parameter

### Prototype(Javascript)
생략