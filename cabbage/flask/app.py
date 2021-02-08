from flask import Flask, render_template, request

import datetime
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


app = Flask(__name__)
# place holder로 값을 넣는다
X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])
# y=ax+b에서 w는 a
W = tf.Variable(tf.random_normal([4,1], name="weight"))
b = tf.Variable(tf.random_normal([1]), name="bias")

# 가설에 넣어 검증
hypothesis = tf.matmul(X, W)+b

# 그래프 빌드하고 세션을 만들어 이 세션을 실행시킴
saver = tf.train.Saver()
model = tf.global_variables_initializer()

sess = tf.Session()
sess.run(model)

# checkpoint file
sava_path = "./model/saved.cpkt"
sava_path(sess, sava_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.methods == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        avg_temp = float(request.form['avg_temp'])
        min_temp = float(request.form['min_temp'])
        max_temp = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])

        price=0
        data = ((avg_temp, min_temp, max_temp, rain_fall),)
        arr = np.array(data, dtype=np.float32)

        x_data = arr[0:4]
        dict = sess.run(hypothesis, feed_dict={X: x_data})
        print(dict[0])
        price = dict[0]

        return render_template('index.html', price=price)


if __name__ == '__main__':
    app.run(debug=True)
