
'''
n,m=map(int,input().split())
g=[[*input()]for _ in[0]*n]
print(g)

'''
'''

a, b, *c= range(10)

print(a, b, *c) 

def product(*numbers):
    p = reduce(lambda x, y: x * y, numbers)
    return p
'''

#print([[i for i in [0]*4] for _ in [0]*3 ])

import sys
def BFS2(arr, node):
    queue = []
    queue.append(node)
    while queue:
        point = queue.pop(0)
        x = point[0]
        y = point[1]
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if  0 <= nx < M and 0 <= ny <N and arr[nx][ny] == 1:
                queue.append([nx, ny])
    return 1


T  = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
for _ in [0]*T:
    M, N, K  = map(int, sys.stdin.readline().split())
    arr = [[0]*N for _ in [0]*M]
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
  