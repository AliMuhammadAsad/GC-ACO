from antcolony.GraphColorACO import *

# # Params
# alpha = 4.0          # relative importance of the pheromone trail
# beta = 4.0           # relative importance of the heuristic information
# gamma = 0.7         # evaporation rate of the pheromone trail
# Q = 10             # Amount of Pheromone deposited by an ant
# numAnts = 10        # Number of ants
# iterations = 50    # Number of iterations

# Testing Params
alpha = 4.0          # relative importance of the pheromone trail
beta = 4.0           # relative importance of the heuristic information
gamma = 0.95        # evaporation rate of the pheromone trail
Q = 5             # Amount of Pheromone deposited by an ant
numAnts = 10        # Number of ants
iterations = 100    # Number of iterations


if __name__ == "__main__":
    print("#---------------------------------------- Graph Coloring Using Ant Colony Optimization ----------------------------------------#")
    print("| Alpha | Beta | Gamma |  Q  | Num Ants | Iterations |")
    print(f"|   {alpha}   |   {beta}  |  {gamma}  |  {Q} |     {numAnts}   |     {iterations}     |")
    # print(f"Running with Params: alpha = {alpha}, beta = {beta}, gamma = {gamma}, Q = {Q}, numAnts = {numAnts}, iterations = {iterations}")
    num = int(input("Press 1 to select data file queen11_11.col\nPress 2 to select data file le450_15b.col:\nSelect Number:"))
    if num == 1:
        filename = 'data/queen11_11.col'
    elif num == 2:
        filename = 'data/le450_15b.col'
    elif num == 3:
        filename = 'data/test.txt'
    print(f"File {filename} selected. If its the second file, please wait a few seconds for it to load - heavy data")
    Graph = Graph(filename)
    AntColony = GraphColorACO(Graph, alpha, beta, gamma, Q, numAnts, iterations)
    AntColony.Generation()
    AntColony.Plot()