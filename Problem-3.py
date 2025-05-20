def generate_series(a):
    result = []
    for i in range(1, 2 * a):
        if i % 2 == 1:
            result.append(i)
    return result[:a if a % 2 == 1 else a - 1]

# Example usage
a = int(input("Enter a: "))
print(generate_series(a))
