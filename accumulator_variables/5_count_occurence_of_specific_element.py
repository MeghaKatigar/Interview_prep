a = [1, 2, 4, 9, 3, 2, 1]

target_element=int(input("Enter Target Element "))
count=0
for i in a:
    print(i)
    if i == target_element:
        count +=1

print(f"The total occurence of element {target_element} is {count} ")