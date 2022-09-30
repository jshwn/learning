#   프로그래머스 SQL

##  행 개수 출력
*   MySQL
    *   LIMIT N
*   Oracle
    *   WHERE ROWNUM <= N

##  문자열 split
*   MySQL
    *   `SUBSTRING_INDEX`가 있기는 한데, 특정 위치까지의 문자열을 출력하는 것이 문제이다.
        *   예: `SUBSTRING('A-B-C', 1)` = A, `SUBSTRING('A-B-C', 2)` = A B

*   Oracle
    *   보통 정규식을 사용해서 요소들을 delimeter로 분할하여 접근한다.

##  DATETIME 조작
*   문제
    *   입양 시각 구하기(1)
*   MySQL
    *   YEAR(DATETIME), MONTH(DATETIME), DAY(DATETIME), HOUR(DATETIME), MINUTE(DATETIME), SECOND(DATETIME) 함수로 원하는 단위 추출
*   ORACLE
    *   EXTRACT( `YEAR | MONTH | DAY` FROM DATETIME ) 형식으로 사용할 수 있으나, 시분초는 추출할 수 없다.
    *   TO_CHAR(DATETIME, 'HH')는 12시간 기준으로 시간이 나오므로, 24시간 기준으로 시간을 추출하고 싶으면 'HH24'로 사용해야 한다.
    *    ORACLE에서 표현식의 ALIAS는 GROUP BY 절과, WHERE절에는 사용할 수 없어서 인라인 뷰를 쓰거나 GROUP BY 대신 WHERE절을 사용해야 한다(M).

### 입양 시각 구하기(1)
```sql
--MySQL
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR > 8 AND HOUR < 20
ORDER BY HOUR
```

```sql
--Oracle
SELECT HOUR, COUNT(*) AS COUNT
FROM (SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR
      FROM ANIMAL_OUTS)
GROUP BY HOUR
HAVING HOUR > 8 AND HOUR < 20
ORDER BY HOUR
```

### 입양 시각 구하기(2)
```sql
--MySQL
--연속적인 숫자를 생성하는 코드가 MySQL에서는 매우 길어서 SQL Statements를 사용
SET @HOUR = -1;
SELECT (@HOUR := @HOUR +1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME))
    FROM ANIMAL_OUTS 
    WHERE HOUR(DATETIME)=@HOUR) AS COUNT 
    FROM ANIMAL_OUTS
WHERE @HOUR < 23;
```

```sql
--Oracle
--0부터 23까지의 연속적인 숫자 인라인 뷰를 생성하여 대상 인라인 뷰와 LEFT OUTER JOIN을 수행
SELECT A_HOUR AS HOUR, COUNT(B_HOUR)
FROM (SELECT level-1 AS A_HOUR
      FROM DUAL
      CONNECT BY level <= 24) A
      LEFT OUTER JOIN
      (SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS B_HOUR
       FROM ANIMAL_OUTS) B
      ON A_HOUR = B_HOUR
GROUP BY A_HOUR
ORDER BY A_HOUR
```

