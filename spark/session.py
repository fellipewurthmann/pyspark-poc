from pyspark.sql import SparkSession

def getSparkSession():
	spark = SparkSession \
		.builder \
	    .getOrCreate()
	return spark
