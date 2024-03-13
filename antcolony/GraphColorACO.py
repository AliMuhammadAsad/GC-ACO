from antcolony.cheenti import *
import numpy as np
import matplotlib.pyplot as plt

class GraphColorACO:
    '''
    This class represents the Ant Colony Optimization Algorithm for the Graph Coloring Problem. It is responsible for generating the colorings for the graph, updating the pheromone matrix, and also for plotting the fitness score vs generation graph.
    '''

    def __init__(self, graph: Graph, alpha: float, beta: float, gamma: float, Q: int, numAnts: int, iterations: int) -> None:
        '''
        This is the constructor for the class. It initializes the class with the graph, alpha, beta, gamma, Q, numAnts, iterations, the number of nodes, the pheromone matrix, colors, ants, and the fitness scores.

        Args:
            - graph: Graph: The graph for which we want to find the coloring.
            - alpha: float: Relative importance of the pheromone trail.
            - beta: float: Relative importance of the heuristic information.
            - gamma: float: Evaporation rate of the pheromone trail.
            - Q: int: Amount of pheromone deposited by an ant.
            - numAnts: int: The number of ants in the ACO algorithm.
            - iterations: int: The number of iterations for which we want to run the ACO algorithm.

        Returns:
            - None
        '''
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

    def generateColorings(self) -> None:
        ''' This method generates a coloring for the graph for each ant in the colony. Each ant constructs a solution by traversing the graph and coloring the nodes. The coloring is then stored in the coloring array. '''
        for i in range(self.numAnts):
            self.ants[i].initializeColors()
            self.coloring[i] = self.ants[i].graphTraversal(self.pheromone)
    
    def getBest(self) -> float:
        ''' This method returns the best fitness score in the current generation. In our case, the best fitness score is the minimum fitness score. '''
        return np.min(self.coloring)

    def getWorst(self) -> float:
        ''' This method returns the worst fitness score in the current generation. In our case, the worst fitness score is the maximum fitness score. '''
        return np.max(self.coloring)
    
    def getAverage(self) -> float:
        ''' This method returns the average fitness score in the current generation. '''
        return np.mean(self.coloring)
    
    def Iteration(self) -> None:
        '''
        This method runs the ACO algorithm for the specified number of iterations. In each iteration, it generates a coloring of the graph for each ant in the colony, updates the pheromone matrix, and then calculates the best, and average fitness scores for the generation.
        '''
        best = float('inf'); avg = []
        for i in range(self.iterations):
            self.generateColorings()
            self.pheromone = (1 - self.evaporationRate) * self.pheromone + sum(ant.PheroMatrix() for ant in self.ants)
            avg.append(self.getAverage())
            self.avgFitness[i] = sum(avg) / len(avg)
            best = min(best, self.getBest())
            self.bestFitness[i] = best
            print(f"Iteration {i + 1}:\tBest Fitness = {best},\tAverage Fitness = {self.avgFitness[i]}")

    def Plot(self) -> None:
        ''' This method plots the fitness score vs generation graph. It plots the best fitness score and the average fitness score for each generation. '''
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