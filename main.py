# Реализовать алгоритм Дейкстры поиска кратчайших путей из одной вершины

matrix = [[0, 3, 1, 5, 0, 0, 0],
         [3, 0, 0, 0, 6, 7, 0],
         [1, 0, 0, 0, 2, 0, 0],
         [5, 0, 0, 0, 0, 0, 32],
         [0, 6, 2, 0, 0, 8, 17],
         [0, 7, 0, 0, 8, 0, 10],
         [0, 0, 0, 0, 17, 10, 0]]


def findMin(current_node, matrix, visited):
    min = 1111
    index_min = 0

    for i in range(len(matrix[current_node])):
        weight = matrix[current_node][i]
        if i not in visited and weight != 0:
            if weight < min:
                min = weight
                index_min = i

    return index_min


def dijAlgorithm(current_node, matrix):
    visited = []
    short_path = [[1111, ''] for i in range(len(matrix))]
    short_path[current_node] = [0, '']  # короткий путь из заданной вершины в нее саму же

    while len(visited) != len(short_path):  # пока все вершины не окажутся пройденными

        for i in range(len(matrix[current_node])):
            if not matrix[current_node][i] == 0 and i not in visited:
                weight = matrix[current_node][i]

                if short_path[i][0] > weight + short_path[current_node][0]:  # если метка соседней вершины > вес текущего ребра + метка текущей вершины
                    short_path[i][1] = short_path[current_node][1] + (str(current_node) + ' ')
                    short_path[i][0] = weight + short_path[current_node][0]  # обновляем значение метки (длину кратчайшего пути)

        visited.append(current_node)
        current_node = findMin(current_node, matrix, visited)

    return short_path


print('Найти кратчайшие пути от вершины:')
node = int(input())
result = dijAlgorithm(node, matrix)

print(f'Расстояния от вершины {node} до:\n')
for i in range(len(result)):
    print(f'{i}: длина = {result[i][0]}, путь: {result[i][1]}{i}')