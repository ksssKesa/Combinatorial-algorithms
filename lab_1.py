"""
Для того чтобы разделить двудольный граф на доли на Python,
можно воспользоваться алгоритмом двухцветной раскраски.
Он заключается в том, чтобы раскрасить вершины графа в два цвета так,
чтобы каждое ребро соединяло вершины разных цветов.
"""


# 1. Необходимо выбрать произвольную вершину из графа и раскрасить ее в первый цвет.

# 2. Раскрасить все вершины, смежные с этой, во второй цвет.

# 3. Далее, необходимо итеративно
# повторить процедуру для каждой вершины второго цвета,
# раскрашивая ее соседние вершины в первый цвет.

# 4. Если на каком-то шаге при раскраске вершины возникает конфликт,
# то граф не является двудольным, и разделение на доли невозможно.

# 5. В результате работы алгоритма получаются две доли графа,
# каждая из которых содержит вершины одного цвета.

def is_bipartite(graphh, start):
    color = {}
    queue = [start]
    color[start] = 0

    while queue:
        vertex = queue.pop()
        for neighbor in graph[vertex]:
            if neighbor not in color:
                color[neighbor] = 1 - color[vertex]
                queue.append(neighbor)
            elif color[neighbor] == color[vertex]:
                return False, {}
    return True, color  # {'5': 0, '2': 1, '4': 0, '3': 1, '1': 0}


def bipartite_partition(G):
    if G:
        color = is_bipartite(G, '1')[1]
    result = {1: [], 0: []}
    for v, c in color.items():
        result[c].append(v)

    first = sorted(result[0], key=lambda x: int(x))
    second = sorted(result[1], key=lambda x: int(x))
    if '1' in first:
        return first, second
    else:
        return second, first


# считывает файл и возвращает
# n - общее кол-во вершин
# matrix - смежную матрицу графа вложенными списками
def read_input(filename):
    result = []
    with open(filename) as file:
        while line := file.readline():
            result.append(line.rstrip())

    n = int(result[0])

    matrixx = []
    for line in result[1:]:
        lst_int = [int(x) for x in line.split(" ")]
        matrixx.append(lst_int)

    return n, matrixx


def write_output(filename):
    with open(filename, "w") as file:
        file.write(output)


# функция преобразующая матрицу смежности графа
# в хеш таблицу вида '1': set(['2', '3']
def matrix_to_graph(nodes, matrixx):
    g = {}
    for m in range(0, nodes):
        a = []
        for i, el in enumerate(matrixx[m]):
            if el == 1:
                a.append(str(i + 1))

        g[str(m + 1)] = set(a)

    return g


if __name__ == '__main__':

    # читаем файл "in.txt" и получаем матрицу
    n, matrixx = read_input("in.txt")

    # преобразуем матрицу в граф
    graph = matrix_to_graph(n, matrixx)

    output = ""
    # проверяем граф на двудольность
    # и записываем результат в строку output
    first, second = bipartite_partition(graph)
    if not first or not second:
        output += "N"
    else:
        output += "Y\n"
        output += " ".join(first) + "\n"
        output += " ".join(second)

    # записываем ответ
    write_output("out.txt")
