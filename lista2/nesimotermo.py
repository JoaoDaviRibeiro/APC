def compare_lists(a, b, t):
    if a[t] != b[t]:
        return a[t] - b[t]
    else:
        return sum(a) - sum(b)

n = int(input())
t = int(input())

lists = []
for _ in range(n):
    lst = list(map(int, input().split()))
    lists.append(lst)

sorted_lists = sorted(lists, key=lambda x: (x[t], sum(x)))

for lst in sorted_lists:
    print(*lst)


