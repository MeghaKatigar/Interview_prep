arr = [1, 4, 9, 10, 12, 0, 78]
min = arr[0]
max = arr[0]

for i in range(1, len(arr)):
    if min > arr[i]:
        min = arr[i]
    elif max < arr[i]:
        max = arr[i]

print(f"min = {min}, max = {max}")
