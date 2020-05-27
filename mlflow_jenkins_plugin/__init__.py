import os

import requests
from mlflow.store.model_registry.sqlalchemy_store import SqlAlchemyStore


class PluginSqlAlchemyStore(SqlAlchemyStore):
    def __init__(self, store_uri=None):
        path = store_uri
        self.is_plugin = True
        super(PluginSqlAlchemyStore, self).__init__(path)

    def transition_model_version_stage(self, name, version, stage, archive_existing_versions):
        jenkins_callback_url = os.getenv("MLFLOW_JENKINS_CALLBACK_URL", None)
        jenkins_action = os.getenv("MLFLOW_JENKINS_ACTION", None)
        jenkins_user = os.getenv("MLFLOW_JENKINS_USER", None)
        jenkins_token = os.getenv("MLFLOW_JENKINS_TOKEN", None)

        if jenkins_callback_url is not None and jenkins_user is not None and \
                jenkins_token is not None and jenkins_action is not None:
            mlflow_model_url = self.get_model_version_download_uri(
                name, version)

            params = {"ACTION": jenkins_action, "MODEL_NAME": name, "MODEL_VERSION": version,
                      "MODEL_STAGE": stage, "MODEL_URL": mlflow_model_url}
            requests.post(jenkins_callback_url, params=params,
                          auth=(jenkins_user, jenkins_token), verify=False)

        return super(PluginSqlAlchemyStore, self).transition_model_version_stage(
            name, version, stage, archive_existing_versions)
