from networksecuirty.logging.Logger import logging
from networksecuirty.enitity.config_enitity import training_pipeline_config,data_ingestion_config
from networksecuirty.enitity.enitity_artfects import EntityArtifacts
from networksecuirty.exection.exection import execution
import os 
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import pymongo
from sklearn.model_selection import train_test_split
from networksecuirty.constants.training_pipline import File_names

from dotenv import load_dotenv

load_dotenv()
mongo_url=os.getenv("MONGO_URL")

class data_reader_config:
    def __init__(self,data_ingestion_config:data_ingestion_config):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise execution(str(e),sys)
#it reader data from local file and return it as a dataframe
    def get_data_from_local(self,dataframe:pd.DataFrame):
        try:
            data_ingestion_feature_storer=self.data_ingestion_config.data_ingestion_feature_store_dir
            dir_path=os.path.join(data_ingestion_feature_storer,"phisingData.csv")
            os.makedirs(data_ingestion_feature_storer,exist_ok=True)
            dataframe.to_csv(dir_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise execution(str(e),sys)
#this function  get_data_from_mongo is used just read data from mongo db and return it as a dataframe        
    def get_data_from_mongo(self):
        try:
            client = pymongo.MongoClient(mongo_url)
            database_name = self.data_ingestion_config.data_ingestion_database_name
            collection_name = self.data_ingestion_config.data_ingestion_collection_name
            db = client[database_name]
            collection = db[collection_name]
            data = list(collection.find())
            df = pd.DataFrame(data)
            if '_id' in df.columns:
                df = df.drop('_id', axis=1)
            df.replace([np.inf, -np.inf], np.nan, inplace=True)
            return df
        except pymongo.errors.ServerSelectionTimeoutError as e:
            local_dataset_path = Path(__file__).resolve().parents[2] / "network_data" / File_names
            if not local_dataset_path.is_file():
                raise execution(
                    f"MongoDB is unavailable and the local fallback dataset was not found: {local_dataset_path}",
                    sys,
                ) from e
            logging.warning(
                "MongoDB is unavailable; using the local dataset at %s instead.",
                local_dataset_path,
            )
            try:
                return pd.read_csv(local_dataset_path)
            except Exception as local_error:
                raise execution(
                    f"Failed to read the local fallback dataset at {local_dataset_path}: {local_error}",
                    sys,
                ) from local_error
        except Exception as e:
            raise execution(str(e),sys)
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.data_ingestion_test_size,random_state=42)
            train_file_path=os.path.join(self.data_ingestion_config.data_ingestion_train_test_dir,"train.csv")
            test_file_path=os.path.join(self.data_ingestion_config.data_ingestion_train_test_dir,"test.csv")
            os.makedirs(self.data_ingestion_config.data_ingestion_train_test_dir,exist_ok=True)
            train_set.to_csv(train_file_path,index=False,header=True)
            test_set.to_csv(test_file_path,index=False,header=True)
        except Exception as e:
            raise execution(str(e),sys)
    def data_ingestion(self):
        try:
            dataframe = self.get_data_from_mongo()
            dataframe = self.get_data_from_local(dataframe)
            self.split_data_as_train_test(dataframe)
            artifacts=EntityArtifacts(train_data_path=os.path.join(self.data_ingestion_config.data_ingestion_train_test_dir,"train.csv"),
                                      test_data_path=os.path.join(self.data_ingestion_config.data_ingestion_train_test_dir,"test.csv"))
            return artifacts
        except Exception as e:
            raise execution(str(e),sys)

