from pyspark.sql.functions import *
from pyspark.sql.types import *
from spark.read import *
from cfg.configs import *
import json

# preprocessing data of family json, grouping by sku
def adjust_json():
    with open(cfg['sector']['path'], 'r') as file:
        familiasetor = file.read()

    list_df = []

    data = json.loads(familiasetor)

    keys = data['sku'].keys()

    for key in keys:
        sku = data['sku'][key]
        family = data['familia'][key]
        sector = data['setor'][key]
        data_dict = {'file_row_number': key, 'sku': sku, 'family': family, 'sector': sector}
        list_df.append(data_dict)
    return list_df

# transform list in dataframe
def sector_processing(list_df):
    rdd = spark.sparkContext.parallelize(list_df)
    df = spark.createDataFrame(rdd) \
        .withColumn('sku', col('sku').cast('int')) \
        .withColumn('current_date', current_timestamp())
    return df
    