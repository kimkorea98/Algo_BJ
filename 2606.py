import sys
import time

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


def BFS(graph, start_node):
    visit = []
    queue = []
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
            #print(len(queue))
    return visit


n = int(sys.stdin.readline())
e = int(sys.stdin.readline())

start = time.time()

g = dict()
for i in range(1, n+1):
    g[i] = []

for _ in range(e):
    e1, e2 = map(int, sys.stdin.readline().split())
    g[e1].append(e2)
    g[e2].append(e1)

result = BFS(g, 1)
print(len(result)-1)

end = time.time()
#print(f"{end-start:.5f} sec")
