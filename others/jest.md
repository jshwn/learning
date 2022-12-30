#   Jest


##  Matchers
*   `expect()`: value tester function which returns  "expectation" object(`jest.JestMatchers<T>`)
*   `expect().matcher()`: matcher function(or method)


##  Setup and Teardown
*   Repeating Setup
    *   `beforeEach()`
    *   `afterEach()`

*   `describe`, alias of `describe.only`
*   `it`, alias of `it`
*   When they are inside a describe block, the `beforeAll` and `afterAll` blocks only apply to the tests within that describe block.

##  other features
*   `jest-diff`
    *   ```js
        const { diff } = require('jest-diff');
        
        const a = { a: { b: { c: 5 } } };
        const b = { a: { b: { c: 6 } } };
        
        const result = diff(a, b);
        
        // print diff
        console.log(result);
        ```
        ```sh
        - Expected
        + Received

        Object {
            "a": Object {
            "b": Object {
        -       "c": 5,
        +       "c": 6,
            },
            },
        }
        ```
