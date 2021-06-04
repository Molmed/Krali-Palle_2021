# Project Workflow

# DATA PREPARATION

1. Data_Processing_MethylPrep.ipynb: After getting access to the data process it with Methylprep library to get the b-values matrix.
2. data_preparationAML.ipynb: filters the b-values matrix, based on our filtered probes applied (N = 406830) and returns a pandas dataframe. Then, it aligns the Sentrix IDs with the help from the sample sheet metadata with the public ids. It saves the phenotypic and the methylation dataframes for further analysis as pickle (pkl) files.

# DATA VISUALIZATION

1. Visualization-WholeDataSet-UMAP.ipynb: Dimensionality reduction UMAP method (Uniform Manifold Approximation and Projection for Dimension Reduction), to reduce the amount of features (CpGs) and visualize all data for all CpGs projected to 10 UMAP components in 2D dimensional space labelled by FAB and Cytogenetic Subtype
2. Visualization-UMAP_Union.ipynb: Dimensionality reduction UMAP method (Uniform Manifold Approximation and Projection for Dimension Reduction), to reduce the amount of features (CpGs) and visualize all data for the selected  1300 CpGs projected to 10 UMAP components in 2D dimensional space labelled by FAB and Cytogenetic Subtype. Heatmap and Hierarchical clustering follow for the methylation matrix. FAB, Subtype and Relapse status bars are also demonstrated. 

# FEATURE SELECTION

1. PCA_feature_contribution_to_PCs.py: Sorts the input data based on highest and lowest values through np.argsort and extracts features per component (most important features) 
2. Feature_Selection.py: Includes 3 functions: one for PCA, where PCA transformation produces the loadings matrix, which corresponds to a specific value per CpG for each component, which is fed in the function from the previous script to sort the matrix and extract the most important features per Component. B) Discriminant analysis that works more or less as PCA, but instead of using unsupervised selection, you add a group factor to facilitate the selection of features that can separate the different subgroups. C) Low Variance, high correlation feature selection (LVHC). Drops CpGs of low variance and high correlated CpGs based on specific thresholds set by the user.
3. Feature_Selection_CpGs.ipynb: Unsupervised feature selection that utilizes Python scripts **1,2**. Removes the undefined samples, performs 5-fold cross validation and then imputates the missing values. For each fold both PCA contribution and LHVC take in place independently and returns the union of the CpGs per run. At the end all the unique CpGs from all folds are saved. 

# MODEL SELECTION & OPTIMIZATION

1. Subtype-prediction-ModelSelection_HyperparameterOptimization.ipynb: Runs nested Cross Validation to pick the best model per Classifier (outer 5-fold) and select the best set hyperparameters per Classifier (inner 3-fold) with Grid Search. Imputation of the missing values take places within the 5-fold loop. 9 models have been used (8 ML and 1 keras softmax Neural network). The best model is returned and saved for further use.  

# MODEL PERFORMANCE VALIDATION – PREDICT SUBTYPES ON THE TEST SET 

1. PermutationAnalysisDLClassification.ipynb: Use the saved optimized model to perform permutation test on all training data. 
2. Review_TrainFitAll_DLClassification.ipynb: Use the saved optimized model to fit it on all train dataset. The saved model ends with FITTED.
3. Review_TestSetPredictionDLClassification.ipynb: The model generated from step 2 is used to predict the cytogenetic subtype of the test dataset. Final output: a classification report and a confusion matrix. 
4. Review_Train_TestFitAlldata_DLClassification.ipynb: The model generated from step 2 is now fitted on all data of known subtype (train + test datasets). The saved model ends with AllknowndatFinal. This model can be utilized to predict the subtype on the remaining undefined samples.

# IMPORTANT CpGs PER SUBTYPE

1. SignificantCpGs_PerSubtype.ipynb: Utilizes the 99 samples of known subtypes to run a Mann-Whitney U test followed by Benjamini-Hochberg correction to identify the most significant (adjusted p-value < 0.05) CpGs per subtype against all the rest. In a first part, all significant CpGs are included, but then all CpGs that appear across the different subtypes are filtered out. Finally the CpGs are annotated against Human Genome to obtain gene information. At the end of the script a table is generated with gene, CpG site, subtype and methylation information per CpG. 

# SURVIVAL ANALYSIS
1. t(8;21)_survival_analysis.ipynb: Extract the diagnostic t(8;21) samples to identify the top 50 most significant CpGs that separate the patients who experienced relapse from those who did not. Heatmap & Hierarchical clustering was performed and identified two groups of high and low methylation levels. For these two groups Survival Analysis took place to investigate if low/high methylation levels are associated with outcome (death or relapse) by running an Overall survival analysis with main event the death of the patients and Relapse Free Survival Analysis with main event relapse. 
