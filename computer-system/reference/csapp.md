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

##  7.12 위치-독립성 코드(PIC)
PIC: Position Independent Code