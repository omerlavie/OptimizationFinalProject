import csv
from random import randint
from numpy import genfromtxt
from Vertex import Vertex


def generate_matrix(num_of_vertices, min_cost=0, max_cost=200):
    """
    The function creates a symmetric 2D matrix that represent the cost of travel between two nodes. The cost is calculated
    randomly.
    :param num_of_vertices: Number of vertices to calculate their cost.
    :param min_cost: The minimum cost that can be between two vertices.
    :param max_cost:The maximum cost that can be between two vertices.
    :return: The 2D array.
    """
    # Create an empty 2D matrix by the size of num_of_vertices * num_of_vertices.
    matrix = [[0 for x in range(num_of_vertices)] for y in range(num_of_vertices)]
    for i in range(num_of_vertices):
        for j in range(i, num_of_vertices):
            if i == j:
                # The distance between a vertex to himself is 0.
                matrix[i][j] = 0
            else:
                # Cost between vertices x->y and y->x are the same.
                matrix[i][j] = matrix[j][i] = randint(min_cost, max_cost)
    return matrix


def generate_vertices_locations(num_of_vertices, min_val=0, max_val=200):
    """
    The function generates a list of vertices in a 2D plain.
    :param num_of_vertices: The number of vertices to be generated.
    :param min_val: The minimum location in x,y graph.
    :param max_val: The maximum location in x,y graph.
    :return: A list of vertices.
    """
    matrix = [[0 for x in range(2)] for y in range(num_of_vertices)]
    for i in range(num_of_vertices):
        matrix[i][0] = randint(min_val, max_val)
        matrix[i][1] = randint(min_val, max_val)
    return matrix


def generate_vertices(cost_path, distance_path):
    list = []
    cost_file = genfromtxt(cost_path, delimiter=',')
    dist_file = genfromtxt(distance_path, delimiter=',')
    for i in range(len(cost_file)):
        list.append(Vertex(cost_file, dist_file[i][0], dist_file[i][1], i))
    return list


if __name__ == '__main__':
    a = generate_matrix(40, 30, 1200)
    with open("data/vertices_cost2.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(a)

    b = generate_vertices_locations(40, 100, 16000)
    with open("data/vertices_distances2.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(b)