from itertools import permutations
from Vertex import Vertex
import math
import time
import timeit

bop = 0


def calc_length(cities, path):
    length = 0
    for i in range(len(cities)):
        length += cities[path[i]].weight_to(cities[(path[(i + 1) % len(cities)])], bop)
    return length


def BruteForce(vertices):
    min_length = math.inf
    min_path = range(len(vertices))

    for path in permutations(range(len(vertices))):
        temp_val = calc_length(vertices, path)
        if temp_val < min_length:
            min_length = temp_val
            min_path = path
    return min_length, min_path


if __name__ == '__main__':
    start = time.time()
    vertices = Vertex.generate_vertices('vertices_cost4.csv', 'vertices_distances4.csv')
    print(BruteForce(vertices))
    end = time.time()
    print("Elapsed time: ", end - start)
