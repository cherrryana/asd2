# Реализовать алгоритм Прима нахождения минимального покрывающего дерева

matrix = [[0, 7, 8, 0, 0, 0],
          [7, 0, 11, 2, 0, 0],
          [8, 11, 0, 6, 9, 0],
          [0, 2, 6, 0, 11, 9],
          [0, 0, 9, 11, 0, 10],
          [0, 0, 0, 9, 10, 0]]

def findEdges(current_node, edges, visited, matrix):
    for i in range(len(matrix[current_node])):
        weight = matrix[current_node][i]

        if weight != 0 and i not in visited:
            edges.append([current_node, i, weight])

def findMin(edges, visited, result_tree):
    min_edge = [0, 0, 1111]

    for edge in edges:
        if edge[0] not in visited or edge[1] not in visited:   # если не образуется цикл
            if edge[2] < min_edge[2]:
                min_edge = edge.copy()

    result_tree.append(min_edge)

    if min_edge[0] in visited:
        return min_edge[1]
    else:
        return min_edge[0]


def primAlgorithm(matrix, i):
    visited = []
    edges = []
    result_tree = []

    current_node = 0
    visited.append(current_node)

    while len(visited) != i:
        findEdges(current_node, edges, visited, matrix)        # находим все ребра, инцидентные рассматриваемой вершине
        current_node = findMin(edges, visited, result_tree)    # находим ближайшую вершину к любой из посещенных
        visited.append(current_node)

    return result_tree

result = primAlgorithm(matrix, len(matrix))
print('Минимальное остовное дерево:\n')
for i in result:
    print(f'Ребро: {i[0]} --- {i[1]}, его вес: {i[2]}')
