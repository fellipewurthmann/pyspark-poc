from pyspark.sql.functions import *
from pyspark.sql.types import *
from spark.read import *
from cfg.configs import *

def billing_processing():
    df = reader(cfg['billing']['path'],
	   cfg['billing']['format'],
	   cfg['billing']['encoding'], 
	   cfg['billing']['delimiter']) \
	   .withColumn('current_date', current_timestamp()) \
	   .withColumn('sku', col('sku').cast('int'))
    return df
    