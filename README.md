# Any Colony Optimization - Swarm Intelligence

This repository contains the second assignment for the course ```CS 451 - Computational Intelligence```. The assignment is about ```Ant Colony Optimization (ACO)```, and optimizing the ```Graph Coloring Problem``` using ```ACO```.

### Running the Code

The [antcolony](antcolony) file contains the implementation for the ```Graph``` class, the ```Ant``` class, and the ```Graph Coloring using ACO``` class. The [main.py](main.py) file runs the algorithm, by loading the data from the [data](data) directory, and running an ant colony on the structured graph. 

To run the code, just simply run the following command in the terminal:
```
make
```

This invokes the ```Makefile``` and runs the ```main.py``` accordingly. This also opens an interactive shell where you can select the datafile you want to load, along with showing the parameters that the code has been set to. The parameters can also be updated in the ```main.py``` file as well accordingly. 

### Graph Coloring Problem

Graph coloring is a classic problem in Computer Science in which you are required to color the vertices of a graph (vertex coloring) with minimum colors such that no two adjacent vertices are of same color (as shown in the image below). 

<img align='center' src='gco.png' width="50%" />

To solve this problem, Ant-Colony Optimization was implemented, and the *queen11_11.col* and *le450-1b.col* datasets were used which can be accessed from [here](https://mat.tepper.cmu.edu/COLOR/instances.html).