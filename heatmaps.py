from dataset import Dataset
import matplotlib
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

time = 0

variables = Dataset().variables
for var in variables:
    if variables[var].dimensions == ('time', 'level', 'latitude', 'longitude'):

        print(var)
        ds = Dataset(var)

        vmin = np.min(ds.data[time])
        vmax = np.max(ds.data[time])

        fig, ax = plt.subplots()
        fig.suptitle('London - ' + var)

        # plt.subplots_adjust(left=.1, right=.9, bottom=.3, top=.9)
        plt.subplots_adjust(left=.1, right=.9, bottom=.2, top=.9)

        ax.set_xlabel('latitude')
        ax.set_ylabel('longitude')

        c = ax.contourf(ds.data[time][0], vmin=vmin, vmax=vmax)

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

        #Writer = animation.writers['ffmpeg']
        #writer = Writer(fps=2, metadata=dict(artist='dhruvnps'), bitrate=1800)
        writer = animation.PillowWriter(fps=2)
        anim.save('figures/heatmaps/' + var + '.gif', writer=writer)


# def update(val):
#     level.valtext.set_text(ds.levels[int(level.val)])
#     time.valtext.set_text(ds.times[int(time.val)])
#     global c
#     for coll in c.collections:
#         coll.remove()
#     c = ax.contourf(
#         ds.data[int(time.val)][int(level.val)],
#         vmin=ds.vmin,
#         vmax=ds.vmax,
#     )


# level = Slider(
#     plt.axes([.1, .1, .8, .03]),
#     'altitude',
#     valmin=0,
#     valmax=len(ds.levels) - 1,
#     valstep=1,
#     valinit=0,
# )
# level.on_changed(update)

# time = Slider(
#     plt.axes([.1, .15, .8, .03]),
#     'time',
#     valmin=0,
#     valmax=len(ds.times) - 1,
#     valstep=1,
#     valinit=0,
# )
# time.on_changed(update)

# plt.show()
