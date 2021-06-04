#!/usr/bin/env python
# coding: utf-8

# Feature selection

from PCA_feature_contribution_to_PCs import *
import pandas as pd
import numpy as np
from IPython.display import Markdown, display

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import seaborn as sns

import joblib




### PCA: Contribution to each Principal Component (PC)


def PC_contribution(X, n_components, num_features): # num_features * 2 as important probes per component
    
    """
    Arguments 
    
    --X: data matrix of shape n_samples x n_features
    --n_components: number of components that we want to extract information from
    --num_features: number of important features that we want to obtain (note that the pooling takes place from both
    positive and negative sides of the pca loadings so the num of features per component will be double
    
    Returns all unique feature names for the desired PCs number (n_components)
    
    
    """
   
    # run PCA; without specifying the n_components it picks the minimum between n_samples and n_features
    pca = PCA()
    pca.fit(X)
    pcdata = pca.transform(X)
    # Create the loadings dataframe (n_features x n_components)
    cols = X.columns.to_list()
    PCAS = pd.DataFrame(data = pca.components_.T, index = cols)
    var = PCAS.index
    # Call the helper function to get a dataframe with the most important features
    importancedf = PCAcontribution(X, PCAS, n_components, num_features, var, pcdata)
    column_values = importancedf[importancedf.columns].values
    unique_values =  np.unique(column_values)
    
    return unique_values  
    

### Discriminant analysis to find most significant CpG sites


def DA_contribution(X, num_features, group):
        
    """
    Arguments 
    
    --X: data matrix of shape n_samples x n_features
    --num_features: number of important features that we want to obtain (note that the pooling takes place from both
    positive and negative sides of the pca loadings so the num of features per component will be double
    --group: labels for the Discriminant analysis to work with while computing weights
    
    Returns all unique feature names for all DA components
    
    
    """
    
    da = LinearDiscriminantAnalysis()
    da.fit(X, group)
    dadata = da.transform(X)
    # Create the loadings dataframe (n_features x n_components)
    cols = X.columns.to_list()
    DAcomp = pd.DataFrame(data = da.scalings_, index = cols)
    var = DAcomp.index
    n_components = DAcomp.shape[1]
    # Call the helper function to get a dataframe with the most important features
    importancedf = PCAcontribution(X, DAcomp, n_components, num_features, var, dadata)
    
    column_values = importancedf[importancedf.columns].values
    unique_values =  np.unique(column_values)
    
    return unique_values   


### Low Variance & High correlation Filtering

def var_corr_sel(X1, X2, var_thresh, cor_thresh):
        
    """
    Arguments 
    
    --X1: train data matrix of shape train_n_samples x n_features
    --X2: validation/test data matrix of shape val_n_samples x n_features
    --var_thresh: variance threshold to filter out the features with low variance
    --corr_thresh: correlation threshold to filter out the features which are highly correlated
    
    Returns all unique feature names for the desired PCs number (n_components)
    
    
    """
    
    #filter out all probes with variance < var_thresh across all samples
    selector = VarianceThreshold(var_thresh)
    selector.fit(X1)
    indices = list(selector.get_support(indices=True))
    X1a = X1.copy()
    X2a = X2.copy()
    X1a = X1a.iloc[:, indices]
    X2a = X2a.iloc[:, indices]

    # remove high correlated cpgs
    # Create correlation matrix
    corr_matrix = X1a.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find features with correlation greater than the threshold
    to_drop = [column for column in upper.columns if any(upper[column] > cor_thresh)]

    # Drop features 
    X1a.drop(to_drop, axis=1, inplace=True)
    X2a.drop(to_drop, axis=1, inplace=True)
    return X1a, X2a
