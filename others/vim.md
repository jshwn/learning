#   Vim

*   `esc`: 명령 모드
*   `/`: 검색 모드
*   `i`: insert(커서 앞)
*   `a`: append(커서 뒤)
*   `I`: 라인 맨 앞에 insert
*   `A`: 라인 맨 뒤에 append
*   `hjkl`: 좌하상우
*   `0`: 라인 맨 앞으로 이동
*   `$`: 라인 맨 앞으로 이동
*   `w`: 한 단어 이후로 이동
    *   `8w` 8 단어 이후로 이동
*   `b`: 한 단어 이전으로 이동
    *   `8w` 8 단어 이전으로 이동
*   `H`: 화면 위
*   `M`: 화면 중간
*   `L`: 화면 끝
*   `gg`: 파일 앞
*   `G`: 파일 끝
    *   `20G`: 20번째 줄로 이동

*   `x`: 현재 커서에서 한 글자 삭제
*   `dd`: 현재 문장 삭제
*   `yy`: 복사
*   `p`: 붙여넣기, paste
*   `*p`
*   `u`: 되감기, undo
*   `ctrl + r`: 앞감기, redo

*   `v`: select 범위 지정

##  Vim의 철학
command + object
*   `d 3w`: 3단어 삭제

##  vim tips
*   `d a w`: delete a word
*   `d 2 j`: delete 2 lines below
*   `d 3 h`: delete 3 lines above
*   `d i {`: delete inside { }
*   `d a (`: delete all inside ()
*   `d a '`: delete all inside ' including '
*   `c i [`: change inside [] (자동으로 insert 모드로 진입)
*   `d f (`: delete 