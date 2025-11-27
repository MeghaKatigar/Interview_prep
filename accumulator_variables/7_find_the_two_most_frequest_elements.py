a = [1, 8, 3, 8, 9, 10, 11, 17, 19, 13, 13, 16, 8]

dict = {}
first_most_frequent = 0
second_most_frequent = 0
first_most_count =0 
second_most_count=0

for i in a:
    if i in dict:
        value =  dict[i]   
        dict[i] = value + 1
    else:
        dict[i] = 1


for key, value in dict.items():
    if value >= first_most_frequent:
        second_most_frequent = first_most_frequent
        first_most_frequent = key
    elif value>second_most_frequent:
        second_most_frequent=key

print(first_most_frequent)
print(second_most_frequent)