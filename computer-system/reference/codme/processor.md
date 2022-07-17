파이프라이닝은 개별 명령어의 실행 시간을 단축시킬 수는 없지만, 명령어 처리량을 늘려서 전체 실행 시간을 단축시킨다.


##  stall vs bubble

### CS:APP p416
스톨링은 한 그룹의 인스트럭션들을 이들의 단계에 붙잡아두지만, 다른 인스트럭션들은 파이프라인을 계속 흘러가도록 한다. (중략) 우리는 이들을 인스트럭션을 해독 단계에 붙ㅈ바아 놓을 때마다 실행 단계에 *버블*을 삽입하는 방식으로 처리한다. 버블을 동적으로 생성된 nop 인스트럭션과 비슷하다: 이것은 레지스터, 메모리, 조건코드, 프로그램 상태를 변경시키지 않는다.

### CODME p320
이 그림은 파이프라인 지연(pipeline stall)이라는 중요한 파이프라이닝 개념을 보여 주고 있다. 지연은 거품(bubble)이라는 별명으로 불리는 경우도 많다.

### CODME p357
(중략)
거품처럼 동작하는 이 nop을 어떻게 파이프라인에 삽입할 수 있을까?
그림 4.49에서 EX, MEM, WB 단계의 9개 제어 신호 모두를 인가하지 않으면 nop 명령어를 만들 수 있다.
ID 단계에서 해저드를 찾아내면 ID/EX 파이프라인 레지스터의 EX, MEM, WB 제어 필드 값을 모두 0으로 만들어서 파이프라인에 거품을 집어넣을 수 있다. 이 제어값들은 매 클럭마다 앞으로 전진하면서 적절한 작업을 한다. 모든 제어값이 0이므로 레지스터나 메모리 값은 전혀 바뀌지 않는다.

### CODME 그림 4.59
and 명령어를 nop으로 바꿈으로써 클럭 사이클 4부터 거품이 삽입되었다. and 명령어가 실제로는 클럭 사이클 2에서 인출(IF)되고 클럭 사이클 3에서 해독(ID)되지만, 이 명령어의 EX 단계는 클럭 사이클 5까지 (1사이클) 연기된다.

### 결론
아예 컴파일 타임에 컴파일러가 nop를 삽입할 수도 있지만, 프로세서가 해저드를 검출하고 다음 단계의 제어 값을 nop로 설정할 수 있다. 이때 이전 단계들의 데이터와 명령 회로 값들은 그대로 단계별 레지스터에 저장되어 있다.

중요한 것은 stall과 bubble 모두 추상적인 개념이지, 물리적인 방법이 아님을 이해해야 하는 것이다.

##  p316 파이프라이닝을 위한 명령어 집합 설계
모든 MIPS 명령어는 같은 길이를 갖는다.
이는 명령어를 해독하는 것을 훨씬 쉽게 해준다.
x86처럼 하위 호환성 보장 등의 이유로 명령어 길이가 다른 경우에는 마이크로 명령어로 변환시켜 파이프라이닝을 한다.

MIPS 명령어 필드에서 src 레지스터 필드 `rs`는 같은 위치(\[25:21\])에 있다.
이는 opcode 해독과 레지스터 파일 읽기를 동시에 수행할 수 있다.

MIPS에서는 매모리 피연산자가 메모리 적재와 메모리 저장 명령어에서만 나타난다.
이는 MIPS의 단일 명령어가 메모리 피연산자를 연산에 사용할 수 없다는 것이다.
만약 x86처럼 메모리 피연산자를 연산에 사용하게 된다면 주소 계산, 메모리 읽기, 연산 실행 단계가 추가로 확장되어야 한다.

##  제어 해저드와 그 대응
*   분기 시 지연(Stall on Branch)
*   분기 예측(Branch Prediction)
*   지연 분기(Delayed Branch)

### 지연 분기
지연 분기: 분기 명령어와 관계없이 실행해야 하는 명령어들을 분기 명령어 뒤로 옮기는 것이다.

즉 순서 상 분기 명령어보다 선행하는 명령어들을 필요한만큼 분기 명령어 뒤로 옮기는 것이다.
따라서 명령어를 버리거나 시간을 지체할 일 없이 분기 결정에 따른 다음 명령어를 파이프라인에 넣을 수 있다.
이때 CODME에서는 1개 명령어를 옮기는 것으로 기술한다.

책에서는 p325에 "지연 분기가 분기 지연이 작을 때 효용이 있기 때문에 한 사이클보다 큰 지연분기를 사용하는 프로세서는 없다. 더 긴 분기 지연에는 하드웨어 기반의 분기 예측이 사용된다."라고 한다.
이에 대해서는 아마 분기와 관련 없는 명령어를 2개 이상 넣어야 할때부터는 데이터 해저드를 고려해야하기 때문인 것으로 추측한다.
그래서 2개 명령어 이상을 분기 명령어 뒤로 옮기지 않는 것 같다.

##  4.10 예외

### p370
많은 구조와 또 많은 저자들이 인터럽트와 예외를 구분하지 않고 두 종류의 사건을 지칭하기 위해 오래된 이름인 인터럽트를 사용한다. 예를 들면 Intel x86은 인터럽트라는 용어만 사용한다. 우리는 MIPS의 규약을 좇아서 원인이 내부적인지 외부적인지는 구분하지 않고 제어 흐름이 예끼치 못한 변화를 지칭하는 데 예외라는 용어를 쓰고, 사건이 외부적인 요인으로 일어날 경우에만 인터럽트라는 용어를 사용한다.

===
이러한 구분은 어느 정도 타당하다고 본다.


##  4.11 명령어를 통한 병렬성
다중 내보내기(multi issue)는 컴파일 타임과 런타임 구현으로 구분할 수 있다.

*   정적 다중 내보내기
    *   루프 언롤링과 레지스터 재명명
    *   VLIW
*   동적 다중 내보내기
    *   슈퍼스칼라

*   동적 파이프라인 스케줄링(비순차 실행)
    *   일반적으로 슈퍼스칼라를 전제

### p388
비순차 실행을 하면 이전 파이프라인 구조에서는 보지 못했던 새로운 파이프라인 해저드가 생긴다.
이름 종속성(name dependence)은 두 명령어가 같은 레지스터나 메모리 주소를 사용할 때 발생한다.
*   반종속성(antidependence)
*   쓰기 종속성(output dependence)

*   반종속성은 WAR(Write After Read) 해저드를 일으킨다.
*   쓰기 종속성은 WAW(Write After Write) 해저드를 일으킨다.
*   진성 데이터 종속성은 (Read After Write) 해저드를 일으킨다.