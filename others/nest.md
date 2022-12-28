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

*   order of request utilities
    1.  Middleware log
    2.  Guard log
    3.  Interceptor log before controller
    4.  Pipe log
    5.  Exception Filter log
    6.  Interceptor log after controller(if no exception)

*   Authorization
    *   role base vs policy base
    *   RBAC: Role-Based Access Control
    *   Claim based Access Control (or ABAC, Attribute-Based Access Control)

*   nest-router for route nesting

+   `fluent interface`: design which relies on method chaining