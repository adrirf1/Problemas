matrix = [
    [0,1,0,0],
    [1,0,1,1],
    [0,1,0,1],
    [0,1,1,0]
    ]

def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2]

print(is_adjacent(matrix,2,3))
