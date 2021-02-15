import sklearn.metrics as sm
import numpy as np

class accuracy :
    def __init__(self):
        self.price = np.array([], dtype=int)
        self.km = np.array([], dtype=int)
        self.get_data()
        self.get_theta()


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

    def get_theta(self):
        fd = open('theta_values', 'r')
        self.theta1 = float(fd.readline().split('=')[1])
        self.theta0 = float(fd.readline().split('=')[1])

    def predict(self):
        print("R2 score =", round(sm.r2_score(self.price, self.theta0 + (self.theta1 * self.km)), 2))

accur = accuracy()

accur.predict()