import netCDF4 as nc
import numpy as N
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import datetime as dt
import pandas as pd

# build date array of all days over 30-year period containing data
start_date = dt.datetime(1980,1,1)
end_date = dt.datetime(2009,12,31)
dates = pd.date_range(start_date,end_date, freq='d')

#ignore years of corrupted data that weren't used; ignore leap days because
#leap days were ignored when building the daily mean files
day_list = []
for date in dates:
    date_yr = date.year
    if date_yr == 1994 or date_yr == 2000:
        continue
    else:
        if date.month == 2 and date.day == 29:
            continue
        else:
            
            day_list.append(date.strftime('%Y%m%d'))

# create numpy array of only dates used in the analysis            
day_array = N.array(day_list)

# read in best matching unit file from matlab output
Bmus_file = pd.read_csv("E:/merra2_yearly_precipwatervapor/som_intermed_data/MERRA2_TQV_SOM_5x4_Bmus.csv",names = ['bmus'],squeeze=True,)
# convert to array
bmus_array = N.array(Bmus_file)

# assign bmus to the date and create a df
# only done because it made calling in particular file names easier by assigning 
# true date to each BMUS
df1 = pd.DataFrame(day_array,columns=['Date'])
df2 = pd.DataFrame(bmus_array,columns=['Bmus'])
date_bmus_df = pd.concat([df1,df2],join='outer',axis=1)

# determine the number of units ('nodes') from the SOM
num_plots = N.max(bmus_array)

# loop through each node
data_to_plot = []
for n in range(num_plots):
    # read in sample file and make empty array to get dimensions
    sample_ncfile = nc.Dataset("E:\\MERRA2_100.tavg1_2d_slv_Nx.19800101.SUB.nc4",'r')
    time = sample_ncfile.variables['time'][:]
    #subset lat, lon for domain that I ran matlab som for    
    lats = sample_ncfile.variables['lat'][49:110]
    lons = sample_ncfile.variables['lon'][144:185]
    time_l = len(time)
    lats_l = len(lats)
    lons_l = len(lons)
    sample_ncfile.close()
    
    # create empty array for the daily composite of variable
    tqv_array = N.zeros((lats_l,lons_l))
    # extract all dates from df from above for a given BMU
    node_dates = N.array(date_bmus_df['Date'][(date_bmus_df['Bmus'] == (n+1))])
    for i in N.arange(0, len(node_dates)):
        date_str = str(node_dates[i])
        # read in data from orginal merra2 files; file names change based on the date
        if date_str >= '19800101' and date_str <= '19911231':
            ncfile = nc.Dataset("E:\\MERRA2_100.tavg1_2d_slv_Nx."+date_str+".SUB.nc4",'r')
            # subset var for spatial domain            
            tqv = N.copy(ncfile.variables['TQV'][:,49:110,144:185])
            # add each hourly time step to the empty array; daily mean will be calculated later from this            
            for t in range(24):
                tqv_array += tqv[t,:,:]
                                    
        elif date_str >= '19920101' and date_str <= '20001231': 
            ncfile = nc.Dataset("E:\\MERRA2_200.tavg1_2d_slv_Nx."+date_str+".SUB.nc4",'r')
            tqv = N.copy(ncfile.variables['TQV'][:,49:110,144:185])
            for t in range(24):
                tqv_array += tqv[t,:,:]
                            
        elif date_str >= '20010101' and date_str <= '20091231':
            ncfile = nc.Dataset("E:\\MERRA2_300.tavg1_2d_slv_Nx."+date_str+".SUB.nc4",'r')
            tqv = N.copy(ncfile.variables['TQV'][:,49:110,144:185])
            for t in range(24):
                tqv_array += tqv[t,:,:]             
        
        else:
            pass
        ncfile.close()
    # calculate total of daily means
    tqv_daily_means = tqv_array/24 #reduce hourly variability
    tqv_node_daily_mean = tqv_daily_means/len(node_dates) #reduce to node average
    #add the composite for that node to the list of all nodes
    data_to_plot.append(tqv_node_daily_mean)




# creates maps for each node included in the som 
fig = plt.figure(1,(8.,8.))

# som was run for a 4x5; hardcoded into the image to make sure the position of figs
# line up with the som
grid_top = ImageGrid(fig, 111, nrows_ncols=(4,5),cbar_location='right',cbar_mode='single',cbar_pad=.2)

# plots each map for each node
for g, d in zip(grid_top,data_to_plot):
    plt.sca(g)
    
    m1 = Basemap(projection='merc',resolution = 'l',llcrnrlon= -86.5,llcrnrlat=32.5,urcrnrlon=-67.5,urcrnrlat=48.5)
    m1.drawstates(color='k', linewidth=.5)
    m1.drawcoastlines(color='k', linewidth=.5)
    m1.drawcountries(color='k', linewidth=.5)

    var1 = d.squeeze()
    x_m, y_m = N.meshgrid(lons,lats)
    x, y = m1(x_m, y_m)

    I = m1.contourf(x,y,var1,levels=N.arange(0,55,5))

# show title and colorbar
#plt.title("Total Precipitable Water Vapor (mm)")
grid_top.cbar_axes[0].colorbar(I)

# save figure
plt.savefig("G:\\informatics\\FinalProject\\som_precipwatervapor_composite_NE.png", dpi=100) 
  

