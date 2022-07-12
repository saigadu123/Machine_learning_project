from housing.logger import logging
from housing.exception import HousingException
from housing.entity.artifact_entity import ModelPusherArtifact,ModelEvaluationArtifact
from housing.entity.config_entity import ModelPusherConfig
import os,sys
import shutil 

class ModelPusher:

    def __init__(self,model_pusher_config:ModelPusherConfig,model_evaluation_artifact:ModelEvaluationArtifact):
        try:
            logging.info(f"{'>>' * 30}Model Pusher log started.{'<<' * 30} ")
            self.model_pusher_config = model_pusher_config
            self.model_evaluation_artifact = model_evaluation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e 

    






