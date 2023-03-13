from collections import deque

arr = [0]*101
N, M = map(int, input().split())
in_list = []
out_list = []
for _ in [0]*(N+M):
    x, y = map(int, input().split())
    in_list.append(x)
    out_list.append(y)

def BFS(start_node):
    queue = deque()
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        for i in range(1,7):
            n = node + i
            if 0 <= n < 101 and arr[n]==0:
                for idx, val in enumerate(in_list):
                    if val == n:
                        arr[n] = arr[node]+1
                        if 0 <= out_list[idx] < 101 and arr[out_list[idx]]==0:
                            arr[out_list[idx]] = arr[node] + 1
                            queue.append(out_list[idx])
                        break #여기서 break를 통해 아래 else문을 건너 뛸 수 있음 이를 통해 사다리, 뱀 이동에 대한 append 제거 가능
                else:
                        arr[n] = arr[node] + 1
                        queue.append(n)
BFS(1)
print(arr[-1])


