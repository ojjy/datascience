from flask import Flask



app = Flask(__name__)    # if conn is not None:


@app.route('/')
def hello_world():

    return 'Hello World!'


if __name__ == '__main__':



    app.run()
