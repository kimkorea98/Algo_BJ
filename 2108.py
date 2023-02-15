import sys
n = int(input())
lst =[]
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()
count = {}
min = lst[0]
max = lst[-1]
total = 0

for i in range(n):
    total += lst[i]
    try: count[lst[i]] += 1
    except: count[lst[i]] =1
print(int(round(total/n, 0)))
print(lst[n//2])
count = sorted(count.items(), key = lambda item: item[1], reverse=True)
#print(count)
if n ==1:
    print(lst[0])
    print(0)
else:
    if count[0][1] == count[1][1]: print(count[1][0])
    else: print(count[0][0])
    print(max-min)


#반올림은 round
#sort() 원본 정령
#sorted(lst) 새로운 정렬 리스트 생성
#dict 정렬
#count = sorted(count.items(), key = lambda item: item[1], reverse=True)





