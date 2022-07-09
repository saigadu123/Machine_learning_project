from housing.exception import HousingException
import sys
from housing.logger import logging
from typing import List
from housing.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from housing.entity.config_entity import ModelTrainerConfig
from housing.util.util import load_numpy_array_data,load_object,save_object
from housing.entity.model_factory import MetricInfoArtifact,ModelFactory,GridSearchBestModel
from housing.entity.model_factory import evaluate_regression_model

class HousingEstimatorModel:
    def __init__(self,preprocessing_object,trained_model_object):
        """
        TrainedModel constructor
        preprocessing_object: preprocessing_object
        trained_model_object: trained_model_object
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self,X):
        """
        function accepts raw inputs and then transformed raw input using preprocessing_object
        which gurantees that the inputs are in the same format as the training data
        At last it perform prediction on transformed features
        """
        transformed_feature = self.preprocessing_object.transform(X)
        return self.trained_model_object.predict(transformed_feature)

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"


class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
        try:
            logging.info(f"{'>>' * 30}Model trainer log started.{'<<' * 30} ")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            logging.info(f"Loading transformed training dataset")
            transformed_train_file_path = self.data_transformation_artifact.transformed_train_file_path
            train_array = load_numpy_array_data(file_path = transformed_train_file_path)

            logging.info(f"Loading Transformed test dataset")
            transformed_test_file_path = self.data_transformation_artifact.transformed_test_file_path
            test_array = load_numpy_array_data(file_path=transformed_test_file_path)

            logging.info(f"Splitting train and test dataset into features and target")
            x_train,y_train,x_test,y_test = train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]

            logging.info(f"Extracting the model config file")
            model_config_file_path = self.model_trainer_config.model_config_file_path

            
            logging.info(f"Initializing model factory class using above model config file: {model_config_file_path}")
            model_factory = ModelFactory(model_config_path=model_config_file_path)

            base_accuracy = self.model_trainer_config.base_accuracy
            logging.info(f"Expected Accuracy: {base_accuracy}")

            logging.info(f"Initating operation model selection")
            
        except Exception as e:
            raise HousingException(e,sys) from e

    
