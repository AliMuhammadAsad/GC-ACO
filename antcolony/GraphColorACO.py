from antcolony.cheenti import *
import numpy as np
import matplotlib.pyplot as plt

class GraphColorACO:
    def __init__(self, graph, alpha, beta, gamma, Q, numAnts, iterations):
        self.Graph = graph
        self.Q = Q
        self.alpha = alpha
        self.beta = beta
        self.evaporationRate = gamma
        self.numAnts = numAnts
        self.iterations = iterations
        self.numNodes = self.Graph.numNodes
        self.pheromone = np.ones((self.numNodes, self.numNodes))
        self.colors = [i for i in range(1, max([int(graph.degreesSingleNode(i)) for i in range(self.numNodes)]) + 1)]
        self.ants = [Cheenti(self.alpha, self.beta, self.Q, self.Graph, self.colors) for _ in range(self.numAnts)]
        self.coloring = np.zeros(self.numAnts)
        self.bestFitness = np.zeros(self.iterations)
        self.avgFitness = np.zeros(self.iterations)
        self.worstFitness = np.zeros(self.iterations)

    def generateColorings(self):
        for i in range(self.numAnts):
            self.ants[i].initialize()
            self.coloring[i] = self.ants[i].aCompletePath(self.pheromone)
    
    def updatePheroMat(self):
        self.pheromone = (1 - self.evaporationRate) * self.pheromone + sum(ant.PheroMatrix() for ant in self.ants)
    
    def getBest(self):
        return np.min(self.coloring)

    def getWorst(self):
        return np.max(self.coloring)
    
    def getAverage(self):
        return np.mean(self.coloring)
    
    def Generation(self):
        best = float('inf'); avg = []
        for i in range(self.iterations):
            self.generateColorings()
            self.updatePheroMat()
            avg.append(self.getAverage())
            self.avgFitness[i] = sum(avg) / len(avg)
            best = min(best, self.getBest())
            self.bestFitness[i] = best
            print(f"Iteration {i + 1}:\tBest Fitness = {best},\tAverage Fitness = {self.avgFitness[i]}")

    def Plot(self):
        iters = list(range(self.iterations))
        plt.plot(iters, self.bestFitness, label='Best Fitness')
        plt.plot(iters, self.avgFitness, label='Average Fitness')

        plt.annotate(f"{self.avgFitness[-1]:.2f}",
                     (len(self.avgFitness) - 1, self.avgFitness[-1]),
                     textcoords="offset points",
                     xytext=(-10, 10),
                     ha='center',
                     arrowprops=dict(arrowstyle="->", color='blue'))
        
        plt.annotate(f"{self.bestFitness[-1]:.2f}",
                     (len(self.bestFitness) - 1, self.bestFitness[-1]),
                     textcoords="offset points",
                     xytext=(0, -20),
                     ha='center',
                     arrowprops=dict(arrowstyle="->", color='orange'))
        
        plt.title('Fitness Score vs Generation'); plt.xlabel('Generation'); plt.ylabel('Fitness Score')
        plt.legend(); plt.show()    