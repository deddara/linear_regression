import numpy as np
import matplotlib.pyplot as plt
import  sys
import sklearn.metrics as sm

class linear_regression :

    def __init__(self):
        self.learning_rate = 0.01
        self.theta0 = self.theta1 = 0
        self.tmp_theta0 = self.tmp_theta1 = 1.0
        self.price = np.array([], dtype=int)
        self.km = np.array([], dtype=int)
        self.norm_price = np.array([], dtype=float)
        self.norm_km = np.array([], dtype=float)
        self.get_data()


    def get_data(self):
        fd = open('data.csv', 'r')
        data = fd.readlines()
        i = -1
        for line in data:
            if i == -1:
                i = i + 1
                continue
            values = line.split(',')
            self.price = np.append(self.price, int(values[1]))
            self.km = np.append(self.km, int(values[0]))
            i = i + 1
        self.price_min = min(self.price)
        self.price_max = max(self.price)
        self.km_max = max(self.km)
        self.km_min = min(self.km)

    def normalize(self):
        for x in self.price:
            self.norm_price = np.append(self.norm_price, (x - self.price_min) / (self.price_max - self.price_min))
        for x in self.km:
            self.norm_km = np.append(self.norm_km, (x - self.km_min) / (self.km_max - self.km_min))

    def mse(self):
        loss_func_sum = 0
        for i in range(len(self.norm_km)):
            loss_func = self.tmp_theta0 + (self.tmp_theta1 * self.norm_km[i]) - self.norm_price[i]
            loss_func *= loss_func
            loss_func_sum += loss_func
        return loss_func_sum / len(self.norm_km)

    def write_values(self):
        fd = open('theta_values', 'w')
        fd.write("slope = ")
        fd.write(str(self.theta1))
        fd.write("\n")
        fd.write("intercept = ")
        fd.write(str(self.theta0))

    def train_model(self, show_plot):
        iterations = 15000
        self.normalize()
        mse_res = self.mse()
        prev_mse_res = mse_res
        dlt_mse = mse_res
        i = 0

        while dlt_mse > 0.0000001 or dlt_mse < -0.0000001:
            # y_predicted = theta0 + (theta1 * norm_km)
            gradient_func1 = gradient_func0 = 0
            self.theta0 = self.tmp_theta0
            self.theta1 = self.tmp_theta1

            for j in range(len(self.norm_km)):
                gradient_func0 += self.tmp_theta0 + (self.tmp_theta1 * self.norm_km[j]) - self.norm_price[j]
            for j in range(len(self.norm_km)):
                gradient_func1 += ((self.tmp_theta0 + (self.tmp_theta1 * self.norm_km[j]) - self.norm_price[j]) * self.norm_km[j])
            self.tmp_theta0 -= self.learning_rate * (gradient_func0/len(self.norm_price))
            self.tmp_theta1 -= self.learning_rate * (gradient_func1/len(self.norm_km))
            prev_mse_res = mse_res
            mse_res = self.mse()
            dlt_mse = mse_res - prev_mse_res
            if (show_plot == 2 and i % 1000 == 0):
                tmp_plot_theta0 = self.price_min + ((self.price_max - self.price_min) * self.theta0) + self.theta1 * (1 - self.km_min)
                tmp_plot_theta1 = (self.price_max - self.price_min) * self.theta1 / (self.km_max - self.km_min)
                plt.plot(self.km, tmp_plot_theta0 + (tmp_plot_theta1 * self.km), color="green")
            i += 1

        self.theta1 = (self.price_max - self.price_min) * self.theta1 / (self.km_max - self.km_min)
        self.theta0 = self.price_min + ((self.price_max - self.price_min) * self.theta0) + self.theta1 * (1 - self.km_min)
        if (show_plot != 0) :
            plt.scatter(self.km, self.price, color = "red")
            plt.plot(self.km, self.theta0 + (self.theta1 * self.km), color="green")
            plt.show()
        self.write_values()


show_plot = 0

if (len(sys.argv) > 2):
    print("Invalid num of arguments")
    exit(1)

for arg in sys.argv:
    if arg == "-show_plot":
        show_plot = 1
    if arg == "-show_plot_by_step":
        show_plot = 2
    if arg == "--help":
        print("-show_plot - to show a plot")
        print("-show_plot_by_step - to show a plot step by step (for each 1000 step)")
        exit(0)


lin_reg = linear_regression()
lin_reg.train_model(show_plot)
