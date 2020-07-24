"""
python xxxx.py runserver -h(ip地址) -p(端口号) -d(开启调试模式)
"""
from flask import Flask, jsonify
from flask_script import Manager

app = Flask(__name__)

# 2.创建Manager对象, 关联app
# manager = Manager(app)
from flask_function import blue

app.register_blueprint(blue)

if __name__ == '__main__':
    # manager.run()
    app.run(host='108.88.4.4', port=5001)

