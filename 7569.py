from collections import deque
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]



M, N, H = map(int, input().split())

def BFS(lst):
    queue = lst
    temp = deque()
    while queue:
        node = queue.popleft()
        for i in range(6):
            nx = node[2] + dx[i]
            ny = node[1] + dy[i]
            nz = node[0] + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = 1
                temp.append((nz, ny, nx))
    return temp

dque = deque()
arr = [[list(map(int, input().split())) for i in [0]*N] for j in [0]*H]
check =0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                dque.append((i, j, k))
                
cnt =-1
while dque:
    cnt +=1
    dque=BFS(dque)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                break
        if arr[i][j][k] == 0:
            break
    if arr[i][j][k] == 0:
        print(-1)
        break
else:
    print(cnt)