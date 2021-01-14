from etls.billing import *
from etls.sector import *
from etls.freight import *
from etls.weight import *
from spark.read import *
from spark.write import *
from cfg.configs import *
from spark.session import getSparkSession


def main():
    spark = getSparkSession()
    billing = billing_processing()
    weight = weight_processing()
    freight = freight_processing()

    list_df = adjust_json()
    sector = sector_processing(list_df)

    writer_jdbc(billing, "billing")
    writer_jdbc(weight, "weight")
    writer_jdbc(freight, "freight")
    writer_jdbc(sector, "sector")


if __name__ == "__main__":
    main()
