# Найти в заданном графе количество и состав компонент связности с помощью поиска в ширину (bfs)

input_file = open("test.txt", "r")
graph_nodes_count = int(input_file.readline())
nodes = [[] for i in range(graph_nodes_count)]

while True:
    line = input_file.readline()
    if not line:
        break
    dots = line.split()
    nodes[int(dots[0])].append(int(dots[1]))

visited = []
queue = []
components_count = 0
components = []

def bfs(i):
    visited.append(i)
    component.append(i)
    for j in range(len(nodes[i])):
        rel_node = nodes[i][j] # смежная вершина
        if rel_node not in visited and rel_node not in queue:
            queue.append(rel_node)
    queue.pop(0)


for i in range(len(nodes)):
    if i not in visited:
        components_count += 1
        component = []
        queue.append(i)
        while len(queue):
            bfs(queue[0])
        components.append(component)

print(f'Состав компонент связности: {components}\nИх кол-во: {components_count}')
