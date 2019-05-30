import matplotlib.pyplot as plt


class GDGraph():

    def __init__(self, l1=None, l2=None, x_lab=None, y_lab=None, title=None):
        self.l1 = l1
        self.l2 = l2
        self.x_lab = x_lab
        self.y_lab = y_lab
        self.title = title
        self.figure = plt.figure()
        self.figure.set_facecolor('#CCCCFF')

    def set_custom(self):
        if (self.x_lab):
            plt.xlabel(self.x_lab)
        if (self.y_lab):
            plt.ylabel(self.y_lab)
        if (self.title):
            plt.title(self.title)

    def gd_update_graph(self, l1, t, norm):
        self.l1 = l1
        length = len(l1) - 1
        str_val = "T1: %.5f\nT2: %.5f" % (t[0] * norm, t[1])
        str_val2 = "Cost: %.5f\n" % l1[length]
        plt.clf()
        self.set_custom()
        plt.plot(self.l1)
        plt.plot(length, l1[length], 'ro')
        plt.text(length * .75, l1[0] * .90, str_val)
        plt.text(length * .75, l1[length], str_val2)
        plt.pause(0.000001)

    def gd_show_static_graph(self, l1, t, norm):
        self.l1 = l1
        length = len(l1) - 1
        str_val = "Final values:\nT1: %.5f\nT2: %.5f" % (t[0] * norm, t[1])
        str_val2 = "Final value:\nCost: %.5f\n" % l1[length]
        plt.clf()
        self.set_custom()
        plt.plot(self.l1)
        plt.plot(length, l1[length], 'ro')
        plt.text(length * .75, l1[0] * .90, str_val)
        plt.text(length * .75, l1[length], str_val2)
        plt.show()

    def pred_show_graph(self, gd, t, target, prediction):
        limits_m = [min(self.l1), max(self.l1)]
        limits_p = [
            gd.hypothesis(t, min(self.l1)),
            gd.hypothesis(t, max(self.l1))
        ]
        plt.plot(limits_m, limits_p, linewidth=2.5)
        plt.plot(self.l1, self.l2, 'ro')
        plt.plot(target, prediction, 'ro', color='g')
        plt.plot([limits_m[0], target], [prediction, prediction], 'g--')
        plt.plot([target, target], [prediction, limits_p[1]], 'g--')
        str_val = "(%d,%d)" % (target, prediction)
        plt.text(target * 1.005, prediction * 1.005, str_val,
                 color='g', weight='bold')
        plt.show()
