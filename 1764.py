import sys
import time
import math

N, M = map(int, sys.stdin.readline().split())
start = time.time()
n_list = [sys.stdin.readline().strip() for i in range(N)]
m_list = [sys.stdin.readline().strip() for i in range(M)]

union =list(set(n_list) & set(m_list))
union.sort()
print(len(union))
for i in union:
    print(i)
end = time.time()
#print(f"{end-start:.5f} sec")