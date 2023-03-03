import sys
import time
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS2(arr, node):
    queue = [node]
    arr[node[0]][node[1]] = 0 #
    
    while queue:
        point = queue.pop(0)
        x = point[0]
        y = point[1]
        #arr[x][y] = 0 #여기에 넣으면 시간초과 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if  0 <= nx < M and 0 <= ny <N and arr[nx][ny] == 1:
                queue.append([nx, ny])
                arr[nx][ny] = 0 #무조건 여기에 넣어야된다는데? -> 모든 배열리 1로 표기 되어 있을때는 큐에 중복해서 들어갈 수 있음
        
    return 1


T  = int(sys.stdin.readline())
start = time.time()
for _ in [0]*T:
    
    M, N, K  = map(int, sys.stdin.readline().split())
    arr = [[i for i in [0]*N] for _ in [0]*M]
    node = []
    for _ in [0]*K:
        x, y  = map(int, sys.stdin.readline().split())
        arr[x][y] = 1
        node.append([x, y])
    
    cnt = 0
    for point in node:
        if arr[point[0]][point[1]] == 1:
            BFS2(arr, point)
            cnt +=1
    print(cnt)
print(time.time()-start)
    #print(BFS(arr,node))

# 그룹화 하는데 내부에 WHILE문을 추가로 넣는 것만으로도 충분히 가능했는데 이것 때문에 고민을 너무 많이 함ㅠ
#asterisk를 활용한 unpacking 매우 중요함!
#[in for _ i [0]*n] 이것도 잘 사용하면 좋을 듯
#풀이 보니까 방문 처리로 0하는 것이 더 좋고 dfs를 여러번 돌리는 게 좋을 듯
#

