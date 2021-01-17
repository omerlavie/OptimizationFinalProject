from itertools import permutations
from Vertex import Vertex
import math
import time

bop = 0


def calc_length(cities, path):
    """
    The function calculates the distance of a given path.
    :param cities: The vertices that represents the cities on the graph.
    :param path: The path.
    :return: The total length of the path between the vertices.
    """
    length = 0
    for i in range(len(cities)):
        length += cities[path[i]].weight_to(cities[(path[(i + 1) % len(cities)])], bop)
    return length


def brute_force(vertices):
    """
    The function calculates the shortest path between all vertices (TSP) in a brute force manner.
    All permutations of the vertices are being checked.
    :param vertices: The vertices of the graph.
    :return: The shortest path and it's length.
    """
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
    vertices = Vertex.generate_vertices('data/vertices_cost5.csv', 'data/vertices_distances5.csv')
    print(brute_force(vertices))
    end = time.time()
    print("Elapsed time: ", end - start)
