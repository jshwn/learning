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

##  Dynamic Module
*   원래 배웠던 방식은 static module binding
*   static module binding에서는 module이 provider에 영향을 미칠 수가 없다. 즉 provider 의존성을 controller나 다른 module에 전파하는 역할밖에 못한다.
*   dynamic module에서는 module에서 `DynamicModule`을 통해 provider에 정보를 넘겨줄 수가 있다.
+   bootstrap time에 인스턴스화된다. runtime에 인스턴스화되는 것은 lazy module이다.

```ts
// example
// ./config/config.service.ts
import * as dotenv from 'dotenv';
import * as fs from 'fs';
import { Injectable, Inject } from '@nestjs/common';
import { EnvConfig } from './interfaces';

@Injectable()
export class ConfigService {
  private readonly envConfig: EnvConfig;

  constructor(@Inject('CONFIG_OPTIONS') private options: Record<string, any>) {
    const filePath = `${process.env.NODE_ENV || 'development'}.env`;
    const envFile = path.resolve(__dirname, '../../', options.folder, filePath);
    this.envConfig = dotenv.parse(fs.readFileSync(envFile));
  }

  get(key: string): string {
    return this.envConfig[key];
  }
}

// ./config/config.module.ts
import { DynamicModule, Module } from '@nestjs/common';
import { ConfigService } from './config.service';

@Module({})
export class ConfigModule {
  static register(options: Record<string, any>): DynamicModule {
    return {
      module: ConfigModule,
      providers: [
        {
          provide: 'CONFIG_OPTIONS',
          useValue: options,
        },
        ConfigService,
      ],
      exports: [ConfigService],
    };
  }
}

// app.module.ts
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ConfigModule } from './config/config.module';

@Module({
    imports: [ConfigModule.register({ folder: './config' })],
    controllers: [AppController],
    providers: [AppService],
})
export class AppModule {}
```


##  other features
*   lazy module
    *   ref: https://docs.nestjs.com/fundamentals/dynamic-modules
    *   necessity for low bootstrap time.
    *   bootstrap의 시간 부담을 각 모듈을 호출할 때 나누어 부담하는 방식.

*   Authorization
    *   role base vs policy base
    *   RBAC: Role-Based Access Control
    *   Claim based Access Control (or ABAC, Attribute-Based Access Control)

*   nest-router for route nesting


##  Microservices
NestJS Apllication as Client

ClientProxy is lazy

* more readings
  * https://dev.to/nestjs/part-1-introduction-and-setup-1a2l
  * https://dev.to/johnbiundo/series/4724
  * https://dev.to/nestjs/part-1-introduction-and-setup-1a2l


##  TODO


##  others
+   `fluent interface`: design which relies on method chaining
+   barrel files
    *   IDE가 symbol tracking을 충분하게 지원한다면 기능 상의 이유로 필요하진 않을 것.
    *   nestjs에서도 barrel file을 만드는 것을 추천하지 않는다.
*   The Twelve Factors App
    *   ref: https://12factor.net



##  Core Anatomy
Java Spring의 Module과 Bean은 NestJS의 Module과 Provider에 각각 대응한다고 볼 수 있다(1:1 대응인지는 확신 X)


### line by line
*   version: `@nestjs/core ^9.0.0`

* `await NestFactorry.create(AppModule);`
  * `NestFactorry.create()` context starts
  * `const container = new NestContainer(new ApplicationConfig());`
  * `await this.initialize(module, container, applicationConfig, httpServer);`
  * paramter evaluated form: `await this.initialize(AppModule, container, applicationConfig, httpServer);`
  * `NestContainer.initialize()` context starts
    * `const instanceLoader = new InstanceLoader(container);`
    * `const teardown = this.abortOnError === false ? rethrow : undefined;`
    * evaluated form:
      * `const teardown = true === false ? rethrow : undefined;`
      * `const teardown = undefined;`
    * `await ExceptionsZone.asyncRun(...)`
    * `ExceptionsZone.asyncRun()` context starts
      * `await dependenciesScanner.scan(module);`
      * `DependenciesScanner.scan()` context starts
        * `await this.registerCoreModule();`
        * `DependenciesScanner.registerCoreModule()` context starts
          *   ```ts
              // evaluated form:
              const moduleDefinition = InternalCoreModuleFactory.create(
                container,
                DependenciesScanner
                ModuleCompiler(),
                HttpAdapterHostRef(),
              );
              ```
            * `InternalCoreModuleFactory.create` context starts
            * **ref for moduleDefinition which is return value of `DependenciesScanner.registerCoreModule()`** : https://github.com/nestjs/nest/blob/aa3ad07c1023b71edda6b6ea53374787d3712231/packages/core/injector/internal-core-module/internal-core-module-factory.ts#L19
            * `InternalCoreModuleFactory.create` context ends
          * `const [instance] = await this.scanForModules(moduleDefinition);`
          * `DependenciesScanner.scanForModules` context starts
            * `const moduleInstance = await this.insertModule(moduleDefinition, scope);`
            * `DependenciesScanner.insertModules()` context starts
              *   ```ts
                  const moduleToAdd = this.isForwardReference(moduleDefinition)
                    ? moduleDefinition.forwardRef()
                    : moduleDefinition;
                  ```
                * `DependenciesScanner.isForwardReference()` context starts
                  * ref for return value: https://github.com/nestjs/nest/blob/aa3ad07c1023b71edda6b6ea53374787d3712231/packages/core/scanner.ts#L542
                  * evaluated form of return value: `module`
                * `DependenciesScanner.isForwardReference()` context ends
                * `return this.container.addModule(moduleToAdd, scope);`
                * `NestContainer.addModule()` context starts
                  * `const { type, dynamicMetadata, token } = await this.moduleCompiler.compile(metatype);`
                  * `ModuleCompiler.compile()` context starts
                    * `const { type, dynamicMetadata } = this.extractMetadata(await metatype);`
                    * `ModuleCompiler.extractMetadata()` context starts
                      * `if (!this.isDynamicModule(metatype)) {return { type: metatype };}`
                      * evaluated form
                        * `if (!(!!metatype.module)){return { ... };}`
                        * `if (!true){ ... }`
                      * **InternalCoreModule as `metatype` is Dynamic Module**
                      * `const { module: type, ...dynamicMetadata } = metatype;`
                      * `return { type, dynamicMetadata };`
                      * evaluated form of return value: `{ type: metatype.module, dynamicMetadata: { ...metatype properties except module } }`
                    * `ModuleCompiler.extractMetadata()` context ends
                    * `const token = this.moduleTokenFactory.create(type, dynamicMetadata);`
                    * `ModuleTokenFactory.create(metatype, dynamicModuleMetadata)` context starts
                      * parameter `metatype`: instance of class `InternalCoreModule`
                      * parameter `dynamicModuleData`: `exports`, `providers`, `metatype`, ...
                      * if moduleId is not saved in `moduleTokenFactory.moduleIdsCache` (which is WeakMap):
                        * `moduleId = randomStringGenerator();`
                        * `this.moduleIdsCache.set(metatype, moduleId);`
                      * `return hash(opaqueToken, { ignoreUnknown: true })`
                    * `ModuleTokenFactory.create()` context ends
                    * `return { type, dynamicMetadata, token };`
                      * 이때 token은 opaqueToken
                  * `ModuleCompiler.compile()` context ends
                  * `const moduleRef = new Module(type, this);`
                  * evaluated form: `const moduleRef = new Module(internalCoreModule, NestContainer);`
                    * `Module.constructor()` context starts
                      * 생략
                    * `Module.constructor()` context ends
                  * 생략
              * `DependenciesScanner.insertModules()` context ends
              * `ctxRegistry.push(moduleDefinition);`
            * 생략
      * `InstanceLoader.createInstancesOfDependencies()` context starts
        * `this.createPrototypes()` context starts
