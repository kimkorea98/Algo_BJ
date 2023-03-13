
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

'''
dx, dy를 활용함으로 코드를 깔끔하게 만들 수 있음
 input으로 들어오는 것은 무조건 STR, 비교를 하든 사용하는 이점 유의하자
 문자열 숫자는 map을 활용하며 구분된 list로 구현 가능 
'''