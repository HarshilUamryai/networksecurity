from networksecuirty.logging.Logger import logging
from networksecuirty.exection.exection import execution
from networksecuirty.enitity.config_enitity import training_pipeline_config,data_ingestion_config
from networksecuirty.components.data_reader import data_reader_config

import sys
if __name__ == "__main__":
    try:
      training_pipeline_config=training_pipeline_config()
      data_ingestion_config=data_ingestion_config(training_pipeline_config=training_pipeline_config)
      data_reader_config=data_reader_config(data_ingestion_config=data_ingestion_config)
      datareder=data_reader_config.data_ingestion()
      print(datareder)
      logging.info("This is an info message.")
    except Exception as e:
        raise execution(str(e),sys)