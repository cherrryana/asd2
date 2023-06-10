# Реализовать алгоритм нахождения эйлерова цикла в неориентированном графе, заданном матрицей смежности

def check_path_cycle(graph, max_node):
    degree = 0
    node = -1

    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:
            degree += 1
            node = i

    if degree == 0:
        return 1, node
    if degree == 2:
        return 2, node
    return 3, node

def dfs(u, graph, visited, path = []):
    path = path + [u]
    for v in graph[u]:
        if not visited[u][v]:
            visited[u][v], visited[v][u] = True, True
            path = dfs(v, graph, visited, path)
    return path

def euler(graph, max_node):
    visited = [[False for i in range(max_node + 1)] for i in range(max_node + 1)]
    check, node = check_path_cycle(graph, max_node)
    if check == 3:
        print("Не эйлеров:")
        return

    start = 1
    if check == 2:
        start = node
        print("Эйлеров путь:")

    if check == 1:
        print("Эйлеров цикл:")

    return dfs(start, graph, visited)


n = 10
graph = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3], 5: []}

print(euler(graph, n))
