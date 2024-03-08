class Graph:
    '''
    This is our Graph class, which will basically be given the file from which we want to load the data, and it will produce the Graph Structure based on the nodes and edges provided in the file.
    '''
    def __init__(self, filename: str) -> None:
        '''
        This is the constructor for the class. An dictionary is used to represent the graph, with a key having a set of nodes (a set has been used to avoid duplication of ndoes) which denotes the neighbors of the key. Since the graph is undirected, an edge between node u and v also implies an edge between node v and u. The graph is loaded from the file provided.

        Args:
         - filename: str: The name of the file from which we want to load the data.
        
        Returns:
         - None
        '''
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
    
    def neighbors(self, node: int, nodes_set: set) -> set:
        '''
        Returns the set of neighbors of a given node that are also in a given set of nodes. The additonal set is defined to pass on unvisited nodes in our graph so that they can also be explored for potentially better solutions.

        Args:
            - node: int: The node for which we want to find the neighbors.
            - nodes_set: set: The set of nodes for which we want to find the neighbors.

        Returns:
            - set: The set of all the neighbors of the provided node that are also in the provided set of nodes.
        '''
        return self.graph.get(node, set()).intersection(nodes_set)

    def degreesSingleNode(self, node: int) -> int:
        '''' Returns the degree - the number of neighbors - of a given node. '''
        return len(self.graph.get(node, set()))
    
    def degreesPlus(self, node: int, nodes_set: set) -> int:
        ''' Returns the number of neighbors of a given node that are also in a given set of nodes. '''
        return len(self.graph.get(node, set()).intersection(nodes_set))