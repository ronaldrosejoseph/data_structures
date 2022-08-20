'''

    3  -> 4
    ^
    |
    0  -> 1
    |    |
    -    -
    2 -> 5

'''


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_val = {}

        for start, end in self.edges:
            if start in self.graph_val:
                self.graph_val[start].append(end)
            else:
                self.graph_val[start] = [end]

        print(self.graph_val)

    def get_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_val:
            return []

        paths = []
        for node in self.graph_val[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)

                if new_paths and len(new_paths) > 0:
                    paths += new_paths

        return paths


if __name__ == '__main__':
    pipes = [
        (0, 1),
        (0, 2),
        (0, 3),
        (3, 4),
        (2, 5),
        (1, 5),
    ]

    graph_obj = Graph(pipes)
    print(graph_obj.get_path(0, 5))
