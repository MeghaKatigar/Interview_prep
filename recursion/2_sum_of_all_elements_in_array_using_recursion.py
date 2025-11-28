a = [1, 2, 3, 4, 5, 6, 7, 8]

def sum_of_an_array(n):
    if not n:
        return 0
    return n[0] + sum_of_an_array(n[1::])

print(sum_of_an_array(a))



#Another way
def sum_of_array(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_of_array(arr, i + 1)
