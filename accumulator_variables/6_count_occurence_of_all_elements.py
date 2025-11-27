from collections import Counter

a = [1, 8, 3, 8, 9, 10, 11, 17, 19, 13, 13, 16]
# count = 0

# print(Counter(a))
dict = {}

# for i in a:
#         dict[i] = a.count(i)
# print(dict)

# for i in a:
#     if i in dict:
#         value =  dict[i]   
#         dict[i] = value + 1
#     else:
#         dict[i] = 1
            
# print(dict)

for i in a:
    dict[i]=dict.get(i, 0) + 1

print(dict)    



