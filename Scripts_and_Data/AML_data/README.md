# Data available for use:
1. Requirements.txt: *Includes the main python libraries used and indicates the Python version*
2. filteredProbes.pkl: *The 406830 CpG sites after filtering*
3. pheno.pkl: *Pickle file containing patient information including public_id, sample type (diagnosis/relapse), FAB, genotype(subtype), relapse status*
4. phenotypes.csv *File containing patient information including public_id, sample type (diagnosis/relapse), FAB, genotype(subtype), relapse status*
5. Unionindices.pkl: *1300 CpGs selected by the two Feature Selection Approaches*
6. DLSubtype_ClassificationHyperoptAlldata.h5: *steps & hyperparameter information for the Neural Network model produced from Hyperparameter Optimization & Model Selection*
7. sklearn_pipelineDLClassification.pkl: *The pipeline of the Neural Network that will be fed by the model steps from the .h5 file*
8. DLSubtype_ClassificationHyperoptAlldataFITTED.h5: *steps & hyperparameter information for the Neural Network model produced after fitting the model on all training samples*
9. sklearn_pipelineDLClassificationFITTED.pkl: *The pipeline of the Neural Network that will be fed by the model steps from the .h5 file* 
10. DLSubtype_ClassificationHyperoptAllknowndataFinal.h5: *steps & hyperparameter information for the Neural Network model produced after fitting the model on all samples of known subtype (train+test sets)*
11. sklearn_pipelineDLClassificationAllknowndataFinal.pkl: *The pipeline of the Neural Network that will be fed by the model steps from the .h5 file* 

Additional files that are not included since they are large files: meth.pkl-which can be produced by the first steps of the analysis, annotation2.csv that contains information on CpGs and Genes that was used for CpG site annotation (Available after request).
Finally, AllSubtypesPredicted.csv for survival analysis is available on the supplementary Table S1 of the manuscript. 
