arr = [1, 4, 9, 10, 12, 0, 78, -1]
min = arr[0]
max = arr[0]
min_index = 0
max_index = 0

for i in range(1, len(arr)):
    if min > arr[i]:
        min = arr[i]
        min_index = i
    elif max < arr[i]:
        max = arr[i]
        max_index = i
print(f"min_indice = {min_index}, max_indice = {max_index}")
