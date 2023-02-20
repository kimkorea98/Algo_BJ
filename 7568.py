
## 1 2 3 4 5 
#w 4 3 1 2 5  
#h 2 3 1 4 5 


import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    lst.append((w, h))

cnt = 1
rank = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if lst[i][0]< lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    rank.append(cnt)
print(*rank, sep= ' ')

#그냥 노가다로 풀면되는데 왜 고생했지....다른 방법이 있었을까?
#브루트포스의 성립 조건이 무엇일까? 