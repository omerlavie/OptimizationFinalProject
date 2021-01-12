import numpy as np

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