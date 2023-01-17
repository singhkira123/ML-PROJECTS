import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolab")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABAE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"rows and colums: {df.shape}")

    # convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])



    client[DATABAE_NAME][COLLECTION_NAME].insert_many(json_recordl)
    