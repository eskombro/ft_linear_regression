def get_data():
    try:
        f = open("data.csv", "r")
    except Exception as e:
        print("Sorry... Error reading file: ({})".format(e))
        exit(1)
    content = f.read().splitlines()[1:]
    data_set = []
    for item in content:
        data = item.split(',')
        data_set.append([
                         float(data[0])/10000,
                         float(data[1])/10000
                        ])
    return (data_set)


def estimate_price(t, km):
    return(t[0] + (t[1] * km))


def tmp_t0(data_set, learning_rate, t):
    val = 0
    for i in range(len(data_set)):
        val += estimate_price(t, data_set[i][0]) - data_set[i][1]
    val = val * learning_rate / len(data_set)
    return(val)


def tmp_t1(data_set, learning_rate, t):
    val = 0
    for i in range(len(data_set)):
        val += (estimate_price(t, data_set[i][0]) - data_set[i][1]) * data_set[i][0]
    val = val * learning_rate / len(data_set)
    return(val)


def gradient_descent():
    learning_rate = 0.0001
    t = [0.0, 0.0]
    tmp_t = [0.0, 0.0]
    data_set = get_data()
    for i in range(250000):
        tmp_t[0] = tmp_t0(data_set, learning_rate, t)
        tmp_t[1] = tmp_t1(data_set, learning_rate, t)
        t[0] = t[0] - tmp_t[0]
        t[1] = t[1] - tmp_t[1]
    t[0] *= 10000
    return(t)


if __name__ == "__main__":
    t = gradient_descent()
    print(estimate_price(t, 42000))
