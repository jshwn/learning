#   데이터베이스 포렌식
*   데이터베이스 덤프: 테이블의 구조 또는 데이터를 SQL 구문 형식으로 파일에 기록.
*   데이터베이스 포렌식 도구
    *   LogMiner for Oracle
    *   Toad

##  MySQL의 경우
*   MySQL은 데이터베이스 별로 Data Directory를 부여하며, 각 데이터베이스에 테이블을 생성하면 어떠한 저장 엔진에도 상관없이 테이블에 대한 정보를 저장하는 .frm 파일이 테이블 이름으로 생성된다.
*   MySQL의 설절파일은 Unix 환경에서는 `/etc/my.cnf`에, Windows Server에서는 `my.ini`로 존재한다.
*   innodb 관련 정보: `blog.jcole.us/innodb`
*   `mysqlbinlog <binary file>`

*   general log
*   slow query log
*   event log(log_bin)