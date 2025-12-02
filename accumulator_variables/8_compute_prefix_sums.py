import time

def prefix_sum(a):
    b = [a[0]]  # Add the first element
    for i in range(1, len(a)):
        b.append(b[i-1] + a[i])
    return b

def prefix_sum_slow(a):
    b = []
    for i in range(1, len(a) + 1):
        b.append(sum(a[0:i]))
    return b

# Test function
def time_function(func, a):
    start_time = time.time()
    func(a)
    end_time = time.time()
    return end_time - start_time

# Test with a small example
print("Test with a small input list:")
a_small = [1, 2, 3, 4, 5]

print(f"Testing prefix_sum with small input...")
time_taken = time_function(prefix_sum, a_small)
print(f"Time taken by prefix_sum: {time_taken:.6f} seconds")

print(f"Testing prefix_sum_slow with small input...")
time_taken = time_function(prefix_sum_slow, a_small)
print(f"Time taken by prefix_sum_slow: {time_taken:.6f} seconds")

# Test with a larger list to see the performance difference
print("\nTest with a larger input list:")
a_large = list(range(1, 1001))  # A list of 1000 numbers

print(f"Testing prefix_sum with large input...")
time_taken = time_function(prefix_sum, a_large)
print(f"Time taken by prefix_sum: {time_taken:.6f} seconds")

print(f"Testing prefix_sum_slow with large input...")
time_taken = time_function(prefix_sum_slow, a_large)
print(f"Time taken by prefix_sum_slow: {time_taken:.6f} seconds")
