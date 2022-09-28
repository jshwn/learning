import heapq
from math import inf
from typing import List

seq=[1,5,3,2,4]

def bubble_sort(seq:List):
    n = len(seq)
    for i in range(n):
        for j in range(i+1, n): # i+1부터 시작하는 것에 주목
            l = seq[i]
            r = seq[j]

            # 오름차순 전제
            # 전자가 후자보다 크다면, 전자와 후자의 위치를 바꿈
            if l > r:
                seq[i], seq[j] = r, l
    
    return seq

# print(bubble_sort(seq))

def insert_sort(seq:List):
    n = len(seq)
    for i in range(n):
        for j in range(i+1, n):
            l = seq[i]
            r = seq[j]

            # 오름차순 전제
            # 전자가 후자보다 크다면,  
            if l > r:
                seq.pop(j)
                seq.insert(i, r)
    
    return seq

# print(insert_sort(seq))

#   top-down
def merge_sort(seq:List, left:int, right:int):
    if left >= right: return

    n = len(seq)
    mid = (left+right)//2

    merge_sort(seq, left, mid)
    merge_sort(seq, mid+1, right)

    sorteds = [0 for _ in range(n)]

    i = left
    j = mid+1
    k = left

    # left와 right에서 pointer를 두고 비교하면서 정렬
    while not ( i>mid or j>right ):
        l = seq[i]
        r = seq[j]

        # 오름차순 전제
        if l > r:
            sorteds[k] = seq[j]
            j+=1
        else:
            sorteds[k] = seq[i]
            i+=1
        
        k+=1
    
    #   남은 값들을 복사
    if i>mid:
        while j <= right:
            sorteds[k] = seq[j]
            k+=1; j+=1
    else:
        while i <= mid:
            sorteds[k] = seq[i]
            k+=1; i+=1
    
    for i in range(left, right+1):
        seq[i]=sorteds[i]
    
    return seq

# print(merge_sort(seq,0,len(seq)-1))

#   top-down, more pythonic
def merge_sort(seq:List):
    n = len(seq)
    if n==1: return seq

    #   left, right 각각 merge sort 수행
    mid = n//2
    lefts, rights = seq[:mid], seq[mid:]
    lefts = merge_sort(lefts)
    rights = merge_sort(rights)

    #   iterator로 변환
    lefts = iter(lefts)
    rights = iter(rights)

    flag=0
    l = next(lefts)
    r = next(rights)

    for i in range(n):
        # 오름차순 전제
        flag = 0 if l > r else 1
        seq[i] = l if flag else r

        #   iteration이 끝나면 inf를 반환
        if flag: l = next(lefts, inf)
        else: r = next(rights, inf)

    return seq

# print(merge_sort(seq))

def quick_sort(seq:List):
    n = len(seq)
    if n < 2:
        return seq
    
    mid = n//2 # 중간 원소를 피벗으로 설정
    pivot = seq[mid]
    left = []
    right = []
    equal = []

    for x in seq:
        if x < pivot:
            left.append(x)
            continue
        if x > pivot:
            right.append(x)
            continue

        equal.append(x)
    
    return quick_sort(left) + equal + quick_sort(right)

# print(quick_sort(seq))

#   raw way
def heap_sort(seq:List):

    def heapify(seq:List, n:int, i:int):
        curr = i
        l = 2*i + 1; r = 2*i + 2
        if l >= n and r >= n:
            return
        
        #   오름차순 전제
        if seq[curr] > seq[l]: curr = l
        if seq[curr] > seq[r]: curr = r
        
        if curr == i: return
        seq[curr], seq[i] = seq[i], seq[curr] # swap
        heapify(seq, n, curr)

    n = len(seq)

    #   heapify seq
    for i in range(n//2 - 1, -1, -1):
        heapify(seq, n, i)

    #   heap sort
    for i in range(n-1, 0, -1):
        seq[i], seq[0] = seq[0], seq[i]  # swap
        heapify(seq, i, 0)
    
    return seq

#   simple and pythonic way
def heap_sort(seq):
    n = len(seq)

    heapq.heapify(seq)
    return [heapq.heappop(seq) for _ in range(n)]

print(heap_sort(seq))