# write a apache spark job that reads in the data from a csv file into a dataframe, then prints out.

import sys
from operator import add

from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

    df = read_data(spark)

    # print out first 10 rows of the dataframe
    df.show(10)


# read in the data from a csv file into a dataframe, infer the schema
def read_data(spark):
    