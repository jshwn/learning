#   Nest.js

*   Frontend(or Preprocess) of Controller
    *   Guard(`@UseGuard`, `CanActivate`)
    *   Interceptor (also postprocess)
    *   Middleware
    *   Pipe
*   Exception Filter
*   Interceptor
    *   `Execution Context` parameter is smae as `Guard` one.
    *   `CallHandler` parameter means Route Controller function
*   Provider: Service, Repository, Factory, Helper, ...
    *    `@Injectable()` decorator marks class as a provider.
    *   property in provider
        *   `provide`: Provider Token. could be class or string.
            *   if `provide` value is string, need to specify the dependency when doing dependency injection as below:
            *   ```ts
                // AppModule
                import { connection } from './connection';
                @Module({
                  providers: [
                    {
                      provide: 'CONNECTION',
                      useValue: connection,
                    },
                  ],
                })
                export class AppModule {}
                // CatsModule
                @Injectable()
                export class CatsRepository {
                  constructor(@Inject('CONNECTION') connection: Connection) {}
                }
                ```
        *   `useClass`: Compatiable Class with `provide` Class
        *   `useValue`: Compatiable Interface, Class, literal object of Class instance of Class with `provide` Class
        *   `useFactory`: allows for creating providers dynamically
            *   can be used to support asynchronous provider feature. [ref](https://docs.nestjs.com/fundamentals/async-providers)
        *   `inject`: optional when using `useFactory`. should be list and its get injected into as useFactory's function arguents
        *   `useExisting`: allows you to create aliases for existing providers.
        *   `scope`: specify scope.
            ```ts
            import { Scope } from '@nestjs/common';
            {
              // ...
              scope: Scope.DEFAULT | Scope. REQUEST | Scope.TRANSIENT
              // ...
            }
            ```

*   `ExecutionContext`
    *   inherits `ArgumentsHost`
    *   `rpc`, `http`, `graphql` 형식이 있다.
*   `reflector`
    *   controller나 serviced에서 metadata에 접근할 수 있게 도와주는 helper

*   `Injection Scope`
    *   Scope Hierarchy
        *   **request-scoped provider에 의존하는 controller는 instantiation 시에 request-scope된다.**
            *   다만 transient-scope의 경우에는 그러하지 아니하다. (명시적으로 scope을 지정해야 한다)
    *   Request Provider (Context Provider in GraphQL)
        *   `REQUEST` scope의 Provider에서 Request object에 접근할 수 있도록 도와주는 것
        *   용례(or necessity to use request-scope)
            *   per-request caching in GraphQL applications
            *   request tracking
            *   multi-tenancy
        *   ` application lifecycle`를 따르지 않기 때문에 (Application) Lifecycle Hook을 사용할 수 없다.
        ```ts
        import { Injectable, Scope, Inject } from '@nestjs/common';
        import { REQUEST } from '@nestjs/core';
        import { Request } from 'express';

        @Injectable({ scope: Scope.REQUEST })
        export class CatsService {
          constructor(@Inject(REQUEST) private request: Request) {}
        }
        ```
    *   Inquirer Provider: 해당 provider가 inject된 부모를 parameter가 반환하도록 한다.
        ```ts
        import { Inject, Injectable, Scope } from '@nestjs/common';
        import { INQUIRER } from '@nestjs/core';

        @Injectable({ scope: Scope.TRANSIENT })
        export class HelloService {
          constructor(@Inject(INQUIRER) private parentClass: object) {}
        }
        ```

*   order of request utilities
    1.  Middleware log
    2.  Guard log
    3.  Interceptor log before controller
    4.  Pipe log
    5.  Exception Filter log
    6.  Interceptor log after controller(if no exception)

*   **Durable Provider**
    *   [출처](https://docs.nestjs.com/fundamentals/injection-scopes#durable-providers)
    *   n명의 이용자들이 서버에 로그인한다고 가정하자. 이용자들의 로그인 세션을 DB에서만 관리하고 하나의 context(인스턴스 구조: Controller-Service-Repository. 각 context의 identity는 contextId로 구분된다. ExecutionContext와 혼동하지 않도록 유의할 것)로 이를 운영한다면 잘못된 로직에 의해 서버 인스턴스에서 다른 이용자들의 정보가 침해될 수 있다. 이는 n명의 이용자들마다 별개의 context를 생성해서 로직을 격리시키면 해결할 수 있다. 이러한 설계가 개념적으로는 타당하다고 볼 수 있다.
    *   하지만 n명의 이용자마다 context를 생성해야 하지, n명의 이용자 별로 m개의 requrest마다 새로 context를 생성하는 것은 시간 낭비이다. 그리고 `REQUEST` scope는 n*m개의 context를 생성해야만 하는 한계가 존재한다(request별 생성이니까).
    *   따라서 NestJS에서는 이미 인스턴스를 생성한 tenant에 대해서는 이미 생성된 context를 반환하고, 새로 접속한 tenant에 대해서만 context를 새로 생성할 수 있도록 `ContextIdStrategy`를 제공한다.
    *   `main.ts` 파일에 `ContextIdFactory.apply(new Custom_ContextIdStrategy());` 코드로 해당 ContextIdStrategy를 등록한다.

*   Circular Dependency
    1.  forward referencing
        *   [on provider level](https://docs.nestjs.com/fundamentals/circular-dependency#forward-reference)
        *   [on module level](https://docs.nestjs.com/fundamentals/circular-dependency#module-forward-reference)
    2.  using `ModuleRef`
        *   on default provider: `moduelRef.get(TargetProviderClass)`
        *   on request-scoped provider: `moduelRef.resolve()`
        *   `registerRequestByContextId()`: ioc container에 등록(register)되지 않은 reqeust-scoped provider를 provider의 method scope에서 동적으로 컨테이너에 등록할 수 있다.
        *   `create`: dynamic instantiation of custom class as provider
        *   `introspect`: ??

*   lazy module
    *   necessity for low bootstrap time.
    *   bootstrap의 시간 부담을 각 모듈을 호출할 때 나누어 부담하는 방식.

*   Authorization
    *   role base vs policy base
    *   RBAC: Role-Based Access Control
    *   Claim based Access Control (or ABAC, Attribute-Based Access Control)

*   nest-router for route nesting


##  TODO
*   Dynamic Modules
*   Testing
*   

##  others
+   `fluent interface`: design which relies on method chaining
+   barrel files
    *   IDE가 symbol tracking을 충분하게 지원한다면 기능 상의 이유로 필요하진 않을 것.
    *   nestjs에서도 barrel file을 만드는 것을 추천하지 않는다.
*   The Twelve Factors App
    *   ref: https://12factor.net