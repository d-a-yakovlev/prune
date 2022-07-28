def bubble_sort(a):
    n = len(a)
    all_good = True
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j+1] < a[j]:
                all_good = False
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
        if all_good:
            return a
    return a

arr = list(map(int, input().split()))

arr = bubble_sort(arr)
for a in arr:
    print(a, end = " ")