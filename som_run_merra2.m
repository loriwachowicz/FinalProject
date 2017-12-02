clear, clc

data_in = [];
addpath('E:/merra2_yearly_precipwatervapor/SOM-Toolbox-master/som');
for yr = 1980:2009
    if (yr ~= 2000) && (yr ~= 1994);
        nc_fname = strcat('E:/merra2_yearly_precipwatervapor/tqv_',num2str(yr),'.nc');
   
    
        TQV_yr = ncread(nc_fname,'TQV',[145 50 1],[40 60 Inf],[1 1 1]);
    
        TQV_yr_permuted = permute(TQV_yr, [3 1 2]);
        TQV_yr_2d = reshape(TQV_yr_permuted,[],size(TQV_yr_permuted,2)*size(TQV_yr_permuted,3));
    
        data_in = cat(1,data_in,TQV_yr_2d);
    
    
        clear nc_fname;
        clear TQV_yr;
        clear TQV_yr_permuted;
        clear TQV_yr_2d;
    end
    
end

%%

% Normalize Data in 2-D Input Variable-- 'var' normalizes the variance of
% the variable to unity and its mean to zero via a simple linear
% transformation.
% data_in would be your 2-D data array with time as rows and grid points as
% columns.
% Normalizing is more important if you are including more than one
% atmospheric variable in the SOM.
sD = som_normalize(data_in, 'var');

clear data_in;

%%
% Initialize a SOM with random values with a given map size (here it is
% 5x4 -- 5 columns x 4 rows). randinit essentially randomly puts the nodes 
% in the data space (sD).
sM = som_randinit(sD,'msize',[5 4]);

%%
% seqtrain is the training algorithm and is the time consuming part. I've
% used the trainlen option here to indicate the number of times I want the
% nodes to update.
sM = som_seqtrain(sM,sD,'trainlen',1000);

%%
% VERY IMPORANT to save the sM variable immediately, this struct has several
% critical data in it. 
save('E:/merra2_yearly_precipwatervapor/som_intermed_data/MERRA2_TQV_SOM_5x4_sM.mat','sM');

% I always save the sD variable as it is the input data used for the SOM,
% not as important to save as sM, especially if your input data are large.
save('E:/merra2_yearly_precipwatervapor/som_intermed_data/MERRA2_TQV_SOM_5x4_sD.mat','sD');
%%
% som_bmus is probably the most important function, this will give you the
% 'Best matching Unit for each time input (i.e. will be equal to the number
% of rows). So for each time, this Bmus variable will have the closest
% matching unit for every time.
Bmus = som_bmus(sM,sD,1);

% Save your Bmus variable immediately
save('E:/merra2_yearly_precipwatervapor/som_intermed_data/MERRA2_TQV_SOM_5x4_Bmus.mat','Bmus')

% This will write out your Bmus variable as a csv if you want
csvwrite('E:/merra2_yearly_precipwatervapor/som_intermed_data/MERRA2_TQV_SOM_5x4_Bmus.csv',Bmus)

% These are two types of error you can calculate if you want, it can give
% you some idea of how well the SOM is performing. Mostly used to track if
% adding iterations is worth the computational expense.
% [qe, te] = som_quality(sM, sD);