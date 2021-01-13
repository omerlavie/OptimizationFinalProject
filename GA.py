import matplotlib.pyplot as plt
import numpy as np
import os
import random
from Vertex import Vertex
from numpy import genfromtxt
import numpy as np


bop = 0
myFile = np.genfromtxt('data1.csv', delimiter=',')

class Route:
    def __init__(self, cities):
        self.cities = cities
        self.distance = self._calculate_distance()
        self.fitness = 1 / self.distance

    def _calculate_distance(self):
        self.distance = 0
        for i, from_city in enumerate(self.cities):
            to_city = self.cities[(i + 1) % len(self.cities)]
            self.distance += from_city.weight_to(to_city, bop)

        return self.distance

    def mate_with(self, route):
        child_cities = list()

        # from parent 1
        start = random.randint(0, len(self.cities) - 1)
        end = random.randint(start, len(self.cities) - 1)
        child_cities = self.cities[start:end]

        # from parent 2
        for city in route.cities:
            if city not in child_cities:
                child_cities.append(city)

        return Route(child_cities)
    
    def plot(self, save=None):
        fig, ax = plt.subplots(figsize=(5, 5))
        xx = [city.x for city in self.cities] + [self.cities[0].x]
        yy = [city.y for city in self.cities] + [self.cities[0].y]
        ax.plot(xx, yy, c='k')
        ax.scatter(xx, yy, c='r')
        plt.axis('off')
        if save:
            plt.savefig(save, dpi=500)


class Population:

    def __init__(self, cities, size):
        self.routes = list()
        self.size = size

        for _ in range(size):
            shuffled_cities = random.sample(cities, len(cities))
            self.routes.append(Route(shuffled_cities))

        self.routes = sorted(self.routes, key=lambda r: r.fitness, reverse=True)

    def best_route(self):
        return self.routes[0]

    def propagate(self, elite_size):
        elite = self.routes[:elite_size]
        self.routes = elite
        while len(self.routes) < self.size:
            parent1, parent2 = random.sample(elite, 2)
            self.routes.append(parent1.mate_with(parent2))
        self.routes = sorted(self.routes, key=lambda r: r.fitness, reverse=True)


def generate_vertices(cost_path, distance_path):
    """
    The function generates vertices from distance file and cost file.
    :param cost_path:
    :param distance_path:
    :return:
    """
    list = []
    cost_file = genfromtxt(cost_path, delimiter=',')
    dist_file = genfromtxt(distance_path, delimiter=',')
    for i in range(len(cost_file)):
        list.append(Vertex(cost_file, dist_file[i][0], dist_file[i][1], i))
    return list


def run_algorithm(n_cities, n_generations, snap_freq, cost_path, distance_path):
    if not os.path.exists(f"snapshots_{n_cities}cities"):
        os.mkdir(f"snapshots_{n_cities}cities")

    # Generate the cities vertices from files.
    cities = generate_vertices(cost_path, distance_path)

    popul = Population(cities, size=1000)
    best_distance = list()
    for i in range(n_generations):
        popul.propagate(elite_size=300)
        best_route = popul.best_route()
        print(best_route.distance)
        best_distance.append(best_route.distance)
        if i % snap_freq == 0:
            best_route.plot(save=f"snapshots_{n_cities}cities/generation_{i}.png")
        for i in best_route.cities:
            print(i.id, ",", end="")
        total_cost, total_dist = Vertex.calc_path_weights(best_route.cities)
        print(f"Total cost is: {total_cost} and total distance is: {total_dist}")

    fix, ax = plt.subplots(figsize=(7, 7))
    ax.plot(range(len(best_distance)), best_distance, c='k')
    plt.xlabel("Generation", fontsize=15)
    plt.ylabel("Distance", fontsize=15)
    ax.tick_params(axis="both", labelsize=12)
    plt.title(f"Genetic algorithm on a {n_cities}-city TSP", fontsize=15)
    plt.savefig(f"{n_cities}_distance_generation.png", dpi=500)
    
    
if __name__ == "__main__":
    bop = 0
    run_algorithm(25, 20, 1, "vertices_cost2.csv", "vertices_distances2.csv")
