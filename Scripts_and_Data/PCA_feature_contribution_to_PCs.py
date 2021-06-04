#!/usr/bin/env python
# coding: utf-8

# # Feature contribution to Principal Components (PC) of PCA

# PCA is a linear data dimensionality reduction transformation, which can remove noise from the data. Each PC is a linear combination of many of the initial features, and explains part of the data variance. Sometimes the first 2 PCs can explain a large %age of the data variance, while in other cases more PCs should be included. With PCA, we manage to reduce the dimensionality of the feature's landscape, without losing important information. In other words with less features (PCs, transformed inputs) we can produce the same or similar outcome by saving time and resources.
# 
# When it comes to target prediction, PCA might not be a problem if we care about e.g. predicting survival rate, drug resistance etc. But we usually need to identify these factors that contribute the most. 
# 
# In this script, I created a function that selects the features that contribute the most on each PC. These features can be later on tested on their own to predict the same target variable and check how the results look like.

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


def PCAcontribution(df, loadings, PCnumber, imp_var, var, embeddings):
    
    """
    Arguments:
    -- df: the original dataframe of shape n_samples X n_features
    -- loadings: PCA loading of shape n_features X n_components
    -- PCnumber: Number of Principal Components to use (It can be less than the selected number of PCs as described)
    -- imp_var: Number of significant variables per component (imp_genes*2); It includes both negative and positive 
    most important values
    -- var: all variables in a list format
    -- embeddings: PCA transformed data of shape n_cells X n_components

    Returns:
    -- importance: a dataframe of shape n_components X important_features(imp_var*2) which includes the names of the 
    important features per PC
    
    """
    var_data = []
    for comp in range(0, PCnumber):
        
        # Get the data for each component and order by loading importance
        
        compdata = loadings.iloc[:, comp]
        sort_loadings = np.argsort(compdata)
        index = np.concatenate((sort_loadings[:imp_var], sort_loadings[-imp_var:])).tolist()
        #append all important features per PC
        var_data.append(var[index].to_list())
        
        
    cols =   ['important_variable' + str(n) for n in range(1, len(var_data[0])+1)]
    rows =  ['comp_' + str(n) for n in range(1, len(var_data)+1)]
    importance = pd.DataFrame(data = var_data, columns = cols, index = rows)    
    return importance