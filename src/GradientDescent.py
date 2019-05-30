from src.Graph import Graph


class GradientDescent():

    def __init__(self, data_set=[], graph=False):
        self.data = data_set
        self.graph = graph
        self.m = len(self.data)

    def hypothesis(self, t, km):
        return(t[0] + (t[1] * km))

    def tmp_t0(self, learning_rate, t):
        sum = 0
        for i in range(self.m):
            sum += self.hypothesis(t, self.data[i][0]) - self.data[i][1]
        return(sum * learning_rate / self.m)

    def tmp_t1(self, learning_rate, t):
        sum = 0
        for i in range(self.m):
            tmp = self.hypothesis(t, self.data[i][0]) - self.data[i][1]
            sum += tmp * self.data[i][0]
        return(sum * learning_rate / self.m)

    def normalize_data(self):
        p1 = [float(ex[0]) for ex in self.data]
        p1_max = max(p1)
        norm = 1
        while (p1_max > 100):
            norm *= 10
            p1_max /= 10
        for i in self.data:
            i[0] = i[0] / norm
            i[1] = i[1] / norm
        return(norm)

    def calculate_cost(self, t):
        sum = 0
        for ex in self.data:
            step_1 = self.hypothesis(t, ex[0]) - ex[1]
            sum += step_1 * step_1
        return (sum / 2 * self.m)

    def gradient_descent(self):
        learning_rate = 0.0001
        t = [0.0, 0.0]
        tmp_t = [0.0, 0.0]
        norm = self.normalize_data()
        cost = [self.calculate_cost(t)]
        gr = Graph(x_lab="Iterations", y_lab="Cost") if (self.graph) else None
        while (42):
            tmp_t[0] = self.tmp_t0(learning_rate, t)
            tmp_t[1] = self.tmp_t1(learning_rate, t)
            t[0] = t[0] - tmp_t[0]
            t[1] = t[1] - tmp_t[1]
            cost.append(self.calculate_cost(t))
            if (self.graph and len(cost) % 1000 == 0):
                gr.update_graph(cost)
            if (cost[len(cost) - 2] - cost[len(cost) - 1] < 0.00000005):
                if (self.graph):
                    gr.show_static_graph(cost)
                break
        t[0] *= norm
        return(t, len(cost), cost[len(cost) - 1])
