# Реализовать алгоритм Беллмана-Форда поиска кратчайших путей из одной вершины

def BellmanFord(edges, num, start):
    distance = [11**11] * num
    distance[start - 1] = 0
    cycle = False

    for k in range(num):
        for i, j in edges.keys():
            if distance[i - 1] + edges[i, j] < distance[j - 1]:
                distance[j - 1] = distance[i - 1] + edges[i, j]

    for i, j in edges.keys():
        if distance[i - 1] + edges[i, j] < distance[j - 1]:
            cycle = True
            break

    return "cycle" if cycle else distance


edges = {(1, 2): 2, (2, 1): 2, (1, 3): 5, (3, 2): -4, (2,4): 2}
start = 1
result = BellmanFord(edges, 4, start)
for i in range(len(result)):
    print(f'Кратчайший путь от {start} до {i + 1} = {result[i]}')

edges = {(1, 2): 2, (2, 1): 2, (1, 3): 5, (3, 2): -4, (2,4): 2, (4, 3): -11}
print(f'\n{BellmanFord(edges, 4, 1)}')
