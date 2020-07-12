from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(dict)
        self._directed = directed
        self.add_connections(connections)
        self.counter = 0

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for source, destination in connections:
            self.add(source, destination)

    def add(self, source, destination):
        """ Add connection between node1 and node2 """
        for des, train in destination.items():
            if des not in self._graph:
                self._graph[des] = dict()
            if des in self._graph[source]:
                for k, v in self._graph[source].items():
                    if k == des and train[0] not in v:
                        v.append(train[0])
            else:
                self._graph[source].update(destination)
        if not self._directed:
            for src, train in destination.items():
                if source in self._graph[src]:
                    for k, v in self._graph[source].items():
                        if k == source and train[0] not in v:
                            v.append(train[0])
                else:
                    self._graph[src].update({source: train})

    def find_hub(self):
        """ Find the largest city/train hub"""
        counter = 0
        largest = dict()
        train_list = []
        max_key, max_value = max(self._graph.items(), key=lambda x: len(set(x[1])))
        counter = counter + len(self._graph.keys())
        for src, des in max_value.items():
            counter += 1
            for train in des:
                train_list.append(train)

        largest['hub'] = max_key
        largest['trains'] = set(train_list)
        largest['size'] = len(set(train_list))
        largest['counter'] = counter
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
        # print(f"{source} -> {destination}")
        counter = 0
        if source in self._graph and destination in self._graph[source]:
            for key, val in self._graph[source].items():
                if key == destination:
                    counter += 1
                    # print(f"{source} is connected to {key} via {val[0]}")
                    return f"Package can be sent directly: Yes, {val[0]}", counter
        else:
            counter += 1
            # print(f"Package can be sent directly: No")
            return f"{source} is not directly connected to {destination}. Package cannot be sent directly.", counter

    def find_path(self, source, destination, path: list):
        """ Find shortest path between source and destination (return path and connecting Train) """
        path = path + [source]
        if source == destination:
            return path
        if source not in self._graph:
            return None
        shortest = None
        for node in self._graph[source]:
            if node not in path:
                new_path = self.find_path(node, destination, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        self.counter += 1
                        shortest = new_path
        return shortest

    def show_all(self):
        counter = 1
        city_list = []
        train_list = []
        for src, des in self._graph.items():
            city_list.append(src)
            for city, trains in des.items():
                city_list.append(city)
                counter += 1
                for train in trains:
                    train_list.append(train)

        return list(set(city_list)), list(set(train_list)), counter

    def get_train(self, train_number):
        counter = 0
        train_dict = dict()
        src_cities = self._graph.keys()
        cities = []
        for city in src_cities:
            des_cities = self._graph.get(city).keys()
            des_dict = self._graph.get(city)
            for des_city in des_cities:
                if train_number in des_dict.get(des_city):
                    cities.append(des_city)
                    cities.append(city)
                    counter += 1
        city_set = set(cities)
        # counter += 1
        if len(city_set) != 0:
            train_dict['train'] = train_number
            train_dict['count'] = len(city_set)
            train_dict['cities'] = city_set
        return train_dict, counter

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    @property
    def get_graph(self):
        return self._graph
