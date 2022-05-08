##  MIPS 명령어 필드
*   op(6bits)
*   rs(5bits)   first soure operand register
*   rt(5bits)   second source operand register
*   rd(5bits)   destination register (연산 결과 저장)
*   shamt(5bits) shift amount. 사용하지 않으면 0
*   funct(6bits) op필드가 대분류면 funct는 구체적인 연산 지정

##  주소 지정 방식
주소 지정 방식은 피연산자를 찾는 방법이다(CODME:134).

명령어의 필드와 오퍼랜드는 다르다.
필드는 물리적인 형식인 반면, 오퍼랜드는 논리적인 개념이다.

*   의미(또는 묵시적, 암묵적) 주소 지정방식: Implied mode
    *   명령어 자체에 피연산자가 전제되어 있어서 피연산자를 지정할 필요가 없다.
    *   예: call, push, pop
*   즉치 주소 지정방식 (Immediate mode)
    *   
*   직접 주소 지정방식 (Direct-addressing mode)
*   간접 주소 지정방식 (Indirect-addressing mode)
*   레지스터 주소 (직접) 지정방식 (Register mode)
*   레지스터 주소 간접 지정방식 (Register indirect mode)

*   상대 주소 지정방식 (Relative addressing mode)
*   인덱스된 주소 지정방식 (Indexed addressing mode)


CODME p135, p169, p177

**MIPS assembly language syntax는 기본적으로 AT&T syntax 형식에서 명령어 순서만 Intel syntax 형식을 채택했다고 볼 수 있다.**

실제 명령어 필드 순서를 보면 src1, src2, dst이지만 어셈블리 구문은 dst, src1, src2이다.
그런데 메모리 참조는 M\[r1\] 이런 형식이 아니라 ($r1)을 쓴다.
AT&T에서는 상수값에 $을 접두사로 붙이는 반면 MIPS는 $를 레지스터에 붙인다. (상수는 Intel syntax처럼 아무것도 안 붙인다)

operand - R: Register, C: Constant, M: Memory