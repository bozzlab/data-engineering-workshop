# data-engineering-workshop

## Python Example  
### Reference : https://snakify.org/   

 
## SQL Example   
### Reference : https://sqlbolt.com/  

## Initial Project

```
pipenv shell --python 3
pipenv install ipykernel
python -m ipykernel install --user --name=$(basename $PWD)
pipenv install jupyterlab
```

## Run/Start

```
jupyter-lab
```

Or, Run python as specific file. 

```
python filename.py
```


## GCLOUD SDK CLI

### Get bucket list
```
gsutil ls 
```

### Copy object into storage 
```
gsutil cp <source_file> <dest_storage>
```

### Delete object storage
```
gsutil delete <bucket_url>/path
```

### Get datasets list
```
bq ls 
```

### BigQuery load CSV data
```
bq load \
--autodetect \
--source_format=CSV \
<datasets>.<table> \
gs://<bucket>/<file>.csv
```

### Create composer cluster (Apache Airflow)
```
gcloud composer enviroments create <composer_name> \
       --location <location> \
       --disk-size <size> \ 
       --node-count <number> \
       --python-version <version>
```
You will got kubernetes cluster, stackdriver, storage  

### Map volume file
```
gs://<bucket>/data <=> /home/airflow/gcs/data
```

### Place DAGs file
```
gsutil cp <dag_file> gs://<bucket_URL>/dags
```
