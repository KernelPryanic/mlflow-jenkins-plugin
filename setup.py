from setuptools import find_packages, setup

setup(
    name="mlflow-jenkins-plugin",
    version="0.1.0",
    description="Jenkins plugin for MLflow",
    packages=find_packages(),
    install_requires=["mlflow"],
    entry_points={
        "mlflow.model_registry_store":
            "postgresql=mlflow_jenkins_plugin:PluginSqlAlchemyStore",
    },
)
