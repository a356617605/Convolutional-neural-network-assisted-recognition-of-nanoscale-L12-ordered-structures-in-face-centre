# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:51:32 2020

@author: yue.li
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def Euler_transformation_100(data_clean, plot):
    #%% Plot 3D crystal structure without duplicates
    data_110 = data_clean
    if plot == True:
        df = pd.DataFrame(data_clean,columns=['a','b','c','d'])
        group_1 = df[df.d==56].values
        group_2 = df[df.d==24].values
        fig = plt.figure()
        ax = plt.subplot(111, projection='3d')  # build a project
        ax.scatter(data_clean [:, 0], data_clean [:, 1], data_clean [:, 2], c=data_clean [:, 3], s=8)  # 绘制数据点
        #ax.plot(group_1 [:, 0], group_1 [:, 2], 'p', zdir = 'y', label = 'Al')    #divide it into different parts
        #ax.plot(group_2 [:, 0], group_2 [:, 2], 'o', zdir = 'y', label = 'Mg')    #divide it into different parts
        
        # plt.legend(loc='upper right')
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_zlabel('Z', fontsize=16)  # axis
        ax.set_ylabel('Y', fontsize=16)
        ax.set_xlabel('X', fontsize=16)
        plt.show()
    return data_110
#%%
def Euler_transformation_110(data_clean, plot):
    #%%  change pole from 100 to 110
    row = data_clean.shape[0]
    data_110 = np.empty([row,4], dtype = float)
    data_110[:,3] = data_clean[:,3]
    
    ##rotate along x axis
    #data_110[:,0] = data_sample[:,0]
    #data_110[:,1] = (data_sample[:,1]+data_sample[:,2])*math.sqrt(2)/2.0
    #data_110[:,2] = (data_sample[:,1]+data_sample[:,2])*math.sqrt(2)/2.0
    
    #rotate along y axis
    data_110[:,0] = (data_clean[:,0]-data_clean[:,2])*math.sqrt(2)/2.0
    data_110[:,1] = data_clean[:,1]
    data_110[:,2] = (data_clean[:,0]+data_clean[:,2])*math.sqrt(2)/2.0
    
    ##rotate along Z axis
    #data_110[:,0] = (data_sample[:,0]+data_sample[:,1])*math.sqrt(2)/2.0
    #data_110[:,1] = (-data_sample[:,0]+data_sample[:,1])*math.sqrt(2)/2.0
    #data_110[:,2] = data_sample[:,2]
    #%% Plot 3D crystal structure 011
    if plot == True:
        df = pd.DataFrame(data_110,columns=['a','b','c','d'])
        group_1 = df[df.d==56].values
        group_2 = df[df.d==24].values
        
        fig = plt.figure()
        ax = plt.subplot(111, projection='3d')  # build a project
        ax.scatter(data_110 [:, 0], data_110 [:, 1], data_110 [:, 2],c=data_110 [:, 3], s=8)  # 绘制数据点
        #ax.plot(group_1 [:, 0], group_1 [:, 2], 'p', zdir = 'y', label = 'Al')    #divide it into different parts
        #ax.plot(group_2 [:, 0], group_2 [:, 2], 'o', zdir = 'y', label = 'Mg')    #divide it into different parts
        
        # plt.legend(loc='upper right')
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_zlabel('Z', fontsize=16)  # axis
        ax.set_ylabel('Y', fontsize=16)
        ax.set_xlabel('X', fontsize=16)
        plt.show()
    #%%
    return data_110
#%%
def Euler_transformation_111(data_clean, plot):
    #%%  change pole from 111 to 001
    row = data_clean.shape[0]
    data_111 = np.empty([row,4], dtype = float)
    data_111[:,3] = data_clean[:,3]
    
    #rotate [111]
    data_111[:,0] = data_clean[:,0]*0.408248 + data_clean[:,1]*0.408248 + data_clean[:,2]*(-0.816497)
    data_111[:,1] = data_clean[:,0]*(-0.707107) + data_clean[:,1]*0.707107 + data_clean[:,2]*(0.0)
    data_111[:,2] = data_clean[:,0]*0.57735 + data_clean[:,1]*(0.57735) + data_clean[:,2]*(0.57735)
    
    data_110 = data_111
    #%% Plot 3D crystal structure 111
    if plot == True:  
        df = pd.DataFrame(data_110,columns=['a','b','c','d'])
        group_1 = df[df.d==56].values  #Al
        group_2 = df[df.d==7].values  #Li
        group_3 = df[df.d==24].values   #Mg
        
        fig = plt.figure()
        ax = plt.subplot(111, projection='3d')  # build a project
        
        ax.scatter(data_110 [:, 0], data_110 [:, 1], data_110 [:, 2],c=data_110 [:, 3], s=8)  # 绘制数据点
        
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.set_zlabel('Z', fontsize=16)  # axis
        ax.set_ylabel('Y', fontsize=16)
        ax.set_xlabel('X', fontsize=16)
        plt.show()
    #%%
    return data_110
#%%