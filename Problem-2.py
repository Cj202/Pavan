def generate_series(a):
    series = [2 * i + 1 for i in range(a)]
    return series

# Example usage
a = int(input("Enter a: "))
print(generate_series(a))
