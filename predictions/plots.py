from dataset import Dataset
import matplotlib
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# latitude index [0,4]
LAT_idx = 0

# longitude index [0,9]
LNG_idx = 0

# cyan (00:00)
min_color = (0, 1, 1)

# magenta (23:59)
max_color = (1, 0, 1)


def color(pct):
    return [a * (1 - pct) + b * pct
            for a, b in zip(min_color, max_color)]


variables = Dataset().variables
for var in variables:
    if variables[var].dimensions == ('time', 'level', 'latitude', 'longitude'):

        print('=>', var + '.png')
        ds = Dataset(var)

        fig, ax = plt.subplots()
        # fig.suptitle(var + ' at 500m')
        fig.suptitle(var + '⁻¹ at 500m')
        ax.set_xlabel('time / hrs (starts midnight)')
        # ax.set_ylabel('conc / µg/m3')
        ax.set_ylabel('conc⁻¹ / m3/µg')
        plt.subplots_adjust(left=.15, right=.95, bottom=.1, top=.9)

        hours = 1
        for time in range(hours):

            # levels = ds.levels
            # levels = ds.levels[:4]

            data = [
                1/ds.data[idx][4][LAT_idx][LNG_idx]
                for idx, _ in enumerate(ds.times)
            ]

            #pct = time / (hours - 1)
            #p, = plt.plot(ds.times, data, color=color(pct))
            p, = plt.plot(ds.times, data, color='red')

            custom_lines = [Line2D([0], [0], color=min_color, lw=4),
                            Line2D([0], [0], color=color(0.5), lw=4),
                            Line2D([0], [0], color=max_color, lw=4)]
            # ax.legend(custom_lines, ['0 hrs', '12 hrs', '24 hrs'])

        plt.savefig('predictions/figures/plots/altitude-500/reciprocal/' + var)
