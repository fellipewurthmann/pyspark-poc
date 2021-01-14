from pyspark.sql.functions import *
from pyspark.sql.types import *
from spark.read import *
from cfg.configs import *

def weight_processing():
    df = reader(cfg['weight']['path'], \
    	cfg['weight']['format'],
    	cfg['weight']['encoding'],
    	cfg['weight']['delimiter']) \
        .withColumn('weight', regexp_replace(col('_c1'), '[^0-9 .]', '').cast('float')) \
        .withColumn('sku', col('_c0').cast('int')) \
        .withColumn('current_date', current_timestamp()) \
        .drop('_c0', '_c1')
    return df