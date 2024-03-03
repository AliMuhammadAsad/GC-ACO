class Graph:
    def __init__(self, filename: str) -> None:
        self.graph = {}
        with open(filename, 'r') as f:
            graphData = f.readlines()[0].split()
            self.numNodes = int(graphData[2]); self.numEdges = int(graphData[3])
        with open(filename, 'r') as f:
            for line in f.readlines()[1:]:
                lData = line.split()
                n1 = int(lData[1]) - 1; n2 = int(lData[2]) - 1
                if n1 not in self.graph:
                    self.graph[n1] = set()
                if n2 not in self.graph:
                    self.graph[n2] = set()
                self.graph[n1].add(n2); self.graph[n2].add(n1)
    
    def neighbors(self, node, nodes_set: set) -> set:
        return self.graph.get(node, set()).intersection(nodes_set)

    def degreesSingleNode(self, node: int) -> int:
        return len(self.graph.get(node, set()))
    
    def degreesPlus(self, node: int, nodes_set: set) -> int:
        return len(self.graph.get(node, set()).intersection(nodes_set))


# class Graph:
#     '''
#     This is our Graph class, which will basically be given the file from which we want to load the data, and it will produce the Graph Structure based on the nodes and edges provided in the file.
#     '''

#     def __init__(self, filename: str) -> None:
#         '''
#         This is the constructor for the class.

#         Args:
#          - filename: str: The name of the file from which we want to load the data.
        
#         Returns:
#          - None
#         '''
#         self.graph = {}
#         with open(filename, 'r') as f:
#             graphData = f.readlines()[0].split()
#             self.numNodes = int(graphData[2]) ; self.numEdges = int(graphData[3])
#         with open(filename, 'r') as f:
#             for line in f.readlines()[1:]:
#                 lData = line.split()
#                 n1 = int(lData[1]) - 1; n2 = int(lData[2]) - 1
#                 if n1 not in self.graph:
#                     self.graph[n1] = set()
#                 if n2 not in self.graph:
#                     self.graph[n2] = set()
#                 self.graph[n1].add(n2); self.graph[n2].add(n1)
    
#     def neighbors(self, node: int, nodeO=None) -> set:
#         '''
#         For any provided node, it returns the set of all the neighbors of that node. If an optional node is provided, it returns the intersection of the neighbors of the two nodes.

#         Args:
#             - node: int: The node for which we want to find the neighbors.
#             - nodeO: int: The optional node for which we want to find the neighbors.

#         Returns:
#             - set: The set of all the neighbors of the provided node.
#         '''
#         if nodeO is None: return self.graph.get(node, set())
#         else: return self.graph.get(node, set()).intersection(nodeO)

#     def degrees(self, node: int, nodeO=None) -> int:
#         '''
#         This methods returns the degrees of any given node - that is, the number of neighbors that this node has. If an optional node is provided, it returns the intersection of the degrees of the two nodes.

#         Args:
#             - node: int: The node for which we want to find the degrees.
#             - nodeO: int: The optional node for which we want to find the degrees.

#         Returns:
#             - int: The number of neighbors of the provided node.
#         '''
#         if nodeO is None: return len(self.graph.get(node, set()))
#         else: return len(self.graph.get(node, set()).intersection(nodeO))
