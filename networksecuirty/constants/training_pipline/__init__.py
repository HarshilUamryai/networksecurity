import os
import sys
import numpy as np
import pandas as pd

#we can define the constants for the training pipeline in this file
Target_column = "result"
Pipline_name:str ="networksecuirty"
Artifact_dir:str="artifact"
File_names:str="phisingData.csv"
file_train:str="train.csv"
file_test:str="test.csv"
#data ingestion constants
data_ingestion_collection_name:str="phisingData"
data_ingestion_database_name:str="networksecuirty"
data_ingestion_dir:str="data_ingestion"
data_ingestion_feature_store_dir:str="feature_store"
data_ingestion_train_test_dir:str="train_test"
data_ingestion_test_size:float=0.2
