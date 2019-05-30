from src.GradientDescent import GradientDescent


def get_theta_values():
    try:
        f = open("data/theta.csv", "r")
    except Exception as e:
        print("Sorry... Error reading file: ({})".format(e))
        exit(1)
    content = f.read().splitlines()[0].split(",")
    t = [float(content[0]), float(content[1])]
    return(t)


if __name__ == "__main__":
    t = get_theta_values()
    gd = GradientDescent()
    prediction = gd.hypothesis(t, 42000)
    print(prediction)
