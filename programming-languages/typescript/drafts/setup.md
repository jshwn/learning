#   Setup

##  contents
*   namespaces
*   Moudle
*   Triple-Slash Directives

##  Module vs Namespaces

### Modules
*   syntax
    *   CommonJS and ES Modules interop with `compilerOptions/esModuleInterop`
*   module resolution
    *   `compilerOptions/traceResolution`으로 module resolution 과정을 확인 가능
*   module output target

### Namespaces

##  Triple-Slash Directives
`compilerOptions/noResolve=true`이면 triple-slash directives가 무시된다.

*   `/// <reference path="..." />`
*   `/// <reference types="..." />`
*   `/// <reference lib="..." />`: library file의 ecma 버전 명시
*   `/// <reference no-default-lib="true"/>`
    *   `compilerOptions/skipDefaultLibCheck=true`면 해당 파일을 스킵한다.
*   `/// <amd-module/>`
*   `/// <amd-dependency/>`

##  Declaration, Declaration merging

##  library declaration files
