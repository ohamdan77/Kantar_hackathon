# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC Data is  in *s3://files.training.databricks.com/ohamdan/creditcard.csv*:
# MAGIC * Create a Database to store the Delta tables meta data
# MAGIC * Ingest the data from the S3 location 
# MAGIC * Split the data in 2 half: first half in the delta bronze table and the second half in a json dir with 100 records in every json file
# MAGIC * Make sure that the data has the needed columns to create a feature store table from it
# MAGIC * Create 2 silver tables from the data:
# MAGIC   * first one with all the features 
# MAGIC   * second with the label in it
# MAGIC
# MAGIC
# MAGIC
# MAGIC In Case the data is not reachable from the S3 Bucket you can download it from Kaggle following the code below. Do not forget to change the username and the KAGGLE_KEY to be yours

# COMMAND ----------

# DBTITLE 0,In case the S3 data is not reachable you can download the data from Kaggle
# MAGIC %sh 
# MAGIC pip install kaggle
# MAGIC export KAGGLE_USERNAME=omarhamdandata
# MAGIC export KAGGLE_KEY=6fa85eea9baf2ea4c1682d7701910799
# MAGIC kaggle datasets download -d mlg-ulb/creditcardfraud -p /dbfs/creditcard/data/
# MAGIC cd /dbfs/creditcard/data/ &&  unzip /dbfs/creditcard/data/creditcardfraud.zip
