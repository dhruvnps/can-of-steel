import netCDF4 as nc
import numpy as np


class Dataset:
    def __init__(self, var=None):
        ds = nc.Dataset('predictions/download.nc')

        if var is not None:
            self.data = ds[var][:]

            self.levels = ds['level'][:]
            self.times = ds['time'][:]

            self.vmin = np.min(ds[var][:])
            self.vmax = np.max(ds[var][:])

        self.variables = ds.variables
