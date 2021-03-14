from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='test', password='password')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
