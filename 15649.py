import sys
def back_tracking(arr, M):
    result = []
    for i in arr:
        if len(arr)>= M and M != 0:
            sub_arr=arr.copy()
            sub_arr.remove(i)
            result.append([ i, back_tracking(sub_arr, M-1)])
    return result

def print_arr(arr, s, M):
    for i in range(len(arr)): 
        if ((len(s)+3)//2) < M:
            print_arr(arr[i][1], s+str(arr[i][0])+' ', M)
        else:
            print(s + str(arr[i][0]))

N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N+1))

result = back_tracking(arr, M)
print_arr(result, '', M)


'''
n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
'''