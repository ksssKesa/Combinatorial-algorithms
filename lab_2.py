def read_input(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        n = int(file.readline())
        result = {}
        for i in range(1, n + 1):
            line = file.readline().strip().split()
            line.pop()
            result[str(i)] = line
        return result


graph = read_input('in.txt')

color = {}
parent = {}
START = 0
FINISH = 0

for u in graph.keys():
    color[u] = 'W'
    parent[u] = None


def dfs(u, color, parent):
    color[u] = 'G'
    for v in graph[u]:
        if color[v] == 'W':
            parent[v] = u
            cycle = dfs(v, color, parent)
            if cycle == True:
                return True
        elif color[v] == 'G' and parent[u] != v:
            global START
            START = v
            global FINISH
            FINISH = u

            return True
    color[u] = 'B'
    return False


def get_way(start, finish, parent, path=[]):
    if parent[finish] == start:
        return path
    path.append(parent[finish])
    finish = parent[finish]
    get_way(start, finish, parent, path=path)
    return path


is_cyclic = False
for u in graph.keys():
    if color[u] == 'W':
        is_cyclic = dfs(u, color, parent)
        if is_cyclic == True:
            break

answer = 'N' if is_cyclic else 'A'

with open('out.txt', "w", encoding='UTF-8') as file:
    file.write(answer)
    if is_cyclic:
        way = [START, FINISH]
        way.extend(get_way(START, FINISH, parent))
        way = sorted(way, key=lambda x: int(x))
        file.write(f'\n{" ".join(way)}')
