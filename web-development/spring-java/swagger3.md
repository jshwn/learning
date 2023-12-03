# Spring Boot
Spring Version이 3.X부터는 spring doc을 사용하는 것이 좋다.

```groovy
# ./build.gradle
plugins {
	id 'java'
	id 'org.springframework.boot' version '3.2.0'
	id 'io.spring.dependency-management' version '1.1.4'
	id 'com.netflix.dgs.codegen' version '6.0.3'
}
```

springfox github는 2020년 7월 14일 이후로 release가 없다.
따라서 springdoc을 사용해야 한다.
[https://springdoc.org/](https://springdoc.org/) 참고
[Demo Source Code](https://github.com/springdoc/springdoc-openapi-demos/tree/2.x/demo-spring-boot-3-webmvc)

설정을 위해 별도의 SwaggerConfig 클래스를 만들지 않으며, 설정 변경은 application.yml에서 가능하다.