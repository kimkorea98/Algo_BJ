value = input()
l = len(value)
lst = []
for i in range(l):
    lst.append(value[i])
lst =list(map(int, lst))
lst.sort(reverse=True)
ans = ''
for i in range(l):
    ans += str(lst[i])
print(ans)