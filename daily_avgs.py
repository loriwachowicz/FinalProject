# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:10:51 2017

@author: ljw11554
"""
## REMEMBER TO CHANGE BOTH START/END DATE IN DAY_RANGE
## REMEMBER TO CHANGE DATE RANGE IN YEARLY LOOP

# missing data for 2 months in 1994.... skip this year
# apparently also missing data for 2000... skip this year too
import netCDF4 as nc
import numpy as N
import datetime as dt
import pandas as pd
from datetime import timedelta

# read in sample file to find dimensions for empty arrays
data_location_str = "E:\\"
ex_input = nc.Dataset(data_location_str+"MERRA2_100.tavg1_2d_slv_Nx.19800101.SUB.nc4",'r')
time = ex_input.variables['time'][:]
#lats = ex_input.variables['lat'][49:110]
#lons = ex_input.variables['lon'][144:185]
lats = ex_input.variables['lat'][:]
lons = ex_input.variables['lon'][:]
time_l = len(time)
lats_l = len(lats)
lons_l = len(lons)
ex_input.close()

# build date array
start_date = dt.date(2001,1,1)
end_date = dt.date(2009,12,31)
day_range = pd.date_range(start_date,end_date,freq='d')

# pull out file names in location and put into a list
TQV_hrly_fnames = []
for date in day_range:
    if date.year >= 1980 and date.year < 1992:
        date_str = date.strftime('%Y%m%d')
        fname = "MERRA2_100.tavg1_2d_slv_Nx."+date_str+".SUB.nc4"
        TQV_hrly_fnames.append(fname)
    elif date.year >= 1992 and date.year < 2001:
        date_str = date.strftime('%Y%m%d')
        fname = "MERRA2_200.tavg1_2d_slv_Nx."+date_str+".SUB.nc4"
        TQV_hrly_fnames.append(fname)
    elif date.year >= 2001 and date.year <= 2009:
        date_str = date.strftime('%Y%m%d')
        fname = "MERRA2_300.tavg1_2d_slv_Nx."+date_str+".SUB.nc4"
        TQV_hrly_fnames.append(fname)
    else:
        pass


TQV_nc_dts = []
TQV_nc_file_names = []
TQV_nc_time_indices = []

# loop through file names and pull out the date from file name
# calculate the base time for that file based on the date of the file
for TQV_hrly_fname in TQV_hrly_fnames:
    date = TQV_hrly_fname.split(".")[2]
    date_dt = dt.datetime.strptime(date,'%Y%m%d')
    yr = date_dt.year
    mt = date_dt.month
    day = date_dt.day
    merra_base_dt = dt.datetime(yr, mt, day, 0, 30)
    
    
    #read in netcdf for the given date
    TQV_nc = nc.Dataset(data_location_str+TQV_hrly_fname)
    TQV_nc_raw_times = TQV_nc.variables['time'][:]
    
    #loop through each time step in the file and add to empty lists
    for ix, raw_t in enumerate(TQV_nc_raw_times):
        t = merra_base_dt + timedelta(minutes=int(raw_t))
        
        TQV_nc_dts.append(t)
        TQV_nc_file_names.append(TQV_hrly_fname)
        TQV_nc_time_indices.append(ix)
    
    TQV_nc.close()

# build a new dataframe of time steps and daily files 
TQV_nc_files_dts_df = pd.DataFrame({'TQV_nc_dt':TQV_nc_dts, 'TQV_nc_index':TQV_nc_time_indices, 'TQV_nc_file_name':TQV_nc_file_names}, index=TQV_nc_dts)

# loop through each year
for year in range(2001,2010,1):
    print "processing: " +str(year)
    #extract all dates within the year
    yearly_TQV_df = TQV_nc_files_dts_df[TQV_nc_files_dts_df.index.year == year]
    
    yearly_dates = []
    start_dt = dt.datetime(year,1,1)
    end_dt = dt.datetime(year,12,31)
    counter_dt = start_dt
    # ignore leap days
    while counter_dt <= end_dt:
        if counter_dt.month == 2 and counter_dt.day == 29:
            pass
        else:
            yearly_dates.append(counter_dt)
        counter_dt += timedelta(days=1)
    # build empty array of to hold daily means at each lat, lon for each day
    yearly_daily_mean_TQV_array = N.empty((len(yearly_dates), len(lats), len(lons)))
    
    # iterate through each hour
    yearly_time_hrs_since_1900_list = []
    for daily_timestep_ix, yearly_date in enumerate(yearly_dates):
        #find all hourly obs within the day and build an empty array of daily mean at each lat lon
        date_df = yearly_TQV_df[N.logical_and(yearly_TQV_df.index.month == yearly_date.month, yearly_TQV_df.index.day == yearly_date.day)]
        date_TQV_array_full = N.empty((len(date_df), len(lats), len(lons)))
        
        # pull out all times for the particular variable (TQV)
        for timestep_ix, timestep_row in enumerate(date_df.iterrows()):
            timestep_TQV_nc = nc.Dataset(data_location_str+timestep_row[1]['TQV_nc_file_name'])
            timestep_TQV_array = N.array(timestep_TQV_nc.variables['TQV'][timestep_row[1]['TQV_nc_index']][:])
            timestep_raw_time = timestep_TQV_nc.variables['time'][timestep_row[1]['TQV_nc_index']]
            timestep_TQV_nc.close()
            
            date_TQV_array_full[timestep_ix::] = timestep_TQV_array
            # build new array of time index
            if timestep_row[1]['TQV_nc_dt'].hour == 0 & timestep_row[1]['TQV_nc_dt'].minute == 30:
                yearly_time_hrs_since_1900_list.append(timestep_raw_time)
            else:
                pass
        # compute daily mean for each day and add daily mean to the yearly array
        date_TQV_array_daily_mean = N.mean(date_TQV_array_full, axis=0)
        yearly_daily_mean_TQV_array[daily_timestep_ix::] = date_TQV_array_daily_mean
        
    # build new netcdf file for the year
    yearly_nc_output = nc.Dataset('E:/merra2_yearly_precipwatervapor/tqv_'+str(year)+'.nc', 'w', format='NETCDF4')
    # creates the dimensions
    lat = yearly_nc_output.createDimension('lat',len(lats))
    lon = yearly_nc_output.createDimension('lon',len(lons))
    time_nc = yearly_nc_output.createDimension('time',len(yearly_dates))
    # creates the variables
    latitudes = yearly_nc_output.createVariable('latitude','f4',('lat',))
    longitudes = yearly_nc_output.createVariable('longitude','f4',('lon',))
    times = yearly_nc_output.createVariable('time','i4',('time',))   
    TQV_output = yearly_nc_output.createVariable('TQV','f4',('time','lat','lon',))
    # assigns variable names to the arrays of data
    latitudes[:] = lats
    longitudes[:] = lons
    times[:] = N.array(yearly_time_hrs_since_1900_list)
    TQV_output[:,:,:] = yearly_daily_mean_TQV_array
    # saves and closes yearly file
    yearly_nc_output.close()