import netCDF4 as nc
import numpy as np


class Dataset:
    data = []
    levels = []
    times = []

    vmin = None
    vmax = None

    def __init__(self, var):
        ds = nc.Dataset('data.nc')

        self.data = ds[var][:]
        self.vmin = np.min(ds[var][:])
        self.vmax = np.max(ds[var][:])

        self.levels = ds['level'][:]
        self.times = ds['time'][:]
