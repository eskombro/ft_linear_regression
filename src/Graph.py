import matplotlib.pyplot as plt


class Graph():

    def __init__(self, line_1=[], line_2=None, x_lab=None, y_lab=None):
        self.line_1 = line_1
        self.line_2 = line_2
        self.x_lab = x_lab
        self.y_lab = y_lab

    def update_graph(self, line_1, line_2=None):
        self.line_1 = line_1
        self.line_2 = line_2
        plt.clf()
        plt.plot(self.line_1)
        if (self.x_lab):
            plt.xlabel(self.x_lab)
        if (self.y_lab):
            plt.ylabel(self.y_lab)
        if (line_2):
            plt.plot(line_2)
        plt.pause(0.000001)

    def show_static_graph(self, line_1, line_2=None):
        self.line_1 = line_1
        plt.plot(line_1)
        if (line_2):
            plt.plot(line_2)
        plt.show()
