import os
import sys
from datetime import datetime
from networksecuirty.constants.training_pipline import *
class training_pipeline_config:
    def __init__(self):
        timestamp=datetime.now().strftime("%m%d%Y__%H%M%S")
        self.pipeline_name=Pipline_name
        self.artifact_dir=Artifact_dir
        self.artifact_dir=os.path.join(Artifact_dir,timestamp)
        self.timestamp:str=timestamp
class data_ingestion_config:
    def __init__(self,training_pipeline_config:training_pipeline_config):
        self.data_ingestion_collection_name=data_ingestion_collection_name
        self.data_ingestion_database_name=data_ingestion_database_name
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,data_ingestion_dir)
        self.data_ingestion_feature_store_dir=os.path.join(self.data_ingestion_dir,data_ingestion_feature_store_dir)
        self.data_ingestion_train_test_dir=os.path.join(self.data_ingestion_dir,data_ingestion_train_test_dir)
        self.data_ingestion_test_size=data_ingestion_test_size
        