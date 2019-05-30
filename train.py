from src.GradientDescent import GradientDescent


def train():
    gd = GradientDescent(True)
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
    t = train()
    write_results_file(t)
