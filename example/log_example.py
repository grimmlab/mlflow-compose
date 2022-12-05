import mlflow
import os

#os.environ['NO_PROXY'] = '10.154.6.32'
os.environ["AWS_ACCESS_KEY_ID"] = "<Minio Key ID>"
os.environ["AWS_SECRET_ACCESS_KEY"] = "<Minio Access key>"
os.environ["MLFLOW_S3_IGNORE_TLS"] = "true"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://<Server IP>:<S3_PORT>" # How to reach MinIO server. should be the host ip and S3_PORT in .env file
# Mlflow username and password. Should be MLFLOW_USER and MLFLOW_PASSWORD in .env
os.environ['MLFLOW_TRACKING_USERNAME'] = "<MLFLOW_USER>"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "<MLFLOW_PASSWORD>"

remote_server_uri = "http://<Server IP>:<PORT>" # set to MLFlow server URI (host ip and PORT in .env)
mlflow.set_tracking_uri(remote_server_uri)

mlflow.set_experiment("Test Experiment")
mlflow.set_tag("mlflow.runName", "Test Run")
mlflow.log_artifact("./gandalf.gif")
mlflow.log_metric("test_metric", 0.22)

mlflow.log_params({
    "test_param": 0.42 
})

mlflow.end_run()