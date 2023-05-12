# Найти в заданном орграфе количество и состав сильно связных компонент с помощью поиска в глубину
# Алгоритм Косарайю

input_file = open("test.txt", "r")
graph_nodes_count = int(input_file.readline())
nodes = [[] for i in range(graph_nodes_count)]

while True:
    line = input_file.readline()
    if not line:
        break
    dots = line.split()
    nodes[int(dots[0])].append(int(dots[1]))

# dfs, пока не будут «помечены» все вершины (вершина считается «помеченной», когда ей присвоено время выхода из рекурсии)

visited = [0 for i in range(graph_nodes_count)]
time = 0

def dfs(i, time):
    time += 1
    visited[i] = time
    for j in range(len(nodes[i])):
        if visited[nodes[i][j]] == 0:
            time = dfs(nodes[i][j], time)
    visited[i] = time
    return (time + 1)

for i in range(len(nodes)):
    if visited[i] == 0:
        time = dfs(i, time)

# инвертирование ребер графа

nodes_inverted = [[] for i in range(graph_nodes_count)]
for i in range(len(nodes)):
    for j in range(len(nodes[i])):
        nodes_inverted[nodes[i][j]].append(i)

# dfs в порядке убывания меток вершин (для инвертированного графа)
component_count = 0
components = []
visited_inv = []

def dfs_inv(i):
    component.append(i)
    visited_inv.append(i)
    for j in range(len(nodes_inverted[i])):
        if (nodes_inverted[i][j]) not in visited_inv:
            dfs_inv(nodes_inverted[i][j])

for i in range(len(visited)):
    i = visited.index(max(visited))
    visited[i] = 0
    component = []
    if i not in visited_inv:
        dfs_inv(i)
        component_count += 1
    if component:
        components.append(component)

print(f'Компоненты сильной связности: {components} \nИх кол-во: {component_count}')