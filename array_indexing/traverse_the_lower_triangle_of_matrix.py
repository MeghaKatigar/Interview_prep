arr = [[1, 2, 3, 4], [1, 1, 2, 2], [1, 1, 1, 2]]

for i in range(len(arr)):
    for j in range(i+1):
        print(f"{arr[i][j]}" , end = "")
    print("")    