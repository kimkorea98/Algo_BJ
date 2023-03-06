Max = 10 ** 5
N, K = map(int, input().split())
arr =[0]*(Max + 1)


def Search(arr, start):
    queue = [start]
    arr[start] = 0
    while queue:
        node = queue.pop(0) #queue.popleft()
        if node == K:
            return arr[node]
        else:
            for nx in (node-1, node +1, 2*node ):
                if 0<= nx <=Max and not arr[nx]:
                    queue.append(nx)
                    arr[nx] = arr[node]+1
    
print(Search(arr, N))