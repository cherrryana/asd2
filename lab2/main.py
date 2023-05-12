# Найти в заданном графе кратчайшие пути из заданной вершины до всех остальных вершин с помощью поиска в ширину (bfs)

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
print('Найти кратчайшие пути от вершины:')
main_node = int(input()) # ввод номера вершины графа, от которой надо найти кратчайшие пути
queue.append(main_node)

short_paths = [[] for i in range(graph_nodes_count)] # список кратчайших путей
short_paths[main_node].append(main_node)

def check_path(this_node, prev_node): # нахождение кратчайшего пути
    if this_node != main_node:
        short_paths[this_node] = short_paths[prev_node].copy()
        short_paths[this_node].append(this_node)

def bfs(i):
    visited.append(i)
    for j in range(len(nodes[i])):
        rel_node = nodes[i][j] # смежная вершина
        if rel_node not in visited and rel_node not in queue:
            check_path(rel_node, i)
            queue.append(rel_node)
    queue.pop(0)

while len(queue):
    bfs(queue[0])

for i in range(len(short_paths)):
    print(f'От {main_node} до {i}: {short_paths[i]}')