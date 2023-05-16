# Kantar_hackathon

Welcome to Kantar Hackathon with Databricks. The main goal of this hacakthon is to enable you to use Databricks Lakehouse Platfrom to support an E2E use case including:
- Ingestion
- Data Engineering
- Data Science
Throughout this Hackathon you will be achieving the following:
- Ingest Data from the cloud location (CSV)
- Split the data in 2 equal pieces
- Store the first one in Delta format in a Bronze layer
- Store the second one in multiple json files in your workspace DBFS putting 100 records in each file
- Do some DE on the bronze table and produce silver table(s)
- Create a Feature Store Table
- Use the Feature Store table to train a model
- Create a stream from the json location to a landing zone on the DBFS, that will read one json file at a time and write to the landing zone
- Use DLT to read from the landing zone and update the bronze and silver tables
- Update also the feature store table from the landing zone
- Create an inference pipeline to use the model you have created and create a gold table with the predictions 
