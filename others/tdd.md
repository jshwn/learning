#   Test Driven Development
TDD:BE. 켄트 벡 저, 김창준·강규영 역. 테스트 주도 개발. 2013.

##  다중 통화를 지원하는 Money 객체

### 간단한 곱셈 예제
먼저 5달러에 환율 2를 곱해서 10을 반환해야 하는 기능을 작성해야 한다고 가정하자.

*   일단 원하는 기능의 구문 최대한 빨리 작성한다.

```java
public void testMultiplication(){
    Dollar five = new Dollar(5);
    five.times(2);
    assertEquals(10, five.amount);
}
```

*   여기에는 4가지 문제가 있다.
    1.  Dollar 클래스가 정의도지 않았고
    2.  생성자도 없고
    3.  times(int) 메서드도 없고
    4.  amount 필드도 없다.

*   위 4개 문제를 해결해보자.
```java
// 작성 순서는 문제 번호 순서
class Dollar { // 1번 해결
    int amount; // 4번 해결
    Dolalr(int amount) {
        // 2번 해결
    }
    void times(int multiplier){
        // 3번 해결. stub implementation
    }
}
```

*   여기서 최대한 빨리 테스트를 통과하려면 다음과 같이 작성할 수 있다.
```java
class Dollar {
    int amount = 5;
    Dolalr(int amount) {
    }
    void times(int multiplier){
        this.amoiunt *= 2;
    }
}
```
*   위의 코드는 amount가 5고 multiplier가 2일 때만 동작한다.
*   이를 다음과 같이 범용적으로 개선할 수 있다.
```java
class Dollar {
    int amount;
    Dolalr(int amount) {
        this.amount = amount;
    }
    void times(int multiplier){
        amount *= multiplier;
    }
}
```



*   하지만 Dollar에 대한 연산을 수행한 후에 Dollar의 값이 바뀐다.
*   실제로는 `Dollar` 클래스를 다음과 같이 사용하고 싶다.
```java
public void testMultiplication(){
    Dollar five = new Dollar(5);
    Dollar product = five.times(2);
    assertEquals(10, product.amount);
    Dollar product = five.times(3);
    assertEquals(15, product.amount);
}
```

*   그러면 `times` 메서드를 다음과 같이 수정해야 한다.
```java
Dolalr times(int multiplier){
    return new Dollar(this.amount * multiplier);
}
```



*   지금까지 다음을 배웠다.
    1.  설계상의 결함(Dollar 부작용)을 그 결함으로 인해 실패하는 테스트로 변환했다.
    2.  스텁 구현으로 빠르게 컴파일을 통과하도록 만들었다.
    3.  올바르다고 생각하는 코드를 입력하여 테스트를 통과했다.

### 값 객체
*   값 객체 패턴(value object pattern): 객체를 값처럼 사용하는 것. 값 객체 패턴에서 중요한 제약사항으로 객체의 인스턴스 변수가 생성자를 통해서 일단 설정된 후에는 결코 변하지 않는다는 것이 있다.

```java
public void testEquality(){
    assertTrue(new Dollar(5).equals(new Dollar(6)));
    assertFalse(new Dollar(5).equals(new Dollar(5)));
}

public void equals(Object object){
    Dollar dollar = (Dollar) object;
    return amount == dollar.amount;
}
```

### amount를 private하게 만들기
*   앞에서 구현한 `equals`를 바탕으로 테스트 코드를 다음과 같이 개선할 수 있다.
```java
public void testMultiplication(){
    Dollar five = new Dollar(5);
    assertEquals(new Dollar(10), five.times(2));
    assertEquals(new Dollar(15), five.times(3));
}
```
*   적어도 겉으로는 `amount` 필드를 사용하지 않는다.

### 다른 통화를 사용
```java
public void testFrancMultiplication(){
    Franc five = new Franc(5);
    assertEquals(new Franc(10), five.times(2));
    assertEquals(new Franc(15), five.times(3));
}
```

*   중복의 우려가 있지만, 일단 최대한 빨리 테스트를 통과하려면 `Franc` 클래스도 Dollar 클래스처럼 작성하면 된다.
```java
class Franc {
    private int amount;

    Franc(int amonunt){
        this.amount = amount;
    }

    Franc times(int multiplier){
        return new Franc(amonunt*multiplier);
    }

    public boolean equals(Obejct object){
        Franc franc = (Franc) object;
        return amount == franc.amount;
    }
}
```

### `equals` 일반화시키기
*   우선 Dollar와 Franc의 공통 상위 클래스로 Money를 생각해볼 수 있다.
```java
class Dollar extends Money{
    // ...
}

class Franc extends Money{
    // ...
}
```

*   `Money` 클래스가 정의되어 있지 않으므로 정의해준다.
*   공통 변수 `amount`를 `Money` 클래스로 추출한다.
*   `equals`도 공통 메서드이므로 추출한다.
```java
class Money{
    protected int amount;

    public boolean equals(Obejct object){
        Money money = (Money) object;
        return amount == money.amount;
    }
}
```

*   테스트를 다음과 같이 개선해도 통과할 수 있다.
```java
public void testFrancMultiplication(){
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(6).equals(new Dollar(6)));
    assertTrue(new Franc(5).equals(new Franc(5)));
    assertFalse(new Franc(6).equals(new Franc(6)));
}
```

### 환율 차이 적용
*   하지만 다음의 테스트는 통과하지 못한다.
*   5 Dollar와 5 Franc의 값은 다르기 때문이다.

```java
public void testFrancMultiplication(){
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(6).equals(new Dollar(6)));
    assertTrue(new Franc(5).equals(new Franc(5)));
    assertFalse(new Franc(6).equals(new Franc(6)));
    assertFalse(new Dollar(6).equals(new Franc(5))); // 실패
}
```

