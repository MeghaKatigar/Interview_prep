def solution(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizz-buzz, ", end="")
        elif i % 3 == 0:
            print("fizz, ", end="")
        elif i % 5 == 0:
            print("buzz, ", end="")
        else:
            print(f"{i}, ", end="")
    print("\b\b ")


def main():
    limit = int(input("Enter a number:"))
    solution(limit)
    print("")


if __name__ == "__main__":
    main()
