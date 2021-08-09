from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is my first flask application"

@app.route('/hello',methods=['Get'])
def home():
    return "This is my  flask home"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)


