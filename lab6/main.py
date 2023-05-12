# Реализовать алгоритм Крускала нахождения минимального покрывающего дерева

graph = []

with open('matrix.txt') as file:
    i = 0
    for line in file:
        Edges = list(map(int, line.split()))

        for j in range(len(Edges)):
            if Edges[j] != 0 and i != j:
                edge = [Edges[j], set([i, j])]
                if edge not in graph:
                    graph.append(edge) # отдельное ребро в графе будет иметь вид [weight, {i, j}]
        i += 1

def weightSort(x):
    return x[0]

graph.sort(key = weightSort) # сортируем по весу

def KruskalAlgorithm(graph):
    result_nodes = []
    result_tree = []

    for edge in graph:
        num_nodes = []  # список "номеров" множеств, которые содержат вершины ребра edge (<= 2)
        cycle = 0

        for j in range(len(result_nodes)):
            if edge[1].issubset(result_nodes[j]):  # если обе вершины ребра содержатся во множестве выбранных вершин, появляется цикл -> никуда не добавляем ребро
                cycle = 1
                break

            elif (len(result_nodes[j].intersection(edge[1])) == 1):  # если одна из вершин ребра содержится во множестве выбранных вершин ->
                # объединяем эти множества, добавляем порядковый номер множества в список
                result_nodes[j].update(edge[1])
                num_nodes.append(j)

        # если ребро имеет вершины в обоих множествах - объединяем их, удаляя одно из них
        if len(num_nodes) == 2:
            result_nodes[num_nodes[0]].update(result_nodes[num_nodes[1]])
            result_nodes.pop(num_nodes[1])

        # если ни одно из множеств не содержит ни одну вершину ребра -> создается новое множество
        elif len(num_nodes) == 0 and cycle != 1:
            result_nodes.append(edge[1])

        if not cycle:
            result_tree.append([edge[0], edge[1].copy()])

    return result_tree


result = KruskalAlgorithm(graph)
print('Минимальное остовное дерево:\n')
for i in result:
    print(f'Ребро: {i[1]}, его вес: {i[0]}')