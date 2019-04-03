# -*- coding: utf-8 -*-
import xarray as xr
#Além do xarray, é necessário instalar netcdf4

# International Comprehensive Ocean-Atmosphere Data Set da década de 1700
# from https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.nodc:ICOADS-netCDF
ds = xr.open_dataset('../nc_file/ICOADS_R3.0.0_1700-09.nc')
df = ds.to_dataframe()