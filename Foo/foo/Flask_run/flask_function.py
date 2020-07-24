# 1.导入蓝图
from flask import Blueprint, jsonify
from Foo.foo.MysqlDb.mysqldb import MysqlDb

# 2.创建蓝图对象
blue = Blueprint('function', __name__)


# 3.使用蓝图对象装饰视图函数
@blue.route('/detail1')
def detail1():
    return 'detail1'


@blue.route('/detail2')
def detail2():
    return 'detail2'


@blue.route('/detail3')
def detail3():
    return 'detail3'


@blue.route('/detail4')
def detail4():
    return 'detail4'


@blue.route('/detail5')
def detail5():
    return 'detail5'


@blue.route('/detail6')
def detail6():
    return 'detail6'


@blue.route('/')
def index():
    mydb = MysqlDb()
    data = mydb.connect_db()
    data = {
        'name': data,
        'age': 13
    }
    return jsonify(data)
