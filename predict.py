from src.GradientDescent import GradientDescent
from src.GDGraph import GDGraph


def plot_graphic(gd, t, target, prediction):
    val_1 = []
    val_2 = []
    for i in gd.data:
        val_1.append(i[0])
        val_2.append(i[1])
    gr = GDGraph(val_1, val_2, "Mileage", "Price", "Prediction")
    gr.set_custom()
    gr.pred_show_graph(gd, t, target, prediction)


def value_from_prompt():
    while (42):
        val = input("Type mileage to get price: ")
        try:
            val_f = float(val)
            if (val_f > 0):
                return (val_f)
            else:
                print("Mileage must be greater than 0")
        except Exception as e:
            print(e)
    return (0)


def get_theta_values():
    try:
        f = open("data/theta.csv", "r")
    except Exception as e:
        print("Sorry... Error reading file: ({})".format(e))
        return([0, 0])
    content = f.read().splitlines()[0].split(",")
    t = [float(content[0]), float(content[1])]
    return(t)


if __name__ == "__main__":
    gd = GradientDescent()
    target = value_from_prompt()
    t = get_theta_values()
    prediction = gd.hypothesis(t, target)
    print("Estimated price: {}".format(prediction))
    plot_graphic(gd, t, target, prediction)
