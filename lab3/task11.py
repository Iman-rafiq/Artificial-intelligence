def generate_array(m, n):
    array = [[i * j for j in range(n)] for i in range(m)]
    return array

rows, cols = 3, 4
print("Generated array:", generate_array(rows, cols))