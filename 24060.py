import sys


def merge_sort(ar, p, r):
    if p < r:
        q = abs((p + r)//2);       # q는 p, r의 중간 지점
        print(p, q, r)
        ar1 = merge_sort(ar, p, q) 
        ar2 = merge_sort(ar, q + 1, r)  # 후반부 정렬
        ar = merge(ar1+ar2, p, q, r)        # 병합
        return ar
# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(ar, p, q, r):
    global cnt 
    i = p
    j = q + 1
    tmp =[]
    while (i <= q) and (j <= r):
        if ar[i] <= ar[j]:
            tmp.append(ar[i]); # tmp[t] <- A[i]; t++; i++;
            i += 1
            cnt += 1
        else:
            tmp.append(ar[j]); # tmp[t] <- A[j]; t++; j++;
            j += 1
            cnt += 1
        if cnt == k: print(tmp[-1])
        #print(cnt, k)

    while (i <= q):  # 왼쪽 배열 부분이 남은 경우
        tmp.append(ar[i])
        i +=1
    while (j <= r):  # 오른쪽 배열 부분이 남은 경우
        tmp.append(ar[j])
        j +=1
    print(tmp)
    return tmp

global k
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, (sys.stdin.readline().split())))
cnt = 0
print(merge_sort(lst, 0, n-1))
