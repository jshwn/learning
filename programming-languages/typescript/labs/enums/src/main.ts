import { CONST_ENUM } from "./module";

enum NUMBER_ENUM {
  ZERO,
  ONE,
}

enum STRING_ENUM {
  ZERO  = '0',
  ONE = '1',
}


console.log(NUMBER_ENUM.ZERO);
console.log(STRING_ENUM.ZERO);
console.log(CONST_ENUM.ZERO);
