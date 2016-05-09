# Relevant Features for Modeling CRISPR Guide Efficiencies 


##Maya Anand and Rachel Mester
###Final Project for COMS W4771 


Our project focused on improving the decision tree model used by Fusi et al for CRISPR guide efficiency prediction. We examined whether the inclusion of additional features would increase the accuracy of the model on the testing set and decrease the variance of results.  CRISPR/Cas9 technology is relatively new and the features that affect the effectiveness of guides are not thoroughly understood.  Therefore we came up with features similar to other successful features in the Fusi et al model, such as the NGGXX feature (similar to the original NGGX) and the count PAM and count repeat (similar to the original count GC). 

Here is the  [**official project page**](http://research.microsoft.com/en-us/projects/azimuth/) for the Fusi et al model. 

**John G. Doench**\*, **Nicolo Fusi**\*, Meagan Sullender\*, Mudra Hegde\*, Emma W. Vaimberg\*, Katherine F. Donovan, Ian Smith, Zuzana Tothova, Craig Wilen , Robert Orchard, Herbert W. Virgin, **Jennifer Listgarten**\*, **David E. Root**.  
[**Optimized sgRNA design to maximize activity and minimize off-target effects for genetic screens with CRISPR-Cas9**](#). *Nature Biotechnology*, 2016.  
(\* = equal contributions, **corresponding author**)  

#### Installation

To run and access our modifications to the code, you can clone this repository.

To run Fusi et al's unit tests, navigate to the main Azimuth directory, and then from the command prompt, type
```shell
nosetests
```
If these pass, you will see "OK" as the last printout.


#### Getting started

From python, you can get predictions from our model by navigating to the azimuth folder (within the main Azimuth folder) and running:

```python test_prediction.py saved_models/name_of_pickle.pickle prediction.csv ```

The first command line argument should be the name of the pickle file corresponding to the model you want to run (saved_models/name_of_pickle.pickle) and the second command line argument should be the name of the .csv file where the guide efficiency predictions should be saved.

- For Model 1: model_1_nopos.pickle
- For Model 2: model_2_nopos.pickle
- For Model 3: model_3_nopos.pickle
- For Model 4: model_4_nopos.pickle
- For Model 5: model_5_nopos.pickle
- For Model 6: model_6_nopos.pickle
- For Model 7: model_7_nopos.pickle
- For Model 8: model_8_nopos.pickle
- For original Fusi et al model: original_nopos.pickle

#### Files Included
Many files in this repository came from the Fusi et al Azimuth project and are needed for our model to run. Below are outlined the main files that we made modifications to or created. All files can be found in the azimuth folder.

- model_comparison.py: creates the model (saved as a .pickle model) and also has a method that runs the model on a given guide sequence
	-  main method: creates the original model based on the training data provided.  The part that we changed is that we included the keys "repeat_count", "PAM_count", and "NGGXX" into the dictionary of learn_options.  These features should be set to True when they are to be included in the model and set to None otherwise.  
	-  save_final_model_V3 method: called by the main method to save the model into a .pickle file. Again, the keys "repeat_count", "PAM_count", and "NGGXX" are added to the dictionary of learn_options.  These features should be set to True when they are to be included in the model
and set to None otherwise.  
	- predict method: This method is passed guide sequence, cut point and percent peptide as numpy arrays as parameters and runs the specified model on the given sequence. This process is fully automated in our test_prediction.py script.  

- features/featurization.py: defines all features, including our added features.
	- NGGXX_interaction_feature method: This method creates the NGGXX feature modeled off of the NGGX feature in the original model.  It takes in the 30 nucleotide data sequence, and then encodes the nucleotides in positions 24, 27, 28 into a one hot encoding representing the N, X, and X nucleotides.
	- countRepeat method: This method creates the countRepeat feature modeled off of the countGC feature in the original model.  It takes in the data sequence and then counts the total number of repeats in the sequence.  This number is returned as an integer.
	- countPAM method: This method creates the countPAM feature modeled off of the countGC feature in the original model.  It takes in the data sequence and then counts the PAM codons in the sequence.  This number is returned as an integer.
	- repeat_count method: This method creates three separate features out of the countRepeat feature, modeled off of the gc_features method in the original model.  It takes in the data and applies the countRepeat method (detailed above).  Then it separates out the three features Repeat = 0, Repeat > 0, and Repeat Count.
	- PAM_count method: This method creates three separate features out of the countPAM feature, modeled off of the gc_features method in the original model.  It takes in the data and applies the countPAM method (detailed above).  Then it separates out the three features PAM = 1, PAM > 1, and PAM Count.
	- featurize_data method: This method converts the features specified in learn_options into usable feature sets.  The parts that we edited were to add the countPAM and countRepeat features into the feature sets.  The count PAM feature was partitioned into three separate features:  PAM = 1 (boolean), PAM > 1 (boolean), and PAM count (integer).  Similarly, the count repeat feature was partitioned into three features: Repeat = 0 (boolean), Repeat > 0 (boolean), and Repeat Count (integer).  These features are converted to sets with the appropriate labels using the pandas.DataFrame package.

- testdata.py: takes an excel file of guide sequences, cut points and percent peptides and returns the appropriate numpy arrays needed to run the model

- test_prediction.py: runs the specified existing model on the given excel file of guide sequences and creates a .txt file with the Gini Importances of the features of the model and a .csv file of the predicted guide efficiencies. The Gini Importances will be saved in the file "GINIImportance.txt" and the predictions will be saved with the filename specified.


- data files
	- FC_plus_RES_withPredictions_original.csv: This file is original to the Fusi et al paper.  It contains the testing data set from their V3 model.
	- testdata.xlsx: This file contains all of the testing data that we used in our model (both from the V1 and V2 data sets). It is a randomly selected 20%of each original data set.
	- V1_data_original.xlsx: This file is original to the Fusi et al paper.  It contains the testing data set from their V1 model. 
	- V1_data.xlsx: This file contains all of the training data that we used in our model that was originally from the V1 dataset.  It is separated from the V1 data for code syntax purposes only, and is not computationally used any differently than the data in the V2_data.xlsx.
	- V1_suppl_data.txt: This file is original to the Fusi et al paper.  It contains additional information on the V1 data set that can be used in optional features of the model.
	- V2_data_original.xlsx: This file is original to the Fusi et al paper.  It contains the testing data set from their V2 model
	- V2_data.xlsx: This file contains all of the training data that we used in our model that was originally from the V2 dataset.  It is separated from the V1 data for code syntax purposes only, and is not computationally used any differently than the data in the V1_data.xlsx.  

#### Dependencies
Our code is written in Python 2.7 and should run on a standard machine.

The following packages must be installed to use our models:

* scipy
* numpy
* matplotlib
* nose
* scikit-learn>=0.17
* pandas
* biopython
 
#### Contacting us 
 
If you have any questions, please contact: mva2112@columbia.edu and rsm2166@columbia.edu


