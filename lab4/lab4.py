# Поиск кол-ва и состава компонент связности с помощью поиска в глубину (dfs)

def dfs(i):
    component.append(i)
    visited.append(i)
    for j in range(len(nodes[i])):
        if (nodes[i][j]) not in visited:
            dfs(nodes[i][j])


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
components = []
component_count = 0

for i in range(len(nodes)):
    component = []
    if i not in visited:
        dfs(i)
        component_count += 1
    if component:
        components.append(component)

print('Состав компонент связности:', components)
print('Их кол-во:', component_count)
