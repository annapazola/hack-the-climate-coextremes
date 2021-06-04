# converting from rotated to regular latitude and longitude

import numpy as np

def unrotate_rll(rlat_in, rlon_in):

    # lat & lon of rotated pole
    plat = 39.25; plon = -162
   
    # convert to radians
    rlon = rlon_in * np.pi/180
    rlat = rlat_in * np.pi/180
    theta = -(90 - plat) * np.pi/180
    phi = -(180 + plon) * np.pi/180
   
    # convert to Cartesian coordinates
    x = np.cos(rlon) * np.cos(rlat)
    y = np.sin(rlon) * np.cos(rlat)
    z = np.sin(rlat)
   
    # rotate Cartesian coordinates
    x_new = np.cos(theta) * np.cos(phi) * x + np.sin(phi) * y + np.sin(theta) * np.cos(phi) * z
    y_new = -np.cos(theta) * np.sin(phi) * x + np.cos(phi) * y - np.sin(theta) * np.sin(phi) * z
    z_new = -np.sin(theta) * x + np.cos(theta) * z
   
    # convert Cartesian coordinates back to lat & lon
    rlon_new = np.arctan2(y_new, x_new) * 180/np.pi
    rlat_new = np.arcsin(z_new) * 180/np.pi
   
    return(rlat_new, rlon_new)