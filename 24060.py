import sys
def merge_sort(ar):
    if len(ar) <=1:
        return ar
    mid = (len(ar)+1)//2
    left = ar[:mid]
    right = ar[mid:]
    print(left, right)       # q는 p, r의 중간 지점
    left = merge_sort(left) 
    right = merge_sort(right)  # 후반부 정렬
    return merge(left, right)

def merge(left, right):
    i = 0
    j =0
    tmp = []
    global cnt
    global k
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            tmp.append(left[i]); # tmp[t] <- A[i]; t++; i++;
            cnt += 1
            if cnt == k:
                print(left[i])
            i += 1
        else:
            tmp.append(right[j]); # tmp[t] <- A[j]; t++; j++;
            cnt += 1
            if cnt == k:
                print(right[j])
            j += 1
        #if cnt == k: print(tmp[-1])
        #print(cnt, k)
    while i < len(left):
        tmp.append(left[i])
        cnt += 1
        if cnt == k:
            print(left[i])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        cnt += 1    
        if cnt == k:
            print(right[j])
        j += 1
    
    return tmp

n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, (sys.stdin.readline().split())))
cnt = 0
merge_sort(lst)
if cnt < k:
    print(-1)
