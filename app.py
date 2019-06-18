from flask import Flask
from polls.controller import bq

app = Flask(__name__)
app.register_blueprint(bq)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
