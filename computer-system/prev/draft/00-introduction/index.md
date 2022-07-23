#   Index
이 글에서는 Computer System 목차를 크게 1부 Processor와 2부 Memory로 구분한다.

그리고 각 장에는 주제별로 다음 관점의 내용들을 수록하고자 한다.

*   RISC vs CISC 차이점 (ex: MIPS(or ARM) vs Intel x86)
*   application programming level
*   instruction architecture level
*   hardware implementation level
*   security issue(ex: Intel CPU gate, if possible)

이는 명령어 명세를 중심으로 다음과 같이 그릴 수 있다.

*   application programming level: C 명세나 코드 작성 레벨 또는 컴파일러 단계에서의 효율성 개선 (if possible)
*   일반적인 하드웨어 구현
*   주어진 아키텍처 맥락에서 효율성 개선(또는 극대화) 하드웨어 구현
*   추상적인(또는 수학적인) 접근(Boolean Algebra, Integer Arithmetic 등)

명령어 명세 이외의 내용(Parallelism, Virtualization 등)은 하드웨어 구현만 기술한다. 그리고 이 주제들을 아주 심도 있게 다루기에는 내용이 너무 많기도 하고 또 어려워서 퀄리티를 어느 정도 타협했다.


(기타)
##  회로 레벨 성능 향상
가산기 회로의 구현
곱셈기 회로의 구현(FFM, Fast Fourier Multiplication까지)
fma, mac