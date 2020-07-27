# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:28:12 2019
2020/01/13 Plot 3D crystal strucutre and then cut it into a retangular shape
            Quick method to find matrix elements using Pandat
2020/01/15 Adjust the method to find neighbors quickly with the help of MK
2020/01/15 The center's brightness could be weaker than its negbours 
            Change the code for Al-Mg  
2020/01/17 Add a cycle for calculating Al-Al and Mg-Mg sequentially
            Add a cycle for generating library of SDMs with different z noise
            Save SDMs into a local file with a nomenclature <Simu_AlMg_L12_noise_z_xxx_Al_Al.png>
2020/01/20  Delete all ticks and enlarge it to fill in whole background for CNN preprocessing   
2020/01/24 add new plotting style 
                from matplotlib.colors import BoundaryNorm
                from matplotlib.ticker import MaxNLocator
2020/02/10  change pole to [111] 
2020/02/20  generate more figures: detection eff, noise in z direction   
2020/04/22  optimze figures plot    
2020/04/23  modify SDMs part   
2020/05/24  creat BCC_Fe crystal  
2020/06/18 optimize code
2020/07/15 FCC Al L12 AlMg
2020/07/27 optimizing codes
@author: yue.li
"""

import numpy as np
import os
import shutil
from Euler_transformation import Euler_transformation_100, Euler_transformation_110, Euler_transformation_111
from generator_single_SDMs import single_SDMs
#%% Input file and parameters
data = np.loadtxt('ggoutputFile_L12_5nm_a_0.405.txt')
lattice_para = 0.405

sigma_xy_all = np.arange(0.2,0.8,0.2)
sigma_z_all = np.arange(0.03,0.055,0.002)
detect_eff_array = np.arange(0.35,0.8,0.02)
atomic_number_1 = 27  #Al
atomic_number_2 = 24  #Mg
plot_noise = False #default
plot_SDM = False  #default
Delete_folder = True  #default
image_name_1 = "AlMgLi_L12_AlAl"
image_name_2 = "AlMgLi_L12_MgMg"
#%% clean ouptfile contents
if Delete_folder == True:
    try:
        shutil.rmtree('Results')  
    except:
        print("file does not exist")
    os.mkdir('Results') 
#%% Remove all duplicates    
data_clean = np.unique(data, axis=0)
#%% Euler_transformation
# data_reconstruction = Euler_transformation_100(data_clean, False)
data_reconstruction = Euler_transformation_110(data_clean, False)
# data_reconstruction = Euler_transformation_111(data_clean, False)
#%% Add Gaussian noise
for sigma_xy in sigma_xy_all:
    for sigma_z in sigma_z_all:
        single_SDMs(data_reconstruction, sigma_xy, sigma_z, plot_noise, detect_eff_array, atomic_number_1, atomic_number_2, lattice_para, image_name_1, image_name_2, plot_SDM)
#%%images into H5f
