def create_multiplication_table(rows, cols):
    
    table = []
    for i in range(1, rows + 1):
        row = [i * j for j in range(1, cols + 1)]
        table.append(row)
    return table

def display_multiplication_table(table):
    
    for row in table:
        print(' '.join(f'{val:3}' for val in row))
