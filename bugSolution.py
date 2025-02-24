def my_function_iterative(x):
    result = 0
    for i in range(1, x + 1):
        result += i
    return result

# Or using the sum function:
def my_function_sum(x):
    return sum(range(1, x + 1))