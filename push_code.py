import os
import sys
import json
from dotenv import load_dotenv
from networksecuirty.exection.exection import execution
load_dotenv()
mongodb_url = os.getenv("mongodb_url")
import certifi
ca = certifi.where()
import pymongo
import pandas as pd
import numpy as np
from networksecuirty.exection import exection
from networksecuirty.logging import Logger

class networksecuirty:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise  exection(e,sys)
    def cv_josn(self,json_file):
        try:
         data = pd.read_csv(json_file)
         #reset the index of the dataframe
         data.reset_index(drop=True, inplace=True)
         #convert into json my csv data 
         recode = list(json.loads(data.T.to_json()).values())
         return recode
        except Exception as e:
            raise  exection(e,sys)

    def insert_data(self,collection,database,record):
        try:
            self.collection = collection
            self.database = database
            self.record = record
            #connect to the mongodb database
            self.client = pymongo.MongoClient(mongodb_url)
            #connect to the database and collection
            self.database = self.client[self.database]
            #connect to the collection
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.record)
            return(len(self.record))
        except Exception as e:
            raise  exection(e,sys)
if __name__ == "__main__":
    file_path ="network_data\phisingData.csv"
    database = "networksecuirty"
    collection = "phisingData"
    networkobject = networksecuirty()
    recode = networkobject.cv_josn(file_path)
    #insert the data into the database
    inserted_data = networkobject.insert_data(collection,database,recode)
    #print the number of records inserted
    print(f"{inserted_data} records inserted into the {collection} collection in the {database} database.")
  
       