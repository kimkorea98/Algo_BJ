# 유클리우드 호제법
# GCD(A, B) -> GCD(B, A%B)
#if A%B = 0 -> GCD = B
#else GCD(B, A%B)


def GCD(A, B):
    if A%B == 0 :
        return B
    else : 
        return GCD(B, A%B)


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    
    print(int(A*B/GCD(A, B)))
