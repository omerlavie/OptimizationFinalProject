import numpy as np


class Vertex():
    def __init__(self, cost_array, x=0, y=0, id=0):
        self.cost_array = cost_array
        self.x = x
        self.y = y
        self.id = id

    def distance_to(self, vertex):
        x_dist = abs(self.x - vertex.x)
        y_dist = abs(self.y - vertex.y)
        distance = np.sqrt(x_dist ** 2 + y_dist ** 2)
        return distance

    def cost_to(self, vertex):
        return self.cost_array[self.id][vertex.id]

    def weight_to(self, vertex, bop):
        """

        :param vertex:
        :param bop: business or pleasure - 0: find fastest route. 4: find cheapest route.
        :return:
        """
        NORMALIZATION_VAL = 1/4
        return (1 - bop * NORMALIZATION_VAL) * self.distance_to(vertex) + bop * NORMALIZATION_VAL * self.cost_to(vertex)