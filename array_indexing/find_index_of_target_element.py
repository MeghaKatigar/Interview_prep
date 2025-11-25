a = [3, 5, 10, 8, 10, 4, 9]

target_element = int(input("Enter the target element"))

# def search_element(arr, target_element):
#     for i in range (len(arr)):
#         if a[i] == target_element:
#             return i
#     # return -1


def search_element(a, target_element):
    indexs = []
    for i in range(len(a)):
        if a[i] == target_element:
            indexs.append(i)
    return indexs if indexs else -1        

print(search_element(a, target_element))


