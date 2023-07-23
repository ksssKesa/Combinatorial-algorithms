from heapq import *


def read_input(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        n = int(file.readline())
        result = {}
        for i in range(1, n + 1):
            line = file.readline().strip().split()
            line.pop()
            if line:
                while line:
                    weight = int(line.pop())
                    vertex = line.pop()
                    result.setdefault(str(i), []).append((weight, vertex))
            else:
                result[i] = line
        graph = {}
        for items, values in result.items():
            graph.setdefault(str(items), [])
            while values:
                weight, vertex = values.pop()
                graph.setdefault(vertex, []).append((weight, items))
        start = file.readline().strip()
        goal = file.readline().strip()
        return graph, start, goal


def write_output(filename, result):
    with open(filename, "w", encoding='UTF-8') as file:
        answer = [str(i) for i in result]
        if answer[0] == 'N':
            answer = ['N']
        file.write('\n'.join(answer))


def djikstra(start, goal, graph):
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited, cost_visited


def get_way(start, goal, visited):
    cur_node = goal
    res = [cur_node]
    while cur_node != start:
        cur_node = visited.get(cur_node)
        if cur_node is None:
            return False
        res.append(cur_node)
    return ' '.join(reversed(res))


graph, start, goal = read_input('in.txt')

visited, cost_visited = djikstra(start, goal, graph)
cost = cost_visited.get(goal)
way = get_way(start, goal, visited)

if cost_visited.get(goal) != None:
    has_way = 'Y'
else:
    has_way = 'N'

result = (has_way, way, cost)
write_output('out.txt', result)
