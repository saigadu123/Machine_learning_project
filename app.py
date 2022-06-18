from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    try:
        raise Exception("We are testing custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are doing custom logging")
    return "My name is sai krishna Studying in SRM University Chennai"


if __name__ == "__main__":
    app.run(debug=True)