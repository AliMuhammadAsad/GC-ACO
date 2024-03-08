from antcolony.graph import *
import random, bisect
import numpy as np

class Cheenti:
    '''
    This class represents an ant in the Ant Colony Optimization Algorithm. It is responsible for finding a complete path for the ant to traverse the graph, and also for updating the pheromone matrix based on the path found.
    '''
    def __init__(self, alpha: float, beta: float, Q: int, Graph: Graph, colors: list) -> None:
        '''
        This is the constructor for the class. It initializes the class with the alpha, beta, Q, Graph, and colors. It also initializes the number of nodes, edges, unvisited nodes, distance traversed by the ant, and the colorMap and colorAssign dictionaries.

        Args:
            - alpha: float: Relative importance of the pheromone trail.
            - beta: float: Relative importance of the heuristic information.
            - Q: int: Amount of pheromone deposited by an ant.
            - Graph: Graph: The graph on which the ant will traverse.
            - colors: list: The list of colors that the ant can use to color the graph.

        Returns:
            - None
        '''
        self.Graph = Graph
        self.nodes = self.Graph.numNodes
        self.edges = self.Graph.numEdges
        self.unvisited = list(self.Graph.graph.keys())
        self.alpha = alpha
        self.beta = beta
        self.Q = Q
        self.colors = colors
        self.distance = 0
        self.colorMap = {}
        self.colorAssign = {}
    
    def initializeColors(self) -> None:
        '''
        This method initializes the color map and color assignment. The color map is a dictionary that maps the colors to the nodes that have been colored with that color. The color assignment is a dictionary where they keys are the nodes and the values are the colors assigned to those nodes.
        '''
        for color in self.colors:
            self.colorMap[color] = set()
        for key in self.Graph.graph.keys():
            self.colorAssign[key] = None
    
    def getSource(self, unvisited: set) -> int:
        ''' This method returns a random node from the set of unvisited node. This node acts as the source for the ant to start traversing the graph. '''
        return random.choice(list(unvisited))
    
    def getVisibility(self, node: int, visited: set, unvisited: set, heur: int) -> int:
        ''' This method returns the visibility of a node, which is the degree of the node with respect to the number of visited nodes. '''
        if heur == 1:
            return self.Graph.degreesPlus(node, visited)
        elif heur == 3:
            return self.Graph.degreesPlus(node, visited.union(unvisited))
    
    def getPheromonesTrail(self, node: int, color: int, PheroMat: np.ndarray) -> float:
        ''' This method returns the average pheromone trail on the edges between a node and the nodes that have been colored with the same color.'''
        return np.mean([PheroMat[node][x] for x in self.colorMap[color]])
    
    def Probabilities(self, visible: dict, PheroTrail: dict, unvisited: list) -> int:
        '''
        This method calculates the probabilities of moving to each of the unvisited nodes from the current node. It uses the visibility and pheromone trail to calculate the probabilities.
        '''
        visible = {k: v + 1e10 for k, v in visible.items()}
        numer = np.zeros(len(unvisited))
        for i in range(len(unvisited)):
            numer[i] = (PheroTrail[unvisited[i]]**self.alpha) * (visible[unvisited[i]]**self.beta)
        denom = sum(numer)
        probabilities = np.cumsum(numer/denom)
        idx = bisect.bisect_left(probabilities, random.uniform(0, 1))
        return unvisited[idx]
    
    def graphTraversal(self, PheroMat: np.ndarray) -> int:
        '''
        This method takes the pheromone matrix as input, and constructs a complete traversal in the graph and updates the distance of the path. 
        '''
        heur = 1
        q = k = 0
        unvisited = set(self.unvisited)
        while k < self.nodes:
            k += 1; q += 1
            visited = set()
            source = self.getSource(unvisited)
            if q not in self.colorMap:
                self.colorMap[q] = set()
            self.colorMap[q].add(source)
            self.colorAssign[source] = q
            neighbors = self.Graph.neighbors(source, unvisited)
            while len(unvisited.difference(neighbors.union({source}))):
                k += 1
                visited = visited.union(neighbors)
                unvisited = unvisited.difference(neighbors.union({source}))
                unvisited_list = list(unvisited)
                visible = {v: self.getVisibility(v, visited, unvisited, heur) for v in unvisited}
                PheroTrail = {v: self.getPheromonesTrail(v, q, PheroMat) for v in unvisited}
                source = self.Probabilities(visible, PheroTrail, unvisited_list)
                neighbors = self.Graph.neighbors(source, unvisited)
                self.colorMap[q].add(source)
                self.colorAssign[source] = q
            unvisited = visited.union(neighbors)
        self.distance = q
        return self.distance
    
    def PheroMatrix(self) -> np.ndarray:
        ''' This method updates the pheromone matrix based on the path found by the ant.'''
        PMat = np.zeros((self.nodes, self.nodes))
        for v1 in range(self.nodes):
            for v2 in range(self.nodes):
                if self.colorAssign[v1] == self.colorAssign[v2] and (v1 != v2):
                    PMat[v1, v2] = self.Q
        return PMat