arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i == 0 or i == (len(arr) - 1):
#             print(f"{arr[i][j]}", end=" ")
#         elif j == 0 or j==(len(arr[i]) - 1):
#             print(f"{arr[i][j]}", end=" ")

for i in range(len(arr)):
    if i == 0:
        print(f"{arr[i]}")
    elif i == (len(arr) - 1):
        print(f"{arr[i]}")
    else:
        print(f"{arr[i][0], arr[i][-1]}")    



