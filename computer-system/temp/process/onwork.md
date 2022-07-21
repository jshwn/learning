#   Process
*   candidates for title
    *   Process Implementation
    *   Process Model
*   프로세스를 보는 관점
    *   운영체제의 관점
    *   프로그래머(또는 컴파일러) 관점

##  Process Memory Layout
*   virtual memory를 전제함.
*   logical segments (segmentation이 아님)
*   how linux implements virtual memory assignment

##  Calling Convention
*   Function Calling Sequence를 전제함.
    *   stack frame, function prologue and epilogue

##  Position Independent Code
*   dynamic linking

## Reference
공식
*   [x86-64-psABI-1.0.pdf](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjfob6-74b5AhUupVYBHUKVC4cQFnoECBIQAQ&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwiki%2Fhjl-tools%2Fx86-psABI%2Fx86-64-psABI-1.0.pdf&usg=AOvVaw2p1uIh84JntqPon1_HJL1O)
*   [x64 ABI conventions - Microsoft Docs](https://docs.microsoft.com/en-us/cpp/build/x64-software-conventions?view=msvc-170)
*   [Linux Standard Base Core Specification for X86-64](https://refspecs.linuxfoundation.org/LSB_5.0.0/LSB-Core-AMD64/LSB-Core-AMD64.pdf)


위키피디아
*   [Subroutine - Wikipedia](https://en.wikipedia.org/w/index.php?title=Subroutine&oldid=1093300550)
*   [Calling convention - Wikipedia](https://en.wikipedia.org/w/index.php?title=Calling_convention&oldid=1090983016)
*   [Call Stack - Wikipedia](https://en.wikipedia.org/w/index.php?title=Call_stack&oldid=1094890277)
*   [Red zone (computing) - Wikipedia](https://en.wikipedia.org/w/index.php?title=Red_zone_(computing)&oldid=1033097887)

기타
*   [Agner Fog](https://www.agner.org/optimize/calling_conventions.pdf)
*   [Memory Layout Lab](https://gist.github.com/CMCDragonkai/10ab53654b2aa6ce55c11cfc5b2432a4)