# Introduction to Optimization - Final Project
Final project in Introduction to Optimization class (89-589), Bar-Ilan University.

## Introduction
In this project we introcuded a similar problem to TSP, but the difference is that the weight of the graph's edges are calculated during runtime, depending on a paramter BOP.\
BOP is a parameter that indicates if the costumer is flying for __business or pleasure__. There are two weights for each edge, one represents the flight cost between two vertices and the other is the distance between two vertices.\
If BOP=0, that means that the costumer wants the shortest path, meaning that it dosn't care of the cost, even if it's very high.
If BOP=4, the costumer want the cheapest path and he dosn't care of the length.
Any value between 0 and 4 will give a relative value between the two edges weights.\
Due to the complexity of the brute force algorithm on this problem _(O(n!))_ we had to choose an optimization algorithm to solve it.

In our project we compared two optimization algorithms: 
* Genetic Algorithm
* Ant Colony optimzation

## How to run
Inside the ```main.py``` file there are two main functions that generates vertices for the algorithms: 
* ```generate_vertices_locations``` - creates a list of coordinates and their x,y locations.
* ```generate_matrix``` generate a 2D matrix of vertices and the flight cost between them.

More information on how to use this functions is available in the source code.

### Genetic Algorithm
The algorithm is inside ```GA.py``` file. To run it, run the ```run_algorithm``` function. The two last paramters to this function is the files generated in the ```main.py``` file. First one is the flights cost file generated and the second one is the list of vertices coordinates.

### Ant Colony Optimization
The algorithm is inside the ```ACO.py``` file. To run it, run the ```SolveTSPUsingACO``` function. Generate the vertices from the files using ```Vertex.generate_vertices``` function and pass it to ```SolveTSPUsingACO``` function.
