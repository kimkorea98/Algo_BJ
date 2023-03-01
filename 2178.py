
N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(arr, x, y, d = 1):
    visit = {}
    queue = []
    i = d
    queue.append([x, y, i])
    while queue:
        node = queue.pop(0)
        x = node[0]
        y = node[1]
       
        if arr[x][y] <2 :
            arr[x][y] = node[2]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0<= ny <M and arr[nx][ny] == 1:
                    queue.append([nx, ny, node[2]+1])
        else:
            if arr[x][y] > node[2]:
                arr[x][y] = node[2]
    return arr

arr =[]
for _ in range(N):
    arr.append(list(map(int, input())))
result =BFS(arr, 0, 0)
print(result[N-1][M-1])