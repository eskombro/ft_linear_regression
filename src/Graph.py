import matplotlib.pyplot as plt

class Graph():

    def __init__(self, line_1=[], line_2=None, x_label=None, y_label=None):
        self.line_1 = line_1
        self.line_2 = line_2
        self.x_label = x_label
        self.y_label = y_label

    def update_graph(self, line_1, line_2=None):
        self.line_1 = line_1
        self.line_2 = line_2
        plt.clf()
        plt.plot(self.line_1)
        if (self.x_label):
            plt.xlabel(self.x_label)
        if (self.y_label):
            plt.ylabel(self.y_label)
        if (line_2):
            plt.plot(line_2)
        plt.pause(0.000001)

    def show_static_graph(self, line_1, line_2=None):
        self.line_1 = line_1
        plt.plot(line_1)
        if (line_2):
            plt.plot(line_2)
        plt.show()
