from spark.session import getSparkSession

spark = getSparkSession()

# read method for load files and set file config
def reader(path, format, encoding, delimiter, header=None):
	df = spark.read.load(
	path=path,
	format=format, 
	encoding=encoding,
	delimiter=delimiter,
	header=header)
	return df
