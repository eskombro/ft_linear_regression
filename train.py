from src.GradientDescent import GradientDescent


def get_data():
    try:
        f = open("data/data.csv", "r")
    except Exception as e:
        print("Sorry... Error reading file: ({})".format(e))
        exit(1)
    content = f.read().splitlines()[1:]
    data_set = []
    for item in content:
        data = item.split(',')
        data_set.append([
                         float(data[0]),
                         float(data[1])
                        ])
    return (data_set)


def train(data_set):
    gd = GradientDescent(data_set, graph=True)
    t, iter, cost = gd.gradient_descent()
    print("Total iterations:       {}".format(iter))
    print("Last iteration cost:    {}".format(cost))
    print("Theta 0:                {}".format(t[0]))
    print("Theta 1:                {}".format(t[1]))
    return(t)


def write_results_file(t):
    try:
        f = open("data/theta.csv", "w")
        f.write("{},{}".format(t[0], t[1]))
        f.close
    except Exception as e:
        print("Sorry... Couldn't create file: ({})".format(e))
        exit(1)
    print("Theta values were written in file: {}".format(f.name))


if __name__ == "__main__":
    data_set = get_data()
    t = train(data_set)
    write_results_file(t)
