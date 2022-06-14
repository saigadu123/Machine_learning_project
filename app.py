from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return "My name is sai krishna Studying in SRM University Chennai"


if __name__ == "__main__":
    app.run(debug=True)