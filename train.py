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


if __name__ == "__main__":
    data_set = get_data()
    gd = GradientDescent(data_set, graph=True)
    t = gd.gradient_descent()
    print(t)
