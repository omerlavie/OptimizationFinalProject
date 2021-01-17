import numpy as np
from numpy import genfromtxt


# The number of options between bop options.
NUMBER_OF_OPTIONS = 5


class Vertex:
    def __init__(self, cost_array, x=0, y=0, id=0):
        self.cost_array = cost_array
        self.x = x
        self.y = y
        self.id = id

    def distance_to(self, vertex):
        """
        The function calculates the Euclidean distance between two vertices.
        :param vertex: The vertex to calculate his distance to.
        :return: The Euclidean distance between the two vertices.
        """
        x_dist = abs(self.x - vertex.x)
        y_dist = abs(self.y - vertex.y)
        distance = np.sqrt(x_dist ** 2 + y_dist ** 2)
        return distance

    def cost_to(self, vertex):
        """
        The function calculates the cost between two vertices from the cost_array matrix.
        :param vertex: The vertex to calculate his cost to.
        :return:The cost between the two vertices.
        """
        return self.cost_array[self.id][vertex.id]

    def weight_to(self, vertex, bop):
        """
        The function calculates the relative (by the bop value) cost and distance between the two vertices.
        :param vertex: The vertex to calculate the edge weight to.
        :param bop: business or pleasure - 0: find fastest route. 4: find cheapest route.
        :return: The normalized (by the bop value) edge weight between the two vertices.
        """
        # The bop value must be between 0 and the number of options - 1 to scroll between.
        if bop < 0 or bop > NUMBER_OF_OPTIONS - 1:
            raise Exception(f"bop value must be between 0 and {NUMBER_OF_OPTIONS - 1}")
        normalization_val = 1 / (NUMBER_OF_OPTIONS - 1)
        return (1 - bop * normalization_val) * self.distance_to(vertex) + bop * normalization_val * self.cost_to(vertex)

    def calc_path_weights(vertices, path=0):
        if path == 0:
            path = range(len(vertices))
        total_cost = 0
        total_distance = 0
        for i in range(len(vertices)):
            total_cost += vertices[path[i]].cost_to(vertices[(path[(i + 1) % len(vertices)])])
            total_distance += vertices[path[i]].distance_to(vertices[(path[(i + 1) % len(vertices)])])
        return total_cost, total_distance

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