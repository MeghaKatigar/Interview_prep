a = [1, 2, 4, 5, 8, 10]
b = []

for i in range(1, len(a)+1):
    b.append(sum(a[0:i])
    )

print(b)