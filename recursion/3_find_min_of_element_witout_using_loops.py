a = [678, 34, 66, 90, 23, 90, 12, 10, 44]


def min_element(a, b = a[0], i=1):
    min = b
    if i == len(a): 
        return min
    elif b > a[i]:
        min = a[i]
    elif b < a[i]:
        min = b    
    return min_element(a, min, i+1)


print(min_element(a))
