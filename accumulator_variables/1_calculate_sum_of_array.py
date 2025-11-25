a = [1, 2, 3, 4]
# print(sum(a))

i=len(a)
sum=0
while (i):
    sum = sum + a[i-1]
    i-=1

print(sum)