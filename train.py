from src.GradientDescent import GradientDescent


def print_result(t, iter, cost):
    print("Total iterations:       {}".format(iter))
    print("Last iteration cost:    {}".format(cost))
    print("Theta 0:                {}".format(t[0]))
    print("Theta 1:                {}".format(t[1]))


def write_results_file(t):
    try:
        f = open("data/theta.csv", "w")
        f.write("{},{}".format(t[0], t[1]))
        f.close
    except Exception as e:
        print("Sorry... Couldn't create file: ({})".format(e))
        exit(1)
    print("Theta values were written in file: {}".format(f.name))


def train():
    gd = GradientDescent(True)
    t, iter, cost = gd.gradient_descent(learning_rate=0.0005)

    return(t, iter, cost)


if __name__ == "__main__":
    t, iter, cost = train()
    write_results_file(t)
    print_result(t, iter, cost)
