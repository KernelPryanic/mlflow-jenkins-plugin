# mlflow-jenkins-plugin
Simple Jenkins plugin for MLflow

Triggers jenkins webhook for every [Model Version stage transition](https://www.mlflow.org/docs/latest/model-registry.html#transitioning-an-mlflow-models-stage).

### Usage
Configure Jenkins Credentials using the following evironment variables:
- MLFLOW_JENKINS_CALLBACK_URL
- MLFLOW_JENKINS_ACTION
- MLFLOW_JENKINS_USER
- MLFLOW_JENKINS_TOKEN
