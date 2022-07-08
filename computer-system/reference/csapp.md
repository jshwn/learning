##  p76 C에서 TMin을 작성하는 방법

```cpp
//  limits.h
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
```

INT_MIN을 -2147483648로 규정하지 않는 이유는 무엇인가?




#   인터넷 검색 자료
Linux는 정적 라이브러리와 동적 라이브러리를 각각 static library(.a)와 shared library(.so)으로 부른다.
이때 확장자는 각각 archive와 shared objects를 의미한다.
반면 Windows는 각각을 libray(.lib)와 dynamic link library(.dll)라고 부른다.

Linux의 실행 파일 포맷은 ELF-64(Executable and Linkable Format)이지만, Windows의 실행 파일 포맷은 PE(Portable Executable)이다. macOS의 경우는 PEF(Preferred Executable Format)이다.

#   Chapter 7 링커

##  목적 파일의 종류
*   재배치 가능 목적파일
*   실행가능 목적파일
*   공유 목적파일

##  ELF 파일의 섹션들
*   .symtab
    *   symbol table. 전역변수와 함수에 대한 엔트리 정보가 기록되어 있다.
    *   컴파일러 내부 심볼 테이블과 달리 지역변수에 대한 엔트리는 없다.
*   .rel.text
    *   링커가 다른 파일들과 이 목적 파일을 연결할 때 수정해야 하는 .text 섹션 내 위치들의 리스트
*   .rel.data
    *   링커가 다른 파일들과 이 목적 파일을 연결할 때 수정해야 하는 .data 섹션 내 위치들의 리스트
*   .line
    *   최초 C 소스코드와 .text 내 머신코드 내 라인번호들 간의 매핑.
    *   -g 옵션으로 컴파일해야만 생긴다.

##  p661 관련
예를 들어 다음과 같이 컴파일한다고 해보다
```
gcc main.o libx.a liby.a libz.a
```
링커는 외부 참조를 해결하기 위해 다음의 집합을 둔다.
*   E: 재배치 가능 목적파일들의 집합
*   U: 미해석 심볼 집합(참조되지만 아직 정의되지 않은 경우)
*   D: 이전 입력 파일에서 정의된 심볼 집합.

링커는 위 명령줄의 파일들에 대해 ltr 순서로 링킹 작업을 한다.

만약 심볼을 정의하는 라이브러리가 심볼을 참조하는 목적파일 전에 명령줄에 나타난다면 이 참조는 해결되지 않는다.


##  7.12 위치-독립성 코드(PIC)
PIC: Position Independent Code. 링커의 어떠한 재배치 작업 없이 로드될 수 있는 코드.

문제는, 공유 라이브러리각 위치 독립적이어야 한다는 것과 별개로 공유 라이브러리 모듈들이 적재된 메모리 주소 위치는 고정적이지 않다.
공유 라이브러리의 메모리 위치가 고정적이라면 공유 라이브러리가 증가함에 따라 메모리 내부 단편화가 심화되기 때문이다.

### p678
지연 바인딩(lazy binding)은 각 프로시저 주소의 확정을 이 프로시저가 런타임에 처음 호출될 때까지 지연하는 것이다.
최초 호출 시 런타임 오버헤드가 존재하지만, 이후에는 바로 사용 가능.

*   GOT: Global Offset Table
*   PLT: Procedure Local Table

##  7.13 라이브러리 삽입
library interpositioning


##  7.14
GNU binutils 패키지
*   ar
*   strings
*   nm
*   size
*   readelf
*   objdump
*   ldd