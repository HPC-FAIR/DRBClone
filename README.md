# DRBClone

## Introduction 

This is the demonstration of using CodeBERT as encoder to have a downstream task of clone detection from [BigCloneBench](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Code/Clone-detection-BigCloneBench). 

We are applying Transfer Learning by using our DataRaceBench(DRB) dataset to test the model to run similarity analysis. 



## Setup 

- create virtual environment: 

  `virtualenv --system-site-package <venv_dir_path>` 

- activate virtual environment: 

  `source <venv_dir_path>/bin/activate` 

- install the all the prerequisite in the environment: 

  `pip3 install -r requirements.txt`


**In order to run the program you have to get the best model from BigCloneBench**

**You have to copy the saved_models from Your finished fine-tuning data from BigCloneBench**

## Files

- test.sh: 
  
  commands that runs the testing process

- train.sh: 

  commands that runs the training process (no training dataset yet)

- run.py: 

   Pipeline that can run fine-tuning, and inference 
   
- model.py: 

  stores the model architecture from bigclonebench 
  
- preprocessing.py: 
  
  runs the preprocessing to modify the datasets to the format that can load into the model 

- clustering.py: 

  creates dendrogram, heatmap from the prediction to run clustering 
  
- dataset: 
  
  stores the dataset that generated by preprocessing.py 
  
- graph: 
  
  stores the graph that generated by clustering.py 

## Steps

  1. Once you finished the setup and training the bigclonebench, you will copy the saved_model from the bigclonebench to the current directory. 
  2. To prepare the data, you need to run `python3 preprocessing.py` 
  3. You will now run `./test.sh` to get the prediction
  4. You will then see the similarity score in the `saved_model/prediction.txt`
  5. With the prediction we can run clustering analysis by running `python3 clustering.py`
 


