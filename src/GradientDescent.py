from src.Graph import Graph

class GradientDescent():

    def __init__(self, data_set, graph=False):
        self.data_set = data_set
        self.graph = graph

    def estimate_price(self, t, km):
        return(t[0] + (t[1] * km))


    def tmp_t0(self, data_set, learning_rate, t):
        val = 0
        for i in range(len(data_set)):
            val += self.estimate_price(t, data_set[i][0]) - data_set[i][1]
        val = val * learning_rate / len(data_set)
        return(val)


    def tmp_t1(self, data_set, learning_rate, t):
        val = 0
        for i in range(len(data_set)):
            val += (self.estimate_price(t, data_set[i][0]) - data_set[i][1]) * data_set[i][0]
        val = val * learning_rate / len(data_set)
        return(val)


    def normalize_data(self, data_set):
        p1 = [float(ex[0]) for ex in data_set]
        p1_max = max(p1)
        norm = 1
        while (p1_max > 100):
            norm *= 10
            p1_max /= 10
        for i in data_set:
            i[0] = i[0] / norm
            i[1] = i[1] / norm
        return(norm)


    def calculate_cost(self, data_set, t):
        sum = 0
        m = len(data_set)
        for ex in data_set:
            step_1 = self.estimate_price(t, ex[0]) - ex[1]
            sum += step_1 * step_1
        return (sum / 2 * m)


    def gradient_descent(self):
        learning_rate = 0.0001
        t = [0.0, 0.0]
        tmp_t = [0.0, 0.0]
        norm = self.normalize_data(self.data_set)
        cost = [self.calculate_cost(self.data_set, t)]
        gr = Graph(x_label="Iterations", y_label="Cost") if (self.graph) else None
        while (42):
            tmp_t[0] = self.tmp_t0(self.data_set, learning_rate, t)
            tmp_t[1] = self.tmp_t1(self.data_set, learning_rate, t)
            t[0] = t[0] - tmp_t[0]
            t[1] = t[1] - tmp_t[1]
            cost.append(self.calculate_cost(self.data_set, t))
            if (self.graph and len(cost) % 1000 == 0):
                gr.update_graph(cost)
            if (cost[len(cost) - 2] - cost[len(cost) - 1] < 0.00000005):
                print(cost[len(cost) - 1], self.estimate_price([t[0] * norm, t[1]], 42000))
                if (self.graph):
                    gr.show_static_graph(cost)
                break
        t[0] *= norm
        return(t)
