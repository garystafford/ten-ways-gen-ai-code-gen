# Purpose: Reads in the data from a csv file
# Author: Gary A. Stafford
# Date: 2023-04-02

# This code creates a SparkSession and reads in the data from a csv file
# into a dataframe. The dataframe is then printed out.


from pyspark.sql import SparkSession


def main():
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .getOrCreate()

    df = read_data(spark)

    # print out first 10 rows of the dataframe
    df.show(10)


# read in the data from a csv file into a dataframe, infer the schema
def read_data(spark):
    """Load data from raw data path and return a dataframe.

    Args:
        spark: SparkSession object.

    Returns:
        df: Dataframe containing the data from a specific source.
    """

    df = spark.read.csv("data.csv", header=True, inferSchema=True)
    return df


if __name__ == "__main__":
    main()
