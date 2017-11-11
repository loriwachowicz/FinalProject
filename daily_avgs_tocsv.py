import numpy as N
import pandas as pd
import netCDF4 as nc
import datetime as dt

#kphl_lat = 39.87 [78] ==> 39.5 lat
#kphl_lon = -75.23 [168] ==> -75.0 long

#ex_input = nc.Dataset("E:\\MERRA2_100.tavg1_2d_slv_Nx.19800101.SUB.nc4",'r')
#time = ex_input.variables['time'][:]
#lats = ex_input.variables['lat'][:]
#lons = ex_input.variables['lon'][:]
#time_l = len(time)
#lats_l = len(lats)
#lons_l = len(lons)
#ex_input.close()



# H500, H850, SLP, Q850, QV10M,T2M,T2MDEW,TQV,U850,V850, U10M, V10M,
start_date = dt.datetime(1980,1,1)
end_date = dt.datetime(2010,1,1)
daterange = pd.date_range(start_date,end_date,freq='d')

dates = []
h500 = []
slp = []
h850 = []
q850 = []
qv10m = []
t2m = []
t2mdew = []
tqv = []
u850 = []
v850 = []
u10m = []
v10m = []

for date in daterange:
    date_str = date.strftime('%Y%m%d')
    if date.month in [12,1,2]:
        if date_str>= '19800101' and date_str <= '19911231':
            try:
                ncfile = nc.Dataset("E:\\MERRA2_100.tavg1_2d_slv_Nx."+date_str+".SUB.nc4",'r')
                SLP = N.copy(ncfile.variables['SLP'][:,78,168])
                H500 = N.copy(ncfile.variables['H500'][:,78,168])
                H850 = N.copy(ncfile.variables['H850'][:,78,168])
                Q850 = N.copy(ncfile.variables['Q850'][:,78,168])
                QV10M = N.copy(ncfile.variables['QV10M'][:,78,168])
                T2M = N.copy(ncfile.variables['T2M'][:,78,168])
                T2MDEW = N.copy(ncfile.variables['T2MDEW'][:,78,168])
                TQV = N.copy(ncfile.variables['TQV'][:,78,168])
                U850 = N.copy(ncfile.variables['U850'][:,78,168])
                V850 = N.copy(ncfile.variables['V850'][:,78,168])
                U10M = N.copy(ncfile.variables['U10M'][:,78,168])
                V10M = N.copy(ncfile.variables['V10M'][:,78,168])
                
                dates.append(date_str)
                slp.append(N.mean(SLP))
                h500.append(N.mean(H500))
                h850.append(N.mean(H850))
                q850.append(N.mean(Q850))
                qv10m.append(N.mean(QV10M))
                t2m.append(N.mean(T2M))
                t2mdew.append(N.mean(T2MDEW))
                tqv.append(N.mean(TQV))
                u850.append(N.mean(U850))
                v850.append(N.mean(V850))
                u10m.append(N.mean(U10M))
                v10m.append(N.mean(V10M))
                ncfile.close()
                del SLP,H500,H850,Q850,QV10M,T2M,T2MDEW,TQV,U850,V850,U10M,V10M
            except RuntimeError:
                print date_str
                pass
                
        elif date_str >= '19920101' and date_str <= '20001231': 
            try:
                ncfile = nc.Dataset("E:\\MERRA2_200.tavg1_2d_slv_Nx."+date_str+".SUB.nc4",'r')
                SLP = N.copy(ncfile.variables['SLP'][:,78,168])
                H500 = N.copy(ncfile.variables['H500'][:,78,168])
                H850 = N.copy(ncfile.variables['H850'][:,78,168])
                Q850 = N.copy(ncfile.variables['Q850'][:,78,168])
                QV10M = N.copy(ncfile.variables['QV10M'][:,78,168])
                T2M = N.copy(ncfile.variables['T2M'][:,78,168])
                T2MDEW = N.copy(ncfile.variables['T2MDEW'][:,78,168])
                TQV = N.copy(ncfile.variables['TQV'][:,78,168])
                U850 = N.copy(ncfile.variables['U850'][:,78,168])
                V850 = N.copy(ncfile.variables['V850'][:,78,168])
                U10M = N.copy(ncfile.variables['U10M'][:,78,168])
                V10M = N.copy(ncfile.variables['V10M'][:,78,168])
                
                dates.append(date_str)
                slp.append(N.mean(SLP))
                h500.append(N.mean(H500))
                h850.append(N.mean(H850))
                q850.append(N.mean(Q850))
                qv10m.append(N.mean(QV10M))
                t2m.append(N.mean(T2M))
                t2mdew.append(N.mean(T2MDEW))
                tqv.append(N.mean(TQV))
                u850.append(N.mean(U850))
                v850.append(N.mean(V850))
                u10m.append(N.mean(U10M))
                v10m.append(N.mean(V10M))
                ncfile.close()
                del SLP,H500,H850,Q850,QV10M,T2M,T2MDEW,TQV,U850,V850,U10M,V10M
            except RuntimeError:
                print date_str
                pass
            
        elif date_str >= '20010101' and date_str <= '20091231':
            try:
                ncfile = nc.Dataset("E:\\MERRA2_300.tavg1_2d_slv_Nx."+date_str+".SUB.nc4",'r')
                SLP = N.copy(ncfile.variables['SLP'][:,78,168])
                H500 = N.copy(ncfile.variables['H500'][:,78,168])
                H850 = N.copy(ncfile.variables['H850'][:,78,168])
                Q850 = N.copy(ncfile.variables['Q850'][:,78,168])
                QV10M = N.copy(ncfile.variables['QV10M'][:,78,168])
                T2M = N.copy(ncfile.variables['T2M'][:,78,168])
                T2MDEW = N.copy(ncfile.variables['T2MDEW'][:,78,168])
                TQV = N.copy(ncfile.variables['TQV'][:,78,168])
                U850 = N.copy(ncfile.variables['U850'][:,78,168])
                V850 = N.copy(ncfile.variables['V850'][:,78,168])
                U10M = N.copy(ncfile.variables['U10M'][:,78,168])
                V10M = N.copy(ncfile.variables['V10M'][:,78,168])
                
                dates.append(date_str)
                slp.append(N.mean(SLP))
                h500.append(N.mean(H500))
                h850.append(N.mean(H850))
                q850.append(N.mean(Q850))
                qv10m.append(N.mean(QV10M))
                t2m.append(N.mean(T2M))
                t2mdew.append(N.mean(T2MDEW))
                tqv.append(N.mean(TQV))
                u850.append(N.mean(U850))
                v850.append(N.mean(V850))
                u10m.append(N.mean(U10M))
                v10m.append(N.mean(V10M))
                ncfile.close()
                del SLP,H500,H850,Q850,QV10M,T2M,T2MDEW,TQV,U850,V850,U10M,V10M    
            except RuntimeError:
                print date_str
                pass

        
    else:
        pass
df1 = pd.DataFrame(dates,columns=['Dates'])
df2 = pd.DataFrame(h500,columns=['h500'])  
df3 = pd.DataFrame(slp,columns=['slp'])
df4 = pd.DataFrame(h850,columns=['h850'])
df5 = pd.DataFrame(q850,columns=['q850'])
df6 = pd.DataFrame(qv10m,columns=['qv10m'])
df7 = pd.DataFrame(t2m,columns=['t2m'])
df8 = pd.DataFrame(t2mdew,columns=['t2mdew'])
df9 = pd.DataFrame(tqv,columns=['tqv'])
df10 = pd.DataFrame(u850,columns=['u850'])
df11 = pd.DataFrame(v850,columns=['v850'])
df12 = pd.DataFrame(u10m,columns=['u10m'])
df13 = pd.DataFrame(v10m,columns=['v10m'])

new_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13],join='outer',axis=1)
new_df.to_csv("G:\\informatics\\merra2_phl_metvars.csv")
  