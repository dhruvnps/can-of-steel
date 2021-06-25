from dataset import Dataset
import matplotlib
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

TIME = 0
FPS = 1.5
MP4 = False  # if true .mpf else .gif

variables = Dataset().variables
for var in variables:
    if variables[var].dimensions == ('time', 'level', 'latitude', 'longitude'):

        filetype = '.mp4' if MP4 else '.gif'

        print('=>', var + filetype)
        ds = Dataset(var)

        vmin = np.min(ds.data[TIME])
        vmax = np.max(ds.data[TIME])

        fig, ax = plt.subplots()
        fig.suptitle('London - ' + var)

        plt.subplots_adjust(left=.1, right=.9, bottom=.2, top=.9)

        ax.set_xlabel('latitude')
        ax.set_ylabel('longitude')

        c = ax.contourf(ds.data[TIME][0], vmin=vmin, vmax=vmax)

        def update(i):
            label = 'Altitude = {:.0f}m'.format(ds.levels[i])
            global c
            for coll in c.collections:
                coll.remove()
            c = ax.contourf(
                ds.data[0][i],
                vmin=vmin,
                vmax=vmax,
            )
            ax.set_xlabel('longitude\n\n' + str(label))

        anim = animation.FuncAnimation(
            fig, update, repeat=True,
            frames=np.arange(0, len(ds.levels)), interval=500
        )

        if MP4:
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=FPS, metadata=dict(
                artist='dhruvnps'), bitrate=1800)
        else:
            writer = animation.PillowWriter(fps=FPS)

        anim.save('predictions/figures/heatmaps/' +
                  var + filetype, writer=writer)
