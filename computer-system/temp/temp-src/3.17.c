long absdiff(long x, long y){
    long result;

    if ( x < y) {
        result = y - x;
    } else {
        result = x - y;
    }
    return result;
}

//  3.17 absdiff의 어셈블리 코드 흐름 모사
long cmovdiff(long x, long y){
    long rval = y - x;
    long eval = x - y;
    long ntest = x >= y;    // cmpq
    if (ntest) rval = eval; // cmovge
    return rval;
}