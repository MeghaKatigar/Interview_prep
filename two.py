from datetime import datetime

# O(N2) Solution

"""
def find_target(num, target):
    start_time = datetime.now()
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if (num[i] + num[j]) == target:
                print(f"{num[i], num[j]}")
                end_time = datetime.now()
                print(f"Total Execution forloop in forloop {end_time-start_time}")
            else:
                pass


"""
def find_target(num, target):
    start_time = datetime.now()
    set_data=set(num)
    for i in range(len(num)):
        if num[i] < target:
            if (target - num[i]) in set_data:
                print(f"{num[i], target - num[i]}")
                end_time = datetime.now()
                print(f"Total execution Time {end_time - start_time}")
                break

# def find_target(num, target):
#     i = 0
#     while i < len(num):
#         for j in range(i + 1, len(num)):
#             if (num[i] + num[j]) == target:
#                 print(f"{num[i], num[j]}")
#         i = i + 1


def main():
    print("Enter the array: ", end="")
    numbers = input()

    numbers = list(map(int, numbers.split(" ")))

    target = int(input("Target: "))

    print((numbers))
    print(target)
    find_target(numbers, target)


if __name__ == "__main__":
    main()
