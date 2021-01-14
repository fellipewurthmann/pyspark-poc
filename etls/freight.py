from pyspark.sql.functions import *
from pyspark.sql.types import *
from spark.read import *
from cfg.configs import *

def freight_processing():
    df = reader(cfg['freight']['path'],
    	cfg['freight']['format'],
    	cfg['freight']['encoding'],
    	cfg['freight']['delimiter'],
    	cfg['freight']['header']) \
        .withColumnRenamed('_c0', 'id') \
        .withColumn('freight_cost', regexp_replace(col('custo_frete'), ',', '.')) \
        .withColumn('freight_cost', regexp_replace(col('freight_cost'), '[^0-9.]', '').cast(DecimalType(17, 4))) \
        .withColumn('current_date', current_timestamp()) \
        .drop('custo_frete')
    return df
