a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prefix_sum = []

for i in range(1, len(a) + 1):
    prefix_sum.append(sum(a[0:i]))

# print(prefix_sum)
i=10
while(i):
    start_indice = int(input(" Enter the start of the indice :"))
    end_indice = int(input("Enter the end indice :"))

    if start_indice == 0 or end_indice == 0:
        print(prefix_sum[end_indice])

    elif (len(a) - 1) not in (start_indice, end_indice) :
        print("Index out of range")
    else:
        print(prefix_sum[end_indice]-prefix_sum[start_indice-1])
    i -= 1
