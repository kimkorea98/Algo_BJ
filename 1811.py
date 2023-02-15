n= int(input())
lst = []
while(n):
    lst.append(input())
    n -= 1
lst = list(set(lst))
lst.sort()
new_lst = []
for i in range(1, 51):
    for j in range(len(lst)):
        if len(lst[j]) == i :
            new_lst.append(lst[j])

for i in range(len(lst)):
    print(new_lst[i])

#중복은 SET으로 없애기
#알파벳 정렬은 길이를 고려하지 않음