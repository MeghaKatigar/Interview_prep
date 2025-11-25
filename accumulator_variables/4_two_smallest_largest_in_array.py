arr = [2, 5, 7, 2, 9, 0]
smallest_1, smallest_2 = arr[0], arr[1]
largest_1, largest_2 = arr[0], arr[1]
for i in range(2, len(arr)):
    if smallest_1 > arr[i]:
        smallest_2 = smallest_1
        smallest_1 = arr[i]
    elif largest_1 < arr[i]:
        largest_2 = largest_1
        largest_1 = arr[i]


print(f" 1st largest : {largest_1}, 2nd largest : {largest_2}")
print(f" 1st smallest : {smallest_1}, 2nd largest : {smallest_2}")
