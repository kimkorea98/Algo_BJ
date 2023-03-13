divide = 15746
N = int(input())

lst = [0]*((10**6)+1)
lst[0] = 1
lst[1] = 2
for i in range(2, N):
    temp =  lst[i-1] + lst[i-2]
    if temp >=divide: temp = temp%divide
    lst[i] = temp
print(lst[N-1]%divide)
#f(n) = f(n-1)+f(n-2)10000001000

#메모리는 최대한 적게 잡아 먹기 위해 저장하는 값을 미리 나머지 취하자
