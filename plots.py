from dataset import Dataset
import matplotlib
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

TIME = 0

# latitude index [0,4]
LAT_idx = 0

# longitude index [0,9]
LNG_idx = 0

variables = Dataset().variables
for var in variables:
    if variables[var].dimensions == ('time', 'level', 'latitude', 'longitude'):

        print('=>', var + '.png')
        ds = Dataset(var)

        data = [
            ds.data[TIME][idx][LAT_idx][LNG_idx]
            for idx, _ in enumerate(ds.levels)
        ]

        fig, ax = plt.subplots()
        fig.suptitle(var)

        plt.subplots_adjust(left=.1, right=.9, bottom=.1, top=.9)
        p, = plt.plot(ds.levels, data)
        ax.set_xlabel('altitude / m')
        ax.set_ylabel('conc / µg/m3')

        plt.savefig('figures/plots/' + var)
