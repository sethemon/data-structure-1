from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(dict)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for source, destination in connections:
            self.add(source, destination)

    def add(self, source, destination):
        """ Add connection between node1 and node2 """
        for key, value in destination.items():
            if key not in self._graph:
                self._graph[key] = dict()
            if key in self._graph[source]:
                self._graph[source] = dict((key, [v[0], value[0]]) for k, v in self._graph[source].items())
            else:
                self._graph[source].update(destination)
        if not self._directed:
            for src, train in destination.items():
                if source in self._graph[src]:
                    self._graph[src] = dict((source, [v[0], train[0]]) for k, v in self._graph[src].items())
                else:
                    self._graph[src][source] = train

    def find_hub(self):
        """ Find the largest city/train hub"""
        train_list = []
        largest = dict()
        size = 1
        for src, des in self._graph.items():
            if len(des.keys()) > size:
                size = len(des.keys())
                largest['hub'] = src
                largest['size'] = len(des.keys())
                for k, v in des.items():
                    train_list.append(v[0])
        largest['trains'] = train_list
        return largest

    def remove(self, node):
        """ Remove all references to node """
        print(f"Deleting {node} ...")
        for src, des in self._graph.items():
            try:
                des.pop(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, source, destination):
        """ Check if source is directly connected to destination """
        print(f"{source} -> {destination}")
        if source in self._graph and destination in self._graph[source]:
            for key, val in self._graph[source].items():
                if key == destination:
                    print(f"Package can be sent directly: Yes, {val[0]}")
                    return f"{source} is connected to {key} via {val[0]}"
        else:
            print(f"Package can be sent directly: No")
            return f"{source} is not directly connected to {destination}"

    def find_path(self, source, destination, path: list):
        """ Find shortest path between source and destination (return path and connecting Train) """
        path = path + [source]
        if source == destination:
            return path
        if source not in self._graph:
            return None
        shortest = None
        # for node, value in self._graph[source].items():
        for node in self._graph[source]:
            # print(f"{source} >> {value} >> {node}")
            if node not in path:
                new_path = self.find_path(node, destination, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    @property
    def get_graph(self):
        return self._graph
