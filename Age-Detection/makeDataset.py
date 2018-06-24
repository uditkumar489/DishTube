# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:45:02 2017

@author: Jaadugar
"""
#Importing Libraries
import pandas as pd

#Loading Train dataset
train=pd.read_csv('train.csv')

#Copying files to the folder
from shutil import copyfile
for i in range(len(train)):
    myCat=train.get_value(index=i,col='Class')
    src='Train/'+train.get_value(index=i,col='ID')
    dst='dataset/'+ myCat +'/'+ train.get_value(index=i,col='ID')
    copyfile(src, dst)
