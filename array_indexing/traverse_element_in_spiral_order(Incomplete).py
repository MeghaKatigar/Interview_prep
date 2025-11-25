a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in range(len(a)):
    for j in range(0, len(a[i])):
        if i==0:
            print(f"{a[i][j]}")
        else:
            print(f"{a[j][-1]}")
            continue
