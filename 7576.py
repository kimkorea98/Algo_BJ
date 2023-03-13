import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in [0]*M]

tmt = deque()
rooten = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            tmt.append((i, j))
        if  arr[i][j] == -1:
            rooten.append((i, j))
cnt =0
while tmt:
    node = tmt.popleft()
    cnt +=1
    for i in range(4):
        nx = node[0] + dx[i]
        ny = node[1] + dy[i]
        if 0 <= nx < M and 0<= ny < N and arr[nx][ny] == 0:
            tmt.append((nx, ny))
            arr[nx][ny] = arr[node[0]][node[1]] + 1

if len(rooten)+cnt != N*M:
    print(-1)
else:
    print(arr[node[0]][node[1]]-1)

#list.pop을 쓰는 것보다 deque.popleft를 써야한다. 좀 배신감이네...
#deque는 양방향 queue로 append, pop 뿐만 아닌 양 끝 모든 element에 대해 O(n)의 시간복잡도를 갖는다
