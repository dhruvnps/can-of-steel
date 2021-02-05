from dataset import Dataset
import matplotlib
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

ds = Dataset('dust')

fig, ax = plt.subplots()
plt.subplots_adjust(left=.1, right=.9, bottom=.3, top=.9)
c = ax.contourf(ds.data[0][0], vmin=ds.vmax, vmax=ds.vmax)


def update(val):
    level.valtext.set_text(ds.levels[int(level.val)])
    time.valtext.set_text(ds.times[int(time.val)])
    global c
    for coll in c.collections:
        coll.remove()
    c = ax.contourf(
        ds.data[int(time.val)][int(level.val)],
        vmin=ds.vmin,
        vmax=ds.vmax,
    )


level = Slider(
    plt.axes([.1, .1, .8, .03]),
    'altitude',
    valmin=0,
    valmax=len(ds.levels) - 1,
    valstep=1,
    valinit=0,
)
level.on_changed(update)

time = Slider(
    plt.axes([.1, .15, .8, .03]),
    'time',
    valmin=0,
    valmax=len(ds.times) - 1,
    valstep=1,
    valinit=0,
)
time.on_changed(update)

plt.show()
