from dataset import Dataset
import matplotlib
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

time = 0
latitude, longitude = (0, 0)

variables = Dataset().variables
for var in variables:
    if variables[var].dimensions == ('time', 'level', 'latitude', 'longitude'):

        print(var)
        ds = Dataset(var)

        data = [
            ds.data[time][idx][latitude][longitude]
            for idx, _ in enumerate(ds.levels)
        ]

        fig, ax = plt.subplots()
        fig.suptitle(var)

        plt.subplots_adjust(left=.1, right=.9, bottom=.1, top=.9)
        p, = plt.plot(ds.levels, data)
        ax.set_xlabel('altitude / m')
        ax.set_ylabel('conc / µg/m3')

        plt.savefig('figures/' + var)
