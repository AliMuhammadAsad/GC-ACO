from antcolony.graph import *
import random, bisect
import numpy as np

class Cheenti:
    def __init__(self, alpha: float, beta: float, Q:int, Graph, colors):
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
    
    def initialize(self):
        for color in self.colors:
            self.colorMap[color] = set()
        for key in self.Graph.graph.keys():
            self.colorAssign[key] = None
    
    def getSource(self, unvisited: set):
        return random.choice(list(unvisited))
    
    def getVisibility(self, node, visited):
        return self.Graph.degreesPlus(node, visited)
    
    def getPheromonesTrail(self, node, color, PheroMat):
        return np.mean([PheroMat[node][x] for x in self.colorMap[color]])
    
    def Probabilities(self, visible, PheroTrail, set1):
        visible = {k: v + 1e10 for k, v in visible.items()}
        numer = np.zeros(len(set1))
        for i in range(len(set1)):
            numer[i] = (PheroTrail[set1[i]]**self.alpha) * (visible[set1[i]]**self.beta)
        denom = sum(numer)
        probabilities = np.cumsum(numer/denom)
        idx = bisect.bisect_left(probabilities, random.uniform(0, 1))
        return set1[idx]
    
    def aCompletePath(self, PheroMat):
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
                set1 = list(unvisited)
                visible = {v: self.getVisibility(v, visited) for v in unvisited}
                PheroTrail = {v: self.getPheromonesTrail(v, q, PheroMat) for v in unvisited}
                source = self.Probabilities(visible, PheroTrail, set1)
                neighbors = self.Graph.neighbors(source, unvisited)
                self.colorMap[q].add(source)
                self.colorAssign[source] = q
            unvisited = visited.union(neighbors)
        self.distance = q
        return self.distance
    
    def PheroMatrix(self):
        PMat = np.zeros((self.nodes, self.nodes))
        for v1 in range(self.nodes):
            for v2 in range(self.nodes):
                if self.colorAssign[v1] == self.colorAssign[v2] and (v1 != v2):
                    PMat[v1, v2] = self.Q / self.distance
        return PMat