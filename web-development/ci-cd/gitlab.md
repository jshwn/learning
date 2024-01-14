# Gitlab CI/CD

[Gitlab Docs](https://docs.gitlab.com/ee/topics/build_your_application.html)

##  Overview

##  개념 정의
* runner
* pipeline: job과 stage로 구성되는 ci/cd의 최상위 단위
* stage: 
* job: runner가 실행해야 하는 명령 모음
  * `script`가 명시되어 있는 것.
* artifact: job에 의해 생성되는 파일. 
* cache: 프로젝트 의존성을 저장하는 데에 사용하는 캐시.