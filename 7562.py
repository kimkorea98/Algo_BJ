dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(arr, start, end):
    queue = [start]
    arr[start[0]][start[1]]
    while queue:
        node = queue.pop(0)
        if node == end:
            return arr[node[0]][node[1]]
        for i  in range(8):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0<= nx < I and 0 <= ny < I and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = arr[node[0]][node[1]] + 1


for _ in [0]*int(input()):
    I = int(input())
    board = [[0]*I for _ in [0]*I]

    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    print(BFS(board, (sx, sy), (ex, ey)))