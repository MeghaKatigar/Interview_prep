a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start_indice = int(input("Enter the start indice"))
end_indice = int(input("Enter the end indice"))

sum = 0
for i in range(start_indice, end_indice + 1):
    sum += a[i]

print(sum)
