#!/bin/bash
# Move into the dsa-airflow directory and make subdirs
cd dsa-airflow
mkdir ./logs ./plugins

# download the docker-compose.yaml and set the .env
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env


# initialize airflow 
docker-compose up airflow-init
