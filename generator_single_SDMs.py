# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:20:35 2020

@author: yue.li
""";

import numpy as np
import matplotlib.pyplot as plt
from scipy import spatial
import pandas as pd
import random as rd
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from fast_histogram import histogram2d as fast_histogram2d 

mu  = 0
SDM_bins = 200   #define pixel density

def single_SDMs(data_reconstruction, sigma_xy, sigma_z, plot_noise, detect_eff_array, atomic_number_1, atomic_number_2, lattice_para, image_name_1, image_name_2, plot_SDM):
   #%% adding noise with the same dimension as 'data_clean'
    print('---->>')
    print('sigma_xy=',sigma_xy)
    print('sigma_z=',sigma_z)
    row = data_reconstruction.shape[0]
    noise_xy = np.random.normal(mu, sigma_xy, [row ,2]) 
    noise_z = np.random.normal(mu, sigma_z, [row ,1])
    zeros = np.zeros((row, 1))
    noise = np.hstack((noise_xy, noise_z, zeros))
    data_noise = data_reconstruction + noise
    #%% Plot 3D crystal structure with noise
    if plot_noise == True:
        ax = plt.subplot(111, projection='3d')  # build a project
        ax.scatter(data_noise [:, 0], data_noise [:, 1], data_noise [:, 2], c=data_noise [:, 3], s=8)  # 绘制数据点
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_zlabel('Z', fontsize=16)  # axis
        ax.set_ylabel('Y', fontsize=16)
        ax.set_xlabel('X', fontsize=16)
        plt.show()
    #%%Plot Gaussian distributions
#    count, bins, ignored = plt.hist(noise_z[:,0], 30, density=True)
#    plt.plot(bins, 1/(sigma_z * np.sqrt(2 * np.pi)) *
#             np.exp( - (bins - mu)**2 / (2 * sigma_z**2) ),linewidth=2, color='r')
#    plt.show()
    #%% Detect efficiency
    #Data random sequence
    data_no_shuffle = data_noise     #110   #no noise
    row = data_no_shuffle.shape[0]
    idx = rd.sample(range(row),row) 
    data_shuffle = data_no_shuffle[idx]

    for detect_eff in detect_eff_array:
        print ('detect_eff is', detect_eff)
        data_sample = data_shuffle[:int(row*detect_eff), :]
        data = data_sample
        row_number = data.shape[0]
        #%% Finding element 1 and element 2
        df = pd.DataFrame(data,columns=['a','b','c','d'])
        
        for el_number in range(1):
    #        print('element_number=', el_number)
            if el_number == 0:
                element_1 = df.loc[(df['d'] == atomic_number_1 ) , ['a','b','c']]   
                element_1 = element_1.values
            else:
                element_2 = df.loc[(df['d'] == atomic_number_2 ) , ['a','b','c']]  
                element_1 = element_2.values
            #Note to use & or | to replace and/or.
                
            #%% generating SDMs
            tree = []
            tree = spatial.cKDTree(element_1)
            SDM = np.zeros([SDM_bins,SDM_bins])
            x_tot = [];
            y_tot = [];
            num_in_SDM = 0;
            max_cand =0
            cand = tree.query_ball_point(element_1, 1.5,return_sorted=False, n_jobs = -1)
            for list in cand:
                num_in_SDM += len(list);
                if (len(list) > max_cand):
                    max_cand = len(list);
            x_tot = np.zeros([num_in_SDM,], dtype = np.float32)
            y_tot = np.zeros([num_in_SDM,], dtype = np.float32)
            x = np.zeros([max_cand,], dtype = np.float32)   
            y = np.zeros([max_cand,], dtype = np.float32)   
            
            start = 0;
            i = 0;
            for list in cand:
                length = len(list)
                x_tot[start:(start+length)] = np.ndarray.__sub__(element_1[list,0],element_1[i,0]);
                y_tot[start:(start+length)] = np.ndarray.__sub__(element_1[list,2],element_1[i,2]);
                i += 1
                start = start+length;
            notzero = (x_tot!=0)*(y_tot!=0);
            SDM = fast_histogram2d(y_tot[notzero],x_tot[notzero], range = [[-1.5,1.5],[-1.5,1.5]],  bins=SDM_bins)   
            #%%Save hisgram z-SDM 
            if plot_SDM == False:
                xedges = np.linspace(-1.5, 1.5, num=SDM_bins+1, endpoint=True, retstep=False, dtype=np.float32)
                yedges = np.linspace(-1.5, 1.5, num=SDM_bins+1, endpoint=True, retstep=False, dtype=np.float32)
                fig2D = plt.figure(figsize=(4,4))
                ax2D = fig2D.add_subplot(111)
                levels = MaxNLocator(nbins=8).tick_values(1, SDM.max())
                if el_number == 0:
                    cmap = plt.get_cmap('BuGn') # jet
                else:
                    cmap = plt.get_cmap('Blues')
                
                norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)   
                im=ax2D.pcolormesh(yedges, xedges, SDM, cmap=cmap, norm=norm)                             
            
                ax2D.set_aspect(1)
                plt.xlim((-0.7,0.7))
                plt.ylim((-0.7,0.7))
                ax2D.set_xticks([])
                ax2D.set_yticks([])
                plt.axis('off')
                plt.subplots_adjust(0,0,1,1)
                # plt.show() 
                plt.close()   
                if el_number == 0:
                    fig2D.savefig('Results\Simu_'+image_name_1+'_a_%.3f_de_%.2f_noise_z_%.3f_noise_xy_%.2f.png'%(lattice_para, detect_eff, sigma_z, sigma_xy),dpi=SDM_bins)
                else:
                    fig2D.savefig('Results\Simu_'+image_name_2+'_a_%.3f_de_%.2f_noise_z_%.3f_noise_xy_%.2f.png'%(lattice_para, detect_eff, sigma_z, sigma_xy),dpi=SDM_bins)        
            #%%Plot hisgram z-SDM
            else:
                xedges = np.linspace(-1.5, 1.5, num=SDM_bins+1, endpoint=True, retstep=False, dtype=np.float32)
                yedges = np.linspace(-1.5, 1.5, num=SDM_bins+1, endpoint=True, retstep=False, dtype=np.float32)
                fig2D = plt.figure(figsize=(4,4))
                ax2D = fig2D.add_subplot(111)
                levels = MaxNLocator(nbins=8).tick_values(1, SDM.max())
                if el_number == 0:
                    cmap = plt.get_cmap('jet') #BuGn
                else:
                    cmap = plt.get_cmap('Blues')
                
                norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)   
                im=ax2D.pcolormesh(yedges, xedges, SDM, cmap=cmap, norm=norm)  
                ax2D.set_xlabel('$\Delta$x, nm', fontsize=20)
                ax2D.set_ylabel('$\Delta$z, nm', fontsize=20)
                print('element_number=', el_number)
                ax2D.set_aspect(1)
                plt.xlim((-0.7,0.7))
                plt.ylim((-0.7,0.7))
                plt.xticks(fontsize=18)
                plt.yticks(fontsize=18)
                cb = fig2D.colorbar(im,ax=ax2D)
                cb.ax.tick_params(labelsize=18)
                plt.show()  