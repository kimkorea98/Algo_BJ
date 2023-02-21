import sys
def BFS(graph, start_node):
    visit = []
    queue = []
    #start node에 해당하는 edge에
    queue.append(start_node)
    while queue:
        #0번째 index d pop
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def DFS(graph, start_node):
    visit = []  
    stack = []
    #start node에 해당하는 edge에
    stack.append(start_node)
    while stack:
        #0번째 index d pop
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))
    return visit

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
# #간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
N, M, V= map(int,sys.stdin.readline().split())

g = dict()
for i in range(1, N+1):
    g[i] = []

for _ in range(M):
    n, m = map(int, sys.stdin.readline().split())
    g[n].append(m)
    g[m].append(n)
for i in range(1, N+1):
    g[i].sort()

#print(g)
print(" ".join(map(str, DFS(g, V))))
print(" ".join(map(str, BFS(g, V))))
