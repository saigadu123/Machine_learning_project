from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_tranformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path = config_path))
        pipeline.start()
        logging.info("main function execution completed.") 
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()