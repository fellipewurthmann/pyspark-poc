from etls.billing import *
from etls.sector import *
from etls.freight import *
from etls.weight import *
from spark.session import getSparkSession

spark = getSparkSession()


def test_billing():
    lst = [("number", 1)]
    df = spark.createDataFrame(lst)
    var = billing_processing()
    assert type(var) == type(df)


def test_weight():
    lst = [("number", 1)]
    df = spark.createDataFrame(lst)
    var = weight_processing()
    assert type(var) == type(df)


def test_sector():
    lst = [("number", 1)]
    df = spark.createDataFrame(lst)
    var = sector_processing(adjust_json())
    assert type(var) == type(df)


def test_freight():
    lst = [("number", 1)]
    df = spark.createDataFrame(lst)
    var = freight_processing()
    assert type(var) == type(df)


def test_adjust_json():
    lst = []
    json = adjust_json()
    assert type(json) == type(lst)
