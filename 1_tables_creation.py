# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC Data is  in *s3://files.training.databricks.com/ohamdan/creditcard.csv*:
# MAGIC * Create a Database to store the Delta tables meta data
# MAGIC * Ingest the data from the S3 location 
# MAGIC * Split the data in 2 half in the delta bronze table and half in a json dir with 100 records in every json file
# MAGIC * Make sure that the data has the needed columns to create a feature store table from it
# MAGIC * Create 2 silver tables from the data:
# MAGIC   * first one with all the features 
# MAGIC   * second with the label in it
