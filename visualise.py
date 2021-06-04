import numpy as np
import xarray as xr
import matplotlib
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import pandas as pd

    
# for heatwave buddies
def get_location_maps(lat, lon):
    # prepare data
    # files
    chi_2020_2030_file = 'chi_vals_2020-12-01_2030-11-30.txt'
    chi_2030_2040_file = 'chi_vals_2030-12-01_2040-11-30.txt'
    chi_2040_2050_file = 'chi_vals_2040-12-01_2050-11-30.txt'
    land_mask_file = 'land_mask_ind_2020-12-01_2030-11-30.txt'
    rlat_file = 'lat_coords_2020-12-01_2030-11-30.txt'
    rlon_file = 'lon_coords_2020-12-01_2030-11-30.txt'

    land_mask = pd.read_csv(land_mask_file, delimiter=" ")
    rlats = pd.read_csv(rlat_file, delimiter=" ", header=None)
    rlons = pd.read_csv(rlon_file, delimiter=" ", header=None)
    chi_2020_2030 = pd.read_csv(chi_2020_2030_file, delimiter = " ", header=None)
    chi_2030_2040 = pd.read_csv(chi_2030_2040_file, delimiter = " ", header=None)
    chi_2040_2050 = pd.read_csv(chi_2040_2050_file, delimiter = " ", header=None)
    
    # keep all chi values parsed in memory for easy access
    data = np.zeros((3, 2064, 2064))
    for k,z in enumerate(['2020_2030', '2030_2040', '2040_2050']):
        for i in eval('chi_'+ z):
            all_corr = eval('chi_'+ z).iloc[i]
            data[k][i] = all_corr.tolist()
            
    coords = pd.read_csv('derotated_coordinates.csv', delimiter = ",")
    
    # setup for plot
    idx = pd.MultiIndex.from_arrays(arrays=[coords['lat'].tolist(),coords['lon'].tolist()], names=["lat","lon"])
    # find flatteded point index
    p = coords.index[(coords['lat'] == lat) & (coords['lon'] == lon)][0]
    
    figs = []
    for (t,d) in [(0, '2020-2030'),(1, '2030-2040'),(2, '2040-2050')]:   
        s = pd.Series(data=data[t][p], index=idx)
        da = xr.DataArray.from_series(s)
        figs.append(plot(da, coords.iloc[p].postcode, d))
    return figs

def plot(xdata, basepoint_label, time_label):
    #Regional map
    region=[-12,4,47,62] #[lon_min,lon_max,lat_min,lat_max]

    projection = cartopy.crs.PlateCarree(central_longitude=0.0, globe=None)
    transform=cartopy.crs.PlateCarree()

    fig = plt.figure(figsize=(10,10))
    fig.suptitle(f"Heatwave extent. \nBasepoint: {basepoint_label}\nTime period: {time_label}")
    ax = plt.axes(projection=projection)

    ax.coastlines(resolution='50m')
    gl = ax.gridlines(crs=cartopy.crs.PlateCarree(), draw_labels=True,alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    #gl.xlocator = mticker.FixedLocator([-180, -45, 0, 45, 180])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    bounds = np.linspace(0,1,100)
    norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=100)
    #cmap=plt.get_cmap('YlOrRd')
    cmap=plt.get_cmap('gist_rainbow_r')
    #fig=ax.contourf(lons,lats,da,transform=transform,norm=norm,cmap=cmap,levels=bounds)
    #da.plot.pcolormesh(cmap=cmap, norm=norm)
    xdata.plot(cmap=cmap, norm=norm,transform=transform) # alternative: transform=ccrs.OSGB()
    ax.set_extent(region, ccrs.PlateCarree())
    return fig