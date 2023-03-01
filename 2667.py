dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())

def BFS(arr, start_node):
    queue = [start_node]
    cnt = 0
    arr[start_node[0]][start_node[1]] = 0
    while queue:
        cnt += 1
        node = queue.pop(0)
        for i in range(4):
            nx = node[0] + dx[i] 
            ny = node[1] + dy[i] 

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0
    return cnt


arr = [list(map(int, [*input()])) for _ in [0]*N] # 이거 쓰는게 너무 섹시해

#for i in range(N):print(arr[i])
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            result.append(BFS(arr, (i, j)))
print(cnt)
result.sort()
for v in result: print(v) 
if not result: # empty check
    print(0)
#for i in range(N):print(arr[i])

#join은 문자열로 되어 있는 배열에만 가능


