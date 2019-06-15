from collections import deque

class Graph():

    def __init__(self, direct_graph = False):
        self.direct_graph = direct_graph
        self.adjacency_list = {}
        self.nodes_data = {}

    def add_node(self, key, data = None):
        self.adjacency_list[key] = {}
        self.nodes_data[key] = data if data else None

    def add_edge(self, key1, key2, weight = 1): 
        self.adjacency_list[key1][key2] = weight
        if not self.direct_graph:
            self.adjacency_list[key2][key1] = weight 

    def edge_weight(self, key1, key2):
        return self.adjacency_list[key1][key2]

    def update_weight(self, key1, key2, weight):
        self.adjacency_list[key1][key2] = weight

    def adjacents(self, key):
        return self.adjacency_list[key].keys()

    def node_data(self, key):
        return self.nodes_data[key]

    def __contains__(self, key):
        return key in self.adjacency_list

    def has_edge(self, key1, key2):
        return key2 in self.adjacency_list[key1]

    def bfs(self, s, t, parents):
        visited = {s}
        queue = deque([s]) 

        while queue:
            current = queue.popleft()
            
            for adjacent, weight in self.adjacency_list[current].items():
                if not adjacent in visited and weight > 0:
                    queue.append(adjacent)
                    visited.add(adjacent)
                    parents[adjacent] = current

        return t in visited

    def ford_fulkerson(self, s, t): 
        
        parent = { node: None for node in graph.adjacency_list }
        residual = Graph(direct_graph = True)
        for node, adjacents in self.adjacency_list.items():
            residual.add_node(node) if not node in residual else None
            for adjacent, weight in adjacents.items(): 
                residual.add_node(adjacent) if not adjacent in residual else None
                residual.add_edge(node, adjacent, weight) 
                residual.add_edge(adjacent, node, 0) if not self.has_edge(adjacent, node) else None

        max_flow = 0

        while residual.bfs(s, t, parent):
            path_flow = float("Inf") 
            v = t

            while v != s:
                u = parent[v] 
                path_flow = min(path_flow, residual.edge_weight(u,v))
                v = parent[v]

            v = t
            while v != s:
                u = parent[v] 
                residual.update_weight(u, v, residual.edge_weight(u,v) - path_flow)
                residual.update_weight(v, u, residual.edge_weight(v,u) + path_flow) 
                v = parent[v]

            max_flow += path_flow

        return max_flow


"""
Ford Fulkerson Example
"""

"""
graph = Graph(True)

graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(0, 1, 16)
graph.add_edge(0, 2, 13)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 12)
graph.add_edge(2, 1, 4)
graph.add_edge(2, 4, 14)
graph.add_edge(3, 2, 9)
graph.add_edge(3, 5, 20)
graph.add_edge(4, 3, 7)
graph.add_edge(4, 5, 4)

print(graph.ford_fulkerson(0,5))
"""
