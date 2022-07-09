#   실습 설정

##  gcc 옵션 설정
출처: https://hdacker.tistory.com/18

gcc -m32 -fno-stack-protector -mpreferred-stack-boundary=2 -no-pie -fno-pic -o main main.c
옵션을 하나하나 살펴보자.
 
*   -m32 : 32bit로 컴파일
*   -fno-stack-protecotr : 버퍼오버플로우가 발생했을 때 gcc는 canary를 이용해 버퍼오버플로우가 발생한 것을 감지하고 프로그램을 종료하는데 우리는 이를 SSP(Stack Smashing Protection)라 부르는데 이러한 보호기법(SSP)을 off한다.
*   -mpreferred-stack-boundary=2 : 32bit로 컴파일할 경우 main함수에 불필요한 instruction을 제거해준다.
*   -no-pie : 주소 고정
*   -fno-pic : 위치 독립 코드 사용 X
*   -o : 출력파일명 지정

참고: https://gcc.gnu.org/onlinedocs/gcc/Option-Index.html
참고: https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#Code-Gen-Options


*   -pg: gprof으로 프로그램을 프로파일링 하려면 이 옵션으로 컴파일해야 한다.
    *     -pg                     Enable mcount instrumentation
    *   참고: https://stackoverflow.com/a/7290284

##  gcc 옵션 prefix
참고: https://stackoverflow.com/a/64152114
참고: https://stackoverflow.com/a/71182423

*   "W": Warning ("w" disables all warnings, "Wall" warns all)  
*   "f" stands for flag. 이 prefix가 붙은 옵션은 주로 machine independent한 설정, 즉 컴파일러가 코드를 생성하는 것과 관련되어 있다https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#Code-Gen-Options.
*   "m": stands for "machine dependent"(https://gcc.gnu.org/onlinedocs/gcc/Submodel-Options.html#Submodel-Options)

##  행렬곱 관련 참고
*   https://blog.qiqitori.com/2018/05/matrix-multiplication-using-the-fma-instruction/
*   https://blog.qiqitori.com/2018/04/baby-steps-in-simd-sseavx/

*   https://junstar92.tistory.com/241

##  프로파일링 관련 참고
https://stackoverflow.com/q/375913

dbi: dynamic binary instrumentation 동적 바이너리 계측
gprof
google performance tool(https://github.com/gperftools/gperftools)