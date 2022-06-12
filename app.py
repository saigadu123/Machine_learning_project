from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return "My name is sai krishna (Data Scientist) in Fractal Analytics Banglore"


if __name__ == "__main__":
    app.run(debug=True)